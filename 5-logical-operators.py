# Temos OR, AND, NOT

temp = 25.0
is_raining = False

if temp > 35 or temp < 0 or is_raining:
  print("The outdoor event is cancelled")
else:
  print("The outdoor event is still scheduled")

is_sunny = True

if temp >= 28 and is_sunny:
  print("It is HOT outside")
  print("It is SUNNY")
elif temp <= 0 and is_sunny:
  print ("It is COLD outside")
  print("It is SUNNY")
