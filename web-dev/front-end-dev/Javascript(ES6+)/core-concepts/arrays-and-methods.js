// Here let's understand the methods most used on arrays in JS

let cards = ["Knight", "Archer", "Giant"]; // Initiate array to manipulate

// Simply start with accessing indices
console.log(cards[0]); // Output: "Knight"


/* - To add new elements to the array, utilize .push() method
   - type the element inside the parens  */
cards.push("Wizard");
console.log(cards); // Output: "Knight", "Archer", "Giant", "Wizard"


/* - To remove an element from an array, utilize the .pop() method
   - It removes and returns the last index  */
newCards = ["sparky", "lumberjack", "valkyrie", "minions"]
newCards.pop();
console.log(newCards); // Output: "sparky", "lumberjack", "valkyrie"


/* - Instead of formal looping, JS allows forEach method to loop
   - In the parens, card = each value stored
   - using arrow, we perform an action on each index  */
cards.forEach(card => console.log("Card:", card)); // Output: "Knight", "Archer", "Giant", "Wizard"


/* - To find an item in an array, utilize .find() method
   - If it does find a matching item, it returns the first match
   - If it doesn’t find anything, it returns: undefined  */
const found = cards.find(card => card === "Archer");
if (found) {
  console.log("Found:", found); // Output: "Archer"
} else {
  console.log("Found:", found); // Output: undefined
}


/* - To check if array includes an item, utilize the .includes() method 
   - It returns true or false depending if a string or an array contains a specified value  */
console.log(cards.includes("Giant")); // true
console.log(cards.includes("Fireball")); // false


/* Let's create a new array with changed values (non-destructive)
   - Using .map(), return new array of elements
   - for each index we return the Upper case of each element  */
const upperCards = cards.map(card => card.toUpperCase());
console.log("Mapped:", upperCards); // Output: Mapped: ["KNIGHT", "ARCHER", "GIANT", "WIZARD"]


/* To filter an array based on a condition, utilize the .filter() method 
   - Out of this newer array, let's print the short names
   - Inside .filter(), let's perform an action on each card in the array 
   - if the length of each index is <= 6, we want to display it  */
let bestCards = ["Balloon", "Electro Wizard", "Miner", "Giant", "Prince", "Arrows", "Firecracker"]
const shortNames = bestCards.filter(card => card.length <= 6);
console.log("Filtered:", shortNames); // Output: ["Miner", "Giant", "Prince", "Arrows"]


/* To reduce to a single value, utilize the .reduce() method i.e. the total of something
   - .reduce() does the following: Add up numbers, Count characters, Build a new string, Combine objects, Flatten arrays
   - (sum, card) = sum: will be the accumulator (starting at 0), card (the current index in array)
   - sum + currentCard.length, 0) = sum (starting at 0) + the numerical length of each index  */
let addCards = ["Zap", "Log", "Giant"] 
const totalChars = addCards.reduce((sum, currentCard) => sum + currentCard.length, 0);
// addCards[0] = 3 chars, addCards[1] = 3 chars, addCards[2] = 5 chars; 3 + 3 + 5 = 11
console.log("Total characters:", totalChars); // Output: Total characters: 11


// To sort an array alphabetically, utilize the .sort() method
const sorted = [...cards].sort();
console.log("Sorted:", sorted); // ["Archer", "Giant", "Knight"]


// 🔁 Reverse order
const reversed = [...cards].reverse();
console.log("Reversed:", reversed); // ["Giant", "Archer", "Knight"]


// 🎯 Slice (non-destructive)
const firstTwo = cards.slice(0, 2);
console.log("Sliced:", firstTwo); // ["Knight", "Archer"]


// 💥 Splice (modifies original array)
cards.splice(1, 1, "Hunter");
console.log("Spliced:", cards); // ["Knight", "Hunter", "Giant"]


// 🧩 Join elements into a string
console.log("Joined:", cards.join(", ")); // "Knight, Hunter, Giant"
