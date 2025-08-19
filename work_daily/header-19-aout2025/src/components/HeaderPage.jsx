import './headerpage.css'
import { useState } from 'react';
export function HeaderPage()
{
    const [isMenuOpen, setIsMenuOpen] = useState(false);
   const handleMenuClick = () => setIsMenuOpen(!isMenuOpen);
   const handleLinkClick = () => setIsMenuOpen(false)


    return(
        <>
           {isMenuOpen && <div className="menu-overlay" onClick={handleMenuClick}></div>}
          <div className="header">
            <div className="left-section">
                <a href="#">
                    <ul>
                        <li><img src="/logo-19-aout.png" alt="Logo" /></li>
                        <li><span>CCM</span></li>
                    </ul>
                </a>
            </div>
            <div className={`middle-section${isMenuOpen ? " show-menu" : ""}`}>
                {/* menu-header-row supprimé : logo et close-menu */}
                <div className="menu-header-row">
                    <div className="menu-logo">
                        <img src="/logo-19-aout.png" alt="Logo" />
                    </div>
                    <button className="close-menu" onClick={handleMenuClick} style={{display: isMenuOpen ? 'block' : 'none'}}>✕</button>
                </div>
                <ul>
                    <li><a href="#" onClick={handleLinkClick}>Acceuil</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Qui sommes-nous</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Mission</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Contact</a></li>
                    <li><a href="#" onClick={handleLinkClick}>Connexion</a></li>
                </ul>
                <button className="deconnexion mobile-only"><a href="#" onClick={handleLinkClick}>Deconnexion</a></button>
            </div>
            <div className="right-section">
                <ul>
                    <button><a href="">Deconnexion</a></button>
                    <li className="menu-icon" onClick={handleMenuClick}>
                         {isMenuOpen? '✕' : '☰'}
                    </li>
                </ul>
            </div>
          </div>
        </>
    );
}