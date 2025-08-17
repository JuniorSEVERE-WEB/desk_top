import { useState } from 'react';
import './headerpage.css';

export function HeaderPage() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const handleMenuClick = () => setIsMenuOpen(!isMenuOpen);
  const handleLinkClick = () => setIsMenuOpen(false);

  return (
    <header className="header">
      <div className="left-section">
        <span className="logo">Quisqueya</span>
      </div>
      <nav className={`middle-section${isMenuOpen ? ' show-menu' : ''}`}>
        <ul>
          <li><a href="#" onClick={handleLinkClick}>Acceuil</a></li>
          <li><a href="#" onClick={handleLinkClick}>Qui sommes nous</a></li>
          <li><a href="#" onClick={handleLinkClick}>Mission</a></li>
          <li><a href="#" onClick={handleLinkClick}>Contact</a></li>
          <li><a href="#" onClick={handleLinkClick}>Connexion</a></li>
          <li><a href="#" onClick={handleLinkClick}>Deconnexion</a></li>
        </ul>
      </nav>
      <div className="right-section">
        <span className="username">Hello Junior</span>
        <img className="profil-username" src="https://randomuser.me/api/portraits/men/1.jpg" alt="Profil" />
        <div className="menu-icon" onClick={handleMenuClick}>
          {isMenuOpen ? '✕' : '☰'}
        </div>
      </div>
    </header>
  );
}
