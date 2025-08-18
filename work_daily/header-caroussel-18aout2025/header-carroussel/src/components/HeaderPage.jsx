import { useState } from "react";
import './headerpage.css'

export function HeaderPage()
{
    const [isMenuOpen, setIsMenuOpen] = useState(false)

    const handleMenuClick = ()=> setIsMenuOpen(!isMenuOpen)
    const handleLinkMenu = ()=> setIsMenuOpen(false)

    return(
        <>
        {/* Overlay noir transparent quand le menu mobile est ouvert */}
        {isMenuOpen && <div className="menu-overlay" onClick={handleMenuClick}></div>}
        <div className="header">
            <div className="left-section">
                <ul>
                    <li><a href="#">Quisqueya</a></li>
                </ul>
            </div>

            <div className={`middle-section${isMenuOpen? " show-menu": ""}`}>
                {/* Ligne du haut : logo à gauche, X à droite */}
                <div className="menu-header-row">
                    <div className="menu-logo"></div>
                    <button className="close-menu" onClick={handleMenuClick} style={{display: isMenuOpen ? 'block' : 'none'}}>✕</button>
                </div>
                <ul>
                    <li><a href="#" onClick={handleLinkMenu}>Accueil</a></li>
                    <li><a href="#" onClick={handleLinkMenu}>Qui sommes-nous</a></li>
                    <li><a href="#" onClick={handleLinkMenu}>Mission</a></li>
                    <li><a href="#" onClick={handleLinkMenu}>Contact</a></li>
                    <li><a href="#" onClick={handleLinkMenu}>Connexion</a></li>
                </ul>
                {/* Bouton Deconnexion visible uniquement sur mobile, sous Connexion */}
                <button className="deconnexion mobile-only"><a>Deconnexion</a></button>
            </div>

            <div className="right-section">
                <ul>
                    {/* Bouton Deconnexion affiché seulement sur desktop */}
                    <button className="deconnexion desktop-only"><a>Deconnexion</a></button>
                    <li className="menu-icon" onClick={handleMenuClick}>
                        {isMenuOpen? '✕' : '☰'}
                    </li>
                </ul>
            </div>
        </div>
        </>
    );
}