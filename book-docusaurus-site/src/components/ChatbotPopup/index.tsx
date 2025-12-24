import React, { useState } from 'react';
import styles from './styles.module.css';

function ChatbotPopup() {
  const [isOpen, setIsOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  const sendMessage = async () => {
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setResponse(data.response);
      setMessage(''); // Clear message after sending
    } catch (error) {
      console.error('Error sending message:', error);
      setResponse('Error: Could not connect to the chatbot.');
    }
  };

  return (
    <>
      <button className={styles.chatButton} onClick={togglePopup}>
        Chat
      </button>

      {isOpen && (
        <div className={styles.popupOverlay}>
          <div className={styles.popupContent}>
            <div className={styles.popupHeader}>
              <h2>Chatbot</h2>
              <button className={styles.closeButton} onClick={togglePopup}>
                &times;
              </button>
            </div>
            <div className={styles.popupBody}>
              <div className={styles.chatWindow}>
                {response && <div className={styles.chatMessage}>Bot: {response}</div>}
              </div>
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    sendMessage();
                  }
                }}
                className={styles.chatInput}
                placeholder="Type your message..."
              />
              <button onClick={sendMessage} className={styles.sendButton}>
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default ChatbotPopup;
