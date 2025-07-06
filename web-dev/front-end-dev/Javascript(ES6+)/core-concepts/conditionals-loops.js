// Here we will understand programming on a conditional level

// Conditions tend to start with if-else, then traverse to looping conditions
// Using concepts from Clash Royale, we'll understand if-else conditions
let elixir = 4;

if (elixir >= 5) {
  console.log("Expensive card");
} else {
  console.log("Playable card");
}

// For loop
/* - let i = 1 --> will start loop at 1
   - i <= 3 --> will stop loop at 3
   - i++ --> will increment the number by 1  */
for (let i = 1; i <= 3; i++) {
  console.log("Battle " + i);
}

// While loop
/* - let count = 0 --> initialize count at 0
   - while(count < 2) --> while number stored in count < 2, the loop continues
   - count++ --> will increment the count by 1 (!required to avoid infinite loop) */
let count = 0;
while (count < 2) {
  console.log("Charge!");
  count++;
}

// forEach() is an array method
const smallCards = ["goblins", "Archer", "fire spirit"]; 

// for the array of cards, let's use forEach() to output each card
// inside forEach(), use an function or arrow function to perform an action
cards.forEach(function(card) {
  console.log("Card:", card);
});

// How for looping differs from  the forEach() array method
const evolutionCards = ["Royal Giant", "Mega Knight", "P.E.K.K.A"];

/* - let i = 0 --> will start loop at 0
   - i < cards.length --> will stop loop at the length of cards
   - i++ --> will increment the number by 1  */
for (let i = 0; i < cards.length; i++) {
  // because for loop, we can perform flexible actions i.e. continuea & break
  if (cards[i] === "Giant") 
    break; // if the current index = Giant, we'll use break to exit loop
  console.log("Card:", cards[i]);
}
