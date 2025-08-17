import { useState } from "react";
import './headerpage.css';

export function HeaderPage()
{
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const handleMenuClick = ()=> setIsMenuOpen(!isMenuOpen);
    const handleLinkClick = ()=> setIsMenuOpen(false);

    return(
        <>
          <div className="header">
            <div className="left-section">
                <p>Quisqueya</p>
            </div>

            <div className={`middle-section${isMenuOpen? " show-menu": ""}`}>
                <ul>
                    <li><a href="#" onClick={handleLinkClick}>Acceuil</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Qui sommes nous</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Mission</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Contact</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Connexion</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Deconnexion</a></li>
                </ul>
            </div>


            <div className="right-section">
                    <div className="menu-icon" onClick={handleMenuClick}>
                        {isMenuOpen?'✕' : '☰'}
                    </div>
            </div>
          </div>
        </>
    );
}