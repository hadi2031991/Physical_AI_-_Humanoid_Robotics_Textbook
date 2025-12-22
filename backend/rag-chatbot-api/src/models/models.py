from datetime import datetime
from typing import List, Optional
import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, JSON, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from ..db import Base # Import Base from the db module

# SQLAlchemy Models (for database ORM)
class Document(Base):
    __tablename__ = "documents"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    source_path = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    checksum = Column(String, nullable=False)
    metadata_ = Column(JSON, name="metadata", nullable=True) # Use metadata_ to avoid conflict with method

    chunks = relationship("Chunk", back_populates="document")

class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(PG_UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)
    text = Column(Text, nullable=False)
    # Embedding will be stored in Qdrant, not directly in Postgres, but we keep its reference if needed.
    # embedding_id = Column(PG_UUID(as_uuid=True), nullable=True) # Reference to Qdrant point ID
    chunk_order = Column(Integer, nullable=False)
    metadata_ = Column(JSON, name="metadata", nullable=True) # Use metadata_ to avoid conflict with method

    document = relationship("Document", back_populates="chunks")

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, index=True, nullable=True) # Optional user ID
    started_at = Column(DateTime, default=datetime.utcnow)
    last_activity_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    messages = relationship("ChatMessage", back_populates="conversation")

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(PG_UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=False)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    relevant_chunks = Column(JSON, nullable=True) # Store as JSON array of UUIDs or strings
    selected_text = Column(Text, nullable=True)
    page_context = Column(Text, nullable=True)
    model_used = Column(String, nullable=False)
    feedback = Column(Integer, nullable=True) # 1-5 rating

    conversation = relationship("Conversation", back_populates="messages")

# Pydantic Models (for API request/response validation and serialization)
from pydantic import BaseModel, Field, HttpUrl

class DocumentBase(BaseModel):
    title: str = Field(..., description="Title of the document.")
    source_path: HttpUrl = Field(..., description="Original file path or URL of the document.")
    checksum: str = Field(..., description="Hash of the document content to detect changes.")
    metadata: Optional[dict] = Field(None, description="Additional metadata for the document.")

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Enable ORM mode for Pydantic (V2)

class ChunkBase(BaseModel):
    document_id: uuid.UUID
    text: str
    chunk_order: int
    metadata: Optional[dict] = None

class ChunkResponse(ChunkBase):
    id: uuid.UUID

    class Config:
        from_attributes = True # Enable ORM mode for Pydantic (V2)

class ConversationResponse(BaseModel):
    id: uuid.UUID
    user_id: Optional[str] = None
    started_at: datetime
    last_activity_at: datetime

    class Config:
        from_attributes = True # Enable ORM mode for Pydantic (V2)

class ChatMessageBase(BaseModel):
    query: str
    response: str
    model_used: str
    selected_text: Optional[str] = None
    page_context: Optional[str] = None
    feedback: Optional[int] = Field(None, ge=1, le=5)

class ChatMessageResponse(ChatMessageBase):
    id: uuid.UUID
    conversation_id: uuid.UUID
    timestamp: datetime
    relevant_chunks: Optional[List[uuid.UUID]] = None

    class Config:
        from_attributes = True # Enable ORM mode for Pydantic (V2)

class ChatMessageCreate(BaseModel):
    query: str
    conversation_id: Optional[uuid.UUID] = None
    selected_text: Optional[str] = None
    page_context: Optional[str] = None
