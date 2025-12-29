import { useState } from "react";

// component to display the btn state
export default function ToggleBoolean() {
 // isOn stores state, setIsOn is used to change the state, useState keyword used to initiate data
  const [isOn, setIsOn] = useState(false);

  return (
    // when btn clicked, setIsOn changes to opposite state
    <button onClick={() => setIsOn(prev => !prev)}>
      {isOn ? "ON" : "OFF"} {/* text is based isOn, if true 'ON' if not 'OFF' */}
    </button>
  );
}
