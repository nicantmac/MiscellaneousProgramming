
import { useEffect, useState } from "react";

// component that will display user fetched data
export default function FetchExample() {
  // data: data from user will be stored, setData: data retrieves data, useState initializes to null
  const [data, setData] = useState(null);
  // loading stores loading state, setLoading will change loading state, useState initializes at true
  const [loading, setLoading] = useState(true);

  // useEffect handles fetching user data on first mounts
  useEffect(() => {
    /* define an async function handles operations that take time, 
       such as making network requests (i.e. fetching data from an API) */
    const fetchData = async () => {
      try {
        // res: use fetch() for raw response from server, await pauses execution until the request completes
        const res = await fetch("jsonplaceholder.typicode.com");
        
        // json: using .json() parses data & converts the raw response into a usable JavaScript object
        const json = await res.json();
        
        setData(json); // setData: update the state with the user data
      } catch (error) {
         // catch handles failures to retrieve user data
        console.error("Caught error:", error);
      } finally {
        setLoading(false); // finally: ALWAYS end loading whether success or fail
      }
    };
            
    // call that function to execute
    fetchData();
  }, []); // Empty dependency array ensures this only runs once on mount

  // 'loading...' renders when state is true 
  if (loading) return <p>Loading...</p>;

  // JSON.stringify converts a JavaScript object into a string
  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
