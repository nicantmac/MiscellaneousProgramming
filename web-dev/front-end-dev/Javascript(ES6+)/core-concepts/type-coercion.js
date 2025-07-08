//Type coercion is when JavaScript automatically converts one data type to another during an operation.

/* Reminder: (empty array [], NaN, empty string "", 0, the boolean literal: false, undefined, and null)
             - These values prior equate to false in JavaScript */

/*  Two Types:
  - Implicit coercion – JS converts behind your back
  - Explicit coercion – you tell JS what to do  */

// Implicit Coercion

/* With (+), if either side is a string, JavaScript converts the other to a string and concatenates
   So string wins here because (+) is overloaded to mean both math and string concatenation  */
console.log("5" + 2); // Output: "52" (number 2 coerced to string)

/* With  -, *, /, etc. JavaScript always tries to convert everything to numbers, 
   because those operators only make sense numerically.
   So numbers wins here because (-) because string is converted  */
console.log("5" - 2); // Output: 3 (string "5" coerced to number)

/* With boolean operations, JavaScript converts boolean to its numeric value
   So true = 1, the operation becomes: 1 + 1 = 2  */
console.log(true + 1); // Output: 2 

/* Using (+) with string, strings becomes prioritized
   So false will literally concatenate, the operation becomes: false + "2" = false2  */
console.log(false + "2"); // Output: "false2"

/* Using (+) with numeric values, numbers become prioritized
   The numeric value of null = 0, the operation becomes: 0 + 1 = 1  */
console.log(null + 1); // Output: 1  (null becomes 0)

/* Using (+) with numeric values, numbers become prioritized
   undefined = NaN(no numeric value), the operation becomes: NaN + 1 = NaN  */
console.log(undefined + 1); // Output: NaN (undefined becomes NaN)

/* Strict equality (===), with falsey values (checking for: data type and value)
   null, undefined = false, however data type: null = object, data type: undefined = undefined(no numeric value)
   the operation becomes: (false & object) === (false & undefined) = false  */
console.log(null === undefined) // Output: false (different types, so strict equality fails)


// Comparison coercion

/* Loose equality (==), type coercion will prioritize value
   JavaScript converts the string to a number, then does a numeric comparison
   the operation becomes: 5 == 5 -> true  */
console.log("5" == 5); // Output: true (== allows coercion)

/* Strict equality (===), prioritizes (checking: data type and value)
   JavaScript compares the string = "5" to the number = 5, then does a strict comparison
   the operation becomes: "5" === 5 -> false  */
console.log("5" === 5); // Output: false (=== is strict — no coercion)

/* The loose equality (==), type coercion prioritizes value
   empty arrays[] in JavaScript register as false, the boolean value for zero = false
   the operation becomes: 0 == 0 -> false  */
console.log([] == 0); // true (empty array is coerced to 0)

/* The strict equality (===), JavaScript checks for both value AND type, without coercion
   empty arrays[], numeric zero = false => however data type: empty array[] = object, data type: numeric zero = number
   the operation becomes: [] === 0 -> false  */
console.log([] === 0); // false

/* The loose equality (==), JavaScript checks value with coercion
   [] is truthy, so ![] → false → [] == false → coerced to 0 == 0 → true
   the operation becomes: [] === ![] -> true  */
console.log([] == ![]); // Output: true (wild one)

/* JavaScript checks value with coercion
   here, false → coerced to 0 (number), "0" → coerced to 0 (also a number)
   the operation becomes: 0 == false -> true  */
console.log("0" == false); // Output: true

// Explicit Coercion
console.log(Number("42"));     // "42" - (string) becomes 42 (number)
console.log(String(123));      // "123" - (number) becomes 123 (string)
console.log(Boolean("hello")); // true - non-empty string results truthy
console.log(Boolean(""));      // false - empty string results falsey

console.log(Number("abc"));    // Output: NaN - "abc" in JS cannot be converted to a number

/* NaN checking (there are two different isNaN functions in JavaScript)
   - isNaN() — Global function and Number.isNaN() — Stricter version
   - Introduced in ES6 (modern JS) the .isNaN() method does not coerce, it only returns true if the value is actually NaN */

/* - isNaN() is original and built-in global function
   - It coerces the value to a number first, then checks if it’s NaN. */
console.log(isNaN("abc")); // Output: true - isNan() returns strictly boolean values
console.log(isNaN(true)); // Output: false (looking for Not-a-Number when true → 1, numeric one is a number)

// .isNaN() method does not coerce, so "abc" is a string, not NaN
console.log(Number.isNaN("abc")); // Output: false
