// child component: 
function ProductCard({ name, price, category, discount = 0 }) {
  
  // Logic block: Calculate final price before returning UI
  const finalPrice = price - discount;

  return (
    <div>
      {/* We can use the variables directly without typing 'props.' */}
      <span>{category}</span>
      <h2>{name}</h2>
      
      <div>
        {discount > 0 ? (
          <p>${finalPrice} <span>${price}</span></p>
        ) : (
          <p>${price}</p>
        )}
      </div>
    </div>
  );
}

// parent component
export default function ShopPage() {
  return (
    <main> {/* main wrapper */}
      <h1>Store Front</h1> {/* regular header text */}
      
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
