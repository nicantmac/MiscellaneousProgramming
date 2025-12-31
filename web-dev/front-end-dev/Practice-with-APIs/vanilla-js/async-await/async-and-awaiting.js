async function fetchData() {
  try {
    // Await the response from the fetch call
    let response = await fetch('https://api.example.com/data');
    // Await the JSON parsing of the response body
    let data = await response.json();
    
    console.log(data); // The resolved data is now available
  } catch (error) {
    // Handle any errors that occurred during the fetch or parsing
    console.error('Error fetching data:', error);
  }
}

// Call the async function
fetchData();
