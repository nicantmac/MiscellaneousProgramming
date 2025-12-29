// import the 'useState' hook from the react library to manage local component state
import { useState } from 'react';

function modifyElement() {
  /* format: 'count' -> stores the state, 
             'setCount' -> is used to modify the state,
             'useState' -> sets the initial value stored */
  const [count, setCount] = useState(0);

  const countUp = () => { 
    // use the modifier 'setCount' to increment the state by 1
    /* note: its good practice to use previous state and render the next desired state when 
       updating so React doesn't mess up focusing on the actual live count, incase user clicks too fast */
    setCount(prevCount => prevCount + 1); 
  };
  
  return(
    <main className="page-container">
      <h1>Current Counter</h1>
      <button onClick={countUp}>Click Me!</button>  {/* countUp function will execute onClick event */}
      <p>{`The current count: ${count}`}</p>  {/* to track we use a template literal to display state */}
    </main>
  );
}

export default modifyElement;
