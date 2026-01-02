/* quick note: useRef() returns an object that looks like this -> { current: initialValue } 
   use dot notation (i.e. myRef.current) to access and modify this value  */

import { useRef, useEffect } from 'react';

// component displays data
function Counter() {
  // clickCount: stores cureent value, useRef() initializes value at 0
  const clickCount = useRef(0);

  // handleClick invokes onclick & adds 1 to current value
  const handleClick = () => {
    clickCount.current += 1; // access & add 1 to current value
    console.log('Button clicked', clickCount.current, 'times'); // log current value
  };

  return ( 
    <div>
      <h1>Button Counter Page</h1>
      <button onClick={handleClick}>Open console & click btn</button>
    </div>
  );
}
