let a = 5;
let b = "5";

// Loose equality (==): compares values after type coercion
console.log(a == b); // true

// Strict equality (===): compares values AND types
console.log(a === b); // false

// Other comparisons
console.log(a != b);  // false
console.log(a !== b); // true
console.log(a > 3);   // true
console.log(a <= 5);  // true
