
import './HomePage.css';
import { useEffect, useState } from 'react';

const slides = [
  {
    title: "Welcome to Quisqueya",
    description: "Your one-stop solution for all your needs.",
    image: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80"
  },
  {
    title: "Our Services",
    description: "We offer a wide range of services to cater to your needs.",
    image: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80"
  },
  {
    title: "Contact Us",
    description: "Get in touch with us for any inquiries.",
    image: "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=800&q=80"
  },
  {
    title: "About Us",
    description: "Learn more about our company and values.",
    image: "https://images.unsplash.com/photo-1503676382389-4809596d5290?auto=format&fit=crop&w=800&q=80"
  }
];

export function HomePage() {
  const [current, setCurrent] = useState(0);

  useEffect(()=>{
    const timer = setInterval(() => setCurrent(c => (c + 1) % slides.length), 4000);
    return ()=> clearInterval(timer);
  },[])



  return (
    

    <>
      <div className="home-container">
        <div className="carroussel">
          <div className="carroussel-img" style={{ backgroundImage: `url('${slides[current].image}')`}}>
            <div className="carroussel-text">
              <h2 style={{color:'#fff', textShadow:'0 2px 8px #000'}}>{slides[current].title}</h2>
              <p style={{color:'#fff', textShadow:'0 2px 8px #000'}}>{slides[current].description}</p>
            </div>
          </div>
        </div>
        <div className="carroussel-images-text">
          <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem ipsam dolore saepe asperiores dolorem voluptatem non, eum labore enim suscipit laudantium ipsa id dolores adipisci aspernatur sapiente corrupti debitis dolorum!</div>
          <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odio asperiores sed commodi nulla aperiam aut eius doloremque id, nostrum enim sint quia sapiente iure alias eligendi, necessitatibus praesentium illum? Nesciunt.</div>
         
        </div>
      </div>
    </>
  );
}

