def net_price(list_price: float, discount: float = 0, tax: float = 0.05):
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1, 0.07))
print(net_price(500))