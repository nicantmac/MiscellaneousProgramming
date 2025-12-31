// import useNavigate hook to programmatically change routes inside your application
import { useNavigate } from "react-router-dom";

// component to display data
function Login() {
  /* navigate stores an imperative function (specifically a NavigateFunction). When you call useNavigate(), it returns 
     this function, which allows you to change the browser's URL and navigate programmatically within your code */
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault(); // prevent the browser from 
    // login logic here
    navigate("/dashboard");
  }

  return (
    // onSubmit we invoke handleSubmit
    <form onSubmit={handleSubmit}>
      <button type="submit">Login</button>
    </form>
  );
}
