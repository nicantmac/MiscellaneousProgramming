import { useEffect, useState } from "react";

export default function FetchExample() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
      const json = await res.json();
      setData(json);
      setLoading(false);
    }

    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
