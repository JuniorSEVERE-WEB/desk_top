import {  useEffect, useRef } from 'react';
import { ChatMessage } from "./ChatMessage";

export function ChatMessages2({ chatMessages })
{
  const chatMessagesRef = useRef(null);

  useEffect(()=>{
    const containerElm = chatMessagesRef.current;
    if(containerElm)
    {
      containerElm.scrollTop = containerElm.scrollHeight;
    }
  }, [chatMessages]);

    return(
        <div className="chat-messages" ref={chatMessagesRef}>
          {chatMessages.map((chatMessage)=>{
               return(
                <ChatMessage 
                  message ={chatMessage.message}
                  sender = {chatMessage.sender}
                  key = {chatMessage.id}/>
               );
          })}
        </div>
    );
}