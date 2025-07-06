// Basic function
function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Archer"));

// Scope example
let outer = "global";

function testScope() {
  let inner = "local";
  console.log(outer); // "global"
  console.log(inner); // "local"
}

// console.log(inner); // ❌ Error: not defined outside
