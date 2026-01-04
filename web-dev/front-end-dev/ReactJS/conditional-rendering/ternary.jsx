import { useState } from "react";

function TernaryRender() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Ternary Rendering Examples</h1>

      {/* Auth-based ternary */}
      <section>
        <h2>Auth Render</h2>
        {isLoggedIn ? (
          <p>Welcome back, user!</p>
        ) : (
          <p>Please log in.</p>
        )}

        <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
          Toggle Login
        </button>
      </section>

      <hr />

      {/* Loading ternary */}
      <section>
        <h2>Loading Render</h2>
        {isLoading ? <p>Loading...</p> : <p>Data loaded!</p>}

        <button onClick={() => setIsLoading(!isLoading)}>
          Toggle Loading
        </button>
      </section>

      <hr />

      {/* Count-based ternary */}
      <section>
        <h2>Count Render</h2>
        {count === 0 ? (
          <p>No items yet</p>
        ) : (
          <p>You have {count} item(s)</p>
        )}

        <button onClick={() => setCount(count + 1)}>
          Add Item
        </button>
      </section>
    </div>
  );
}

export default TernaryRender;
