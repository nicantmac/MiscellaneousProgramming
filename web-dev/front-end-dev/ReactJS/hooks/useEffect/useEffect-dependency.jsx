// import the 'useEffect' & 'useState' hook from the react library to manage the local component state
import { useEffect, useState } from "react";

// component to display data
export default function UseEffectDependency() {
  // count stores count, setCount will change count data, useState initializes count at 0
  const [count, setCount] = useState(0);

  // useEffect will mount off first render and always update if count data ever changes
  useEffect(() => {
    console.log("Count changed:", count);
  }, [count]);

  return (
    // based onClick, the setCount will add 1 to count state
    <button onClick={() => setCount(prevCount => prevCount + 1)}>
      Count: {count} {/* here will display count data */}
    </button>
  );
}
