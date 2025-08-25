// Un composant réutilisable qui affiche un produit
export default function ProductCard({ product }) {
  return (
    <div className="border p-3 rounded-md shadow-md">
      <h2 className="font-bold">{product.name}</h2>
      <p>Prix : {product.price} $</p>
      <button className="bg-blue-500 text-white px-2 py-1 rounded">
        Ajouter au panier
      </button>
    </div>
  );
}
