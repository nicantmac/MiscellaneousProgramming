// We define functional components by typing 'export default' before function keyword
// 'export default' allows us to reuse elsewhere
function Homepage() { 

  function handleClick = () => {
      alert("You clicked the button!"); // showing alert when user clicks!
  }

  // return blocks primary job is telling React what the user interface structure should look like
  return ( 
    <main> 
      <h1>Welcome Home</h1> {/* regular heading */}
      <p>Welcome to the landing Home Page</p> {/* regular text */}
      
      <button type="button onClick={handleClick}>Click Me!</button>
    </main> 
  ); 
} 

// 'export default' let's us use this somewhere else
export default Homepage;
