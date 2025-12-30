/* Helper Notes:
   - 'useEffect' runs after the browser render, there is a tiny "gap" (usually a few milliseconds).
   i.e. if you use useEffect to change a background color from Red to Blue, the user will see Red 
   for a split second before it flashes to Blue. This is why we say useEffect is non-blocking it waits 
   for the user to see the content before doing its work so the app feels fast.
*/

// import the 'useEffect' hook from the react library to manage actions that happen outside the standard rendering logic
import { useEffect } from "react";

// component to display data
export default function UseEffectBasic() {
 
  // useEffect handles actions after the UI is visible to the user
  useEffect(() => {
    console.log("Component mounted"); // when rendered, we quickly console.log 'Component mounted'

    // the return function in useEffect is the 'cleanup function'
    return () => {
      console.log("Component unmounted"); // here we clean up by logging 'Unmounted'
    };
  }, []); // runs ONCE after the initial render via the empty dependency array

  return <p>Check the console!</p>;
}
