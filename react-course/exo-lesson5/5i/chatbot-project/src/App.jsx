import { useState } from 'react'
import { ChatInput } from './components/ChatInput';
import ChatMessages from './components/ChatMessages';
import './App.css'

function App() {
  const [chatMessages, setChatMessages] = useState([{
    message: 'hello chatbot',
    sender: 'user',
    id: 'id1',
    time: 1736127288920
  }, {
    message: 'Hello! How can I help you?',
    sender: 'robot',
    id: 'id2',
    time: 1736127288921
  }, {
    message: 'can you get me todays date?',
    sender: 'user',
    id: 'id3',
    time: 1736127288922
  }, {
    message: 'Today is September 27',
    sender: 'robot',
    id: 'id4',
    time: 1736127288923
  }]);

  return (
    <div className="app-container">
      <ChatMessages chatMessages={chatMessages} />
      <ChatInput 
        chatMessages={chatMessages}
        setChatMessages={setChatMessages}
      />
    </div>
  );
}

export default App
