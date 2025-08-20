
import { useEffect, useState } from 'react';
import { HeaderPage } from '../components/HeaderPage';
import './homepage.css'
import { FooterPage } from '../components/FooterPage';


const slides = [
    {
    image: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80',
    text: 'Bienvenue à Quisqueya!'
  },
  {
    image: 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80',
    text: 'Découvrez nos programmes éducatifs.'
  },
  {
    image: 'https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=800&q=80',
    text: 'Rejoignez une communauté dynamique.'
  }
];
export function HomePage()
{
    const [current, setCurrent] = useState(0);

    useEffect(()=>{
        const timer = setInterval(()=>setCurrent(c=> (c + 1) % slides.length), 4000);
        return () => clearInterval(timer);
    }, [])

    const prev = ()=> setCurrent(c => (c - 1 + slides.length) % slides.length);
    const next = ()=> setCurrent(c => (c + 1 ) % slides.length);

    return(
        <>
        <HeaderPage />
        

            <div className="carroussel">
                <div className="carroussel-img" style={{ backgroundImage: `url(${slides[current].image})` }}>
                    <div className="carroussel-text">{slides[current].text}</div>
                    <button className="carroussel-btn prev" onClick={prev}>&lt;</button>
                    <button className="carroussel-btn next" onClick={next}>&gt;</button>
                </div>
            </div>

            

           


        <FooterPage />
        </>
    );
}