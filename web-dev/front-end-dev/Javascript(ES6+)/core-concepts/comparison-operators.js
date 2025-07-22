// Here we will understand how JavaScript does comparisons

let a = 5; // Initiate a number
let b = "5"; // Initiate a string

/* - (==) => loose equality: compares values stored after type coercion
   - In JavaScript, numbers holds hierarchy, type coercion converts the string 5 into a number to match 5  */
console.log(a == b); // Type Coercion: 5 == 5, Output: true

/* - (===) => strict equality: compares values stored AND data types
   - In JavaScript, strict comparison is three characters length (i.e. checks if boolean and true)  */
console.log(a === b); // false


// Practice comparisons

/* JavaScript converts the string a = "5" converts to the number 5, then compares both values
   After type coercion, the equation becomes: 5 != 5, results = false  */
console.log(a != b);  // false

/* Strict equality compares the string a = "5" with number b = 5
   The equation becomes: 5 !== "5", results = true  */
console.log(a !== b); // true

/* Simply checks if a = 5 greater than 3
   The equation is: 5 > 3, results = true  */
console.log(a > 3);   // true

/* - JavaScript converts the string y = "7" into a number 7
   - <, >, <=, and >= are a numeric operators so it becomes: 7 > 5  */
let y = "7";
console.log(y > 5); // true

/* Simply checks if a = 5 less than or equal to 5
   The equation is: 5 <= 5, results = true  */
console.log(a <= 5);  // true
