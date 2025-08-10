import { useState } from 'react'
import supersimpledev from 'supersimpledev';
import styles from './css/ChatInput.module.css'
export function ChatInput({chatMessages, setChatMessages})
{
  const [inputText, setInputText] = useState("")

  function saveInputText(event)
  {
    setInputText(event.target.value)
  }
  function escEnter(event)
  {
    if(event.key === "Enter")
    {
      sendMessage()
    }
    else if(event.key === "Escape")
    {
      setInputText("")
    }
  }

  async function sendMessage()
  {
    const newChatMessages = [
      ...chatMessages,
      {
        message: inputText,
        sender: "user",
        id: crypto.randomUUID()
      }
    ];
    setChatMessages(newChatMessages);
    setChatMessages([
      ...newChatMessages,
      {
        message:"Loading...",
        sender:"robot",
        id:crypto.randomUUID()
      }

      
      ])
        const response = await supersimpledev.chatbot.getResponseAsync(inputText);
      console.log(response);
      
      setChatMessages([
        ...newChatMessages,
        {
          message: response,
          sender: "robot",
          id: crypto.randomUUID()
        }
    ]);
    setInputText("");
    
  }
  return(
    <div className={styles.chatInputBar}>
          <input 
           className={styles.chatInput}
           placeholder="Ask me your question"
           value = {inputText}
           onKeyDown={escEnter}
           onChange={saveInputText}/>
          <button 
       onClick={sendMessage}
       className={styles.sendButton}>Send message</button>
        </div>
    );
}