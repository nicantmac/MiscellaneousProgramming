class Card:
    def __init__(self, name, elixir_cost, rarity, card_type):
      self.name = name
      self.elixir_cost = elixir_cost
      self.rarity = rarity
      self.card_type = card_type

    def display_info(self):
      print(f"Name: {self.name}")
      print(f"Cost: {self.elixir_cost} Elixir")
      print(f"Rarity: {self.rarity}")
      print(f"Type: {self.card_type}")

    def isExpensive(self):
      return self.elixir_cost >= 5

  def isLegendary(self):
      if self.rarity == "Legendary":
        return f"This is a legendary card: {self.name} 🔥"
      return f"{self.name} is not a legendary."
        

card1 = Card("Royal Giant", 6, "Common", "Troop")
card1.display_info()
print(card1.is_expensive())
print(card1.isLegendary())
