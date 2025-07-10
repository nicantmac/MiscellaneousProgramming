class Card:
    def __init__(self, name, elixir_cost, rarity, card_type):
      self.name = name
      self.elixir_cost = elixir_cost
      self.rarity = rarity
      self.card_type = card_type

    # Create method to display attributes of the card
    def display_info(self):
      print(f"Name: {self.name}")
      print(f"Cost: {self.elixir_cost} Elixir")
      print(f"Rarity: {self.rarity}")
      print(f"Type: {self.card_type}")

    # Create method to check if the card is expensive
    def isExpensive(self):
      return self.elixir_cost >= 5

    # Create method to check if the card is a legendary ranked card
    def isLegendary(self):
      if self.rarity == "Legendary":
        return f"This is a legendary card: {self.name} 🔥"
      return f"{self.name} is not a legendary."
        
# We're creating: the Royal Giant, costing 6 elixir, ranked common level, and is a ground troop
card1 = Card("Royal Giant", 6, "Common", "Troop")

# Next, try calling display_info, is_expensive, and is_legendary methods 
card1.display_info()
print(card1.is_expensive()) 
print(card1.isLegendary())
