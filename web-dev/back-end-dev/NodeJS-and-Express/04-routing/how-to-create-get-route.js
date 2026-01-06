/**
 * HOW TO CREATE A GET ROUTE IN EXPRESS
 *
 * A GET route responds when the browser or client
 * makes a GET request to a specific URL.
 */

const express = require("express");
const app = express();

/**
 * This route runs ONLY when someone visits:
 * http://localhost:3000/hello
 */
app.get("/hello", (req, res) => {
  res.send("Hello from Express");
});

/**
 * Start the server
 */
app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
