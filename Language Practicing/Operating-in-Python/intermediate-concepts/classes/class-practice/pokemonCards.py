class Pokemon:
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank

  def pokemonName(self):
    print(f"My name is {self.name}")

  def pokemonRank(self):
    print(f"My rank is {self.rank}")

pokemon1 = Pokemon("Charizard", "Ultra")
