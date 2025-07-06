const card = {
  name: "Musketeer",
  elixir: 4,
  type: "Troop"
};

// Access properties
console.log(card.name);  // "Musketeer"
console.log(card["elixir"]); // 4

// Add new property
card.range = "Long";
console.log(card);

// Loop keys
for (let key in card) {
  console.log(key + ":", card[key]);
}
