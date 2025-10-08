age = int(input("Enter your age: "))

if age >= 18:
  print("You are now signed up!")
elif age < 0:
  print("You haven't been born yet!")
else:
  print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N): ")

if response == "Y":
  print("Have some food!")
else:
  print("No food for you")