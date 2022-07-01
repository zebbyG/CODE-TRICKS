class shoes:
  def __init__(self, name, brand, type, cost):
    self.brand = brand
    self.type = type
    self.cost = cost
    self.name = name
  def shoe_sale(self):
    print("Hello " + self.name + "!!!" "\nThis is an " + self.type + " shoe, from the " + self.brand + " company and it retails at $" + self.cost + ".")
shop1 = shoes("Zebbylion Njau", "Nike", "Air max", "35")
shop1.shoe_sale()