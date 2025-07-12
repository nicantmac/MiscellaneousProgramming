import React, { useState } from 'react';

function modifyElement() {
  const [count, setCount] = useState(0)

  function() { (count) => setCount(count + 1); }
  
  return(
    <div className="page-container">
      <div>
        <h1>Current Counter</h1>
        <button onClick={countUp}>Click Me!</button>
        <p>`The current count: ${count}`</p>
      </div>
    </div>
  );
}
export default modifyElement;
