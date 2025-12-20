import { useState } from 'react';

function UserLoader() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  // The async logic lives in a plain function
  const handleLoadUser = async () => {
    setLoading(true); // 1. initiate the loading status

    try {
      // here we retrieve user data via fetch() & json()
      const response = await fetch('https://api.example.com/user');
      const data = await response.json();
      setUser(data); // 2. Set data
    } catch (error) {
      // if getting data fails, let's catch the error to avoid crashing  
      console.error("Failed to fetch:", error);
    } finally {
      // 3. End loading state because (success or fail) has rendered
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={handleLoadUser} disabled={loading}>
        {loading ? 'Loading...' : 'User Profile'}
      </button>

      {user && <div>Welcome, {user.name}!</div>}
    </div>
  );
}
