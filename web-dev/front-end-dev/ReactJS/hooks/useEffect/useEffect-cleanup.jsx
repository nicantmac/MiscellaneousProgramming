// import the 'useEffect' & 'useState' hook from the react library to manage the local component state
import { useEffect, useState } from "react";

// component to display data
export default function Timer() {
  // time stores time value, setTime will change time, useState initializes time at 0
  const [time, setTime] = useState(0);

  // right when react renders, useEffect will start an interval by (1000ms or 1sec) that adds 1 to time state
  useEffect(() => {
    const id = setInterval(() => {
      setTime(t => t + 1);
    }, 1000);

    /* If the user navigates to a different page and this component is removed from the UI, the browser's 
       setInterval will not stop automatically. It will keep running in the background, trying to update a 
       state that no longer exists (a "memory leak").  */
    return () => clearInterval(id);
  }, []); // empty array: so setup once on mount, cleanup once on unmount

  return 
    (
      <main>
        <h1>This is the current time!</h1>
        <p>Timer: {time}</p> {/* here we show the time data */}
      </main>
    );
}
