
import { useEffect } from "react";

export default function UseEffectBasic() {
  useEffect(() => {
    console.log("Component mounted");

    return () => {
      console.log("Component unmounted");
    };
  }, []);

  return <p>Check the console 👀</p>;
}
