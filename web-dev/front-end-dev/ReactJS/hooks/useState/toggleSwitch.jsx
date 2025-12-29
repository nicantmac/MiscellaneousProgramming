import { useState } from "react";

export default function ToggleBoolean() {
  const [isOn, setIsOn] = useState(false);

  return (
    <button onClick={() => setIsOn(prev => !prev)}>
      {isOn ? "ON" : "OFF"}
    </button>
  );
}
