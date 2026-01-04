import { useState } from "react";

function ConditionalRender() {
  const [isLoading, setIsLoading] = useState(false);
  const [hasError, setHasError] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // 1️⃣ Loading state (highest priority)
  if (isLoading) {
    return (
      <div style={{ padding: "2rem" }}>
        <h1>Loading...</h1>
        <button onClick={() => setIsLoading(false)}>
          Stop Loading
        </button>
      </div>
    );
  }

  // 2️⃣ Error state
  if (hasError) {
    return (
      <div style={{ padding: "2rem" }}>
        <h1>Something went wrong ❌</h1>
        <button onClick={() => setHasError(false)}>
          Clear Error
        </button>
      </div>
    );
  }

  // 3️⃣ Auth state
  if (!isLoggedIn) {
    return (
      <div style={{ padding: "2rem" }}>
        <h1>Please log in</h1>
        <button onClick={() => setIsLoggedIn(true)}>
          Log In
        </button>
      </div>
    );
  }

  // 4️⃣ Default render (success state)
  return (
    <div style={{ padding: "2rem" }}>
      <h1>Welcome back 🎉</h1>
      <button onClick={() => setIsLoggedIn(false)}>
        Log Out
      </button>
      <button onClick={() => setIsLoading(true)}>
        Trigger Loading
      </button>
      <button onClick={() => setHasError(true)}>
        Trigger Error
      </button>
    </div>
  );
}

export default ConditionalRender;
