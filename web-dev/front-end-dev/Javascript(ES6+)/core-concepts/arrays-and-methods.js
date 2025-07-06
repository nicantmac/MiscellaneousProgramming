let cards = ["Knight", "Archer", "Giant"];

// Access
console.log(cards[0]); // "Knight"

// Add
cards.push("Wizard");
console.log(cards);

// Remove
cards.pop();
console.log(cards);

// Loop
cards.forEach(card => console.log("Card:", card));
