import { useEffect, useState } from "react";
import axios from "axios";
import ProductCard from "../components/ProductCard";

export default function HomePage() {
  const [products, setProducts] = useState([]);

  // Charger les produits depuis l’API
  useEffect(()=>{
      axios.get("http://localhost:3002/products")
           .then(response => {
            setProducts(response.data); // mettre a jour le state
           })
           .catch(error => {
            console.error("Erreur lors du fetch:", error)
           });
  },[]);
 

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Catalogue Produits</h1>
      <div className="grid grid-cols-2 gap-4">
        {products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}
