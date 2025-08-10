import { ChatMessages2 } from './components/ChatMessages2'

import { ChatInput } from './components/ChatInput'
import { useState } from 'react'
import styles from './App.module.css'



function App() {
  const [chatMessages, setChatMessages] = useState([
    {
      message: "Hello dear Chatbot",
      sender: "user",
      id: "id1"
    },
    {
      message: "Hello dear User",
      sender: "robot",
      id: "id2"
    }
  ])
  
  return (
    <div className={styles.chatContainer}>
      <ChatMessages2 chatMessages={chatMessages} />
      <ChatInput chatMessages={chatMessages} setChatMessages={setChatMessages} />
    </div>
  );
}

export default App
