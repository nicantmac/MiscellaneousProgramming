//Type coercion is when JavaScript automatically converts one data type to another during an operation.

//Two Types:
//Implicit coercion – JS converts behind your back 😅

//Explicit coercion – you tell JS what to do

// Implicit Coercion

console.log("5" + 2);       // "52" (number 2 coerced to string)
console.log("5" - 2);       // 3   (string "5" coerced to number)
console.log(true + 1);      // 2   (true becomes 1)
console.log(false + "2");   // "false2" (false becomes string)

console.log(null + 1);      // 1   (null becomes 0)
console.log(undefined + 1); // NaN (undefined becomes NaN)

// Comparison coercion
console.log("5" == 5);      // true  (== allows coercion)
console.log("5" === 5);     // false (=== is strict — no coercion)

console.log([] == 0);       // true  (empty array is coerced to 0)
console.log([] === 0);      // false

console.log([] == ![]);     // true  (wild one)
console.log("0" == false);  // true

// Explicit Coercion

console.log(Number("42"));     // 42
console.log(String(123));      // "123"
console.log(Boolean("hello")); // true
console.log(Boolean(""));      // false

// NaN check
console.log(Number("abc"));    // NaN
console.log(isNaN("abc"));     // true
