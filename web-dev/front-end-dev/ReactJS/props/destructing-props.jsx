// child component: 
function ProductCard({ name, price, category, discount = 0 }) {
  
  // Logic block: Calculate final price before returning UI
  const finalPrice = price - discount;

  return (
    <div className="p-4 border rounded-lg shadow-sm">
      {/* We can use the variables directly without typing 'props.' */}
      <span className="text-xs font-bold uppercase text-blue-500">{category}</span>
      <h2 className="text-xl font-semibold">{name}</h2>
      
      <div className="mt-2">
        {discount > 0 ? (
          <p className="text-green-600 font-bold">${finalPrice} <span className="line-through text-gray-400 text-sm">${price}</span></p>
        ) : (
          <p className="text-gray-900 font-bold">${price}</p>
        )}
      </div>
    </div>
  );
}

// parent component
export default function ShopPage() {
  return (
    <main className="p-10 space-y-4"> {/* main wrapper */}
      <h1 className="text-3xl font-bold">Store Front</h1> {/* regular header text */}
      
      {/* create child compnt's & passed manual data via prop names that the child will destructure */}
      {/* Put nums, arrys & bools in curly brack's, strings don't need curly brack's */}
      <ProductCard 
        name="Mechanical Keyboard" 
        price={120} 
        category="Electronics" 
        discount={20} 
      />

      <ProductCard 
        name="Coffee Mug" 
        price={15} 
        category="Home Decor" 
        // side note: no 'discount' prop is passed here, so it will use the default from child
      />
    </main>
  );
}
