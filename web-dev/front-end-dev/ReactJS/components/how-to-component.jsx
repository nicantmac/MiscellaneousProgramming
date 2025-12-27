// Define a functional component named Homepage
function Homepage() { 
  return ( 
    // The component returns a single parent <div> to group the content
    <div> 
      {/* Renders a primary heading for the page */}
      <h1>Welcome Home</h1> 
      
      {/* Renders a paragraph containing the subtitle/description */}
      <p>Welcome to the landing Home Screen</p> 
    </div> 
  ); 
} 

// Export the component so it can be imported and used in other files (like App.js)
export default Homepage;
