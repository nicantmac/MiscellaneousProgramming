import React from 'react';
import { useState } from 'react';

// Our functional component called: App
function App() {

    // Let's use a React hooks: useState, to keep track of: cat data
    const [catData, setCatData] = useState(null);

    // Let's create a function to get the cat data from API link
    // Async & await will return cat data when ready
    async function getData() {
        try {
            // Reminder: await can only be used inside an async function
            const response = await fetch("https://api.thecatapi.com/v1/images/search");

            // JavaScript Object Notation: easy to read, write, and simple to parse
            const data = await response.json(); // stores random cat data every request

            // because it's in list format, always retrieve it like its list item
            setCatData(data[0])
        } catch (error) {
            console.log('Error fetching:', error);
            // An alternative: console.error(), it helps differentiate errors from regular logs.
        }
    }

    return(
      <div>
          <h1 style={{
              /* this is just inline styling for our page title */
              textAlign: 'center',
              textAlignVertical: 'center',
              justifyContent: 'center',
              border: '2px dotted black'
          }}>The Vin Data</h1>

          <div>
              {/* this button when clicked, will activate getData() */}
              <button onClick={getData}>Click Me</button>

              {/* let's conditionally render the data if true */}
              {catData && (
                  <div>
                      {/* when catData is true, we display: img, url, img height & width */}
                      <img src={catData.url} alt="Cat Picture"/>
                      <p>Cat Data: {catData.url}</p>
                      <p>Cat Img Height: {catData.width}</p>
                      <p>Cat Img Width: {catData.height}</p>
                  </div>
              )}
          </div>
      </div>
    );
}

export default App;
