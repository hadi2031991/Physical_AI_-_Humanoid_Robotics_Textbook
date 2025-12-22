import React from 'react';
import Layout from '@theme/Layout';
import Chatbot from '../components/Chatbot';

export default function ChatbotPage() {
  return (
    <Layout title="Chatbot" description="A RAG-powered chatbot">
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          padding: '2rem',
        }}
      >
        <h1>RAG Chatbot</h1>
        <p>This is an interactive chatbot powered by a Retrieval-Augmented Generation backend.</p>
        <Chatbot />
      </div>
    </Layout>
  );
}
