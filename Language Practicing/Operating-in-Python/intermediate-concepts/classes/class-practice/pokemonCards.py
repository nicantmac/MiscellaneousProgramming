class Pokemon:
  def __init__(self, name, rank):
    self.name = name
    self.rank = rank

  def pName(self):
    print(f"My name is {self.name}")

  def pRank(self):
    print(f"My rank is {self.rank}")

pokemon1 = Pokemon("Charizard", "Ultra")
pokemon2 = Pokemon("Bulbasaur", "Master")

pokemon1.pName()
pokemon1.pRank()

pokemon2.pName()
pokemon2.pRank()
