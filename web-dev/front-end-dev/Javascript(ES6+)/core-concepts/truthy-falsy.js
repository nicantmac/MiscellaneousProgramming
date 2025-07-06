// Falsy values: false, 0, "", null, undefined, NaN
let val = 0;

if (val) {
  console.log("Truthy!");
} else {
  console.log("Falsy!"); // This will run
}

// Truthy values: anything not falsy
let name = "Knight";
if (name) {
  console.log("Name is truthy"); // This will run
}
