// import useNavigate hook to programmatically change routes inside your application
import { useNavigate } from "react-router-dom";

// component for displaying data
function Home() {
  // to use navigate hook, store the function into variable
  const navigate = useNavigate();

  return (
    // onClick -> btn invokes function that calls navigate hook to dashboard
    <button onClick={() => navigate("/dashboard")}>
      Go to Dashboard
    </button>
  );
}

export default Home;
