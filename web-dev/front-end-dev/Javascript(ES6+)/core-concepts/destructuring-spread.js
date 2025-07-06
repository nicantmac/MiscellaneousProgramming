// Destructuring
const card = { name: "Mega Minion", cost: 3 };
const { name, cost } = card;
console.log(name); // "Mega Minion"

// Spread with arrays
let deck1 = ["Archer", "Knight"];
let deck2 = ["Giant", ...deck1]; // spreads deck1 into deck2
console.log(deck2); // ["Giant", "Archer", "Knight"]
