

import styles from './css/ChatMessage.module.css';
import robotImg from '../assets/robot.png';
import userImg from '../assets/user.png';

export function ChatMessage({sender, message})
{
    return(
        <div>
            {sender === "robot" &&(<img className={styles.robotImage} src={robotImg} alt="Robot"/>)}
            {message}
            {sender === "user" && (<img className={styles.userImage} src={userImg}  alt="User"/>)}
        </div>
    );
}