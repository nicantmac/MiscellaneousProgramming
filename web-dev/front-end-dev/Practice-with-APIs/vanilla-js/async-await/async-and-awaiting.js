// async ensures the function always returns a Promise
async function fetchData() {
  // because retriveing data can fail, we throw desired code in a try block
  try {
    // await the response from the fetch call
    let response = await fetch('https://api.example.com/data');
    // await the JSON parsing of the response
    let data = await response.json();
    console.log(data); // now resolved data is available, we can log it
  } catch (error) {
    // if failed, we handle any errors that occurred during the fetch or parsing
    console.error('Error fetching data:', error); // .error() is better than .log() for logging errors
  }
}

// call the async function
fetchData();
