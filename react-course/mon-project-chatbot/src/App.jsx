import { ChatMessage } from './components/ChatMessage'
import { ChatInput } from './components/ChatInput'
import './App.module.css'



function App() {
  return (
    <>
      
      <ChatInput />
      <ChatMessage message="Hello Mr chatbot" sender="user"/>
      <ChatMessage message="Hello dear user" sender="robot"/>
      
    </>
  );
}

export default App
