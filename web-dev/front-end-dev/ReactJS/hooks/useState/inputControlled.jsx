import { useState } from "react";

// component will display data
export default function InputControlled() {
  // value stores data, setValue will modify data, useState initialized with empty str
  const [value, setValue] = useState("");

  return (
    // input will be used to change state of whats typed
    <input
      value={value} {/* the input will always show exactly whats stored in the state */}
      placeholder="Type here..." {/* shows "Type here..." when the input is empty */}

      {/* onchange is an event listener that triggers every time the user types. It updates the state with the current string typed */}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}
