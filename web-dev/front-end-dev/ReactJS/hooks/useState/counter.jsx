import { useState } from "react";

// component to display button count
export default function BasicCounter() {
  // count holds the data, setCount will change data, useState keyword will initiate the value
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p> {/* here display count */}

      {/* both btns use 'setCount' as a function to update count */}
      <button onClick={() => setCount(c => c + 1)}>+</button>
      <button onClick={() => setCount(c => c - 1)}>-</button>
    </div>
  );
}
