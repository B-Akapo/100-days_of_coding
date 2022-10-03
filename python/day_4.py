# Author: Bunmi Akapo
# Date: 3rd October, 2022
# Description: an adventure story where user inputs their choices.

name = input("Enter your name: ")
city = input("Enter a city: ")
time = input("Pick morning or night: ")
fav_snacks = input("Pick your fave snacks: ")
street = input("Name a street: ")

print()
print("Welcome", "\033[31m", name, "\033[0m")
print("Your adventure begins in", city, "in the", time)
print("You are on you way to pick some",
      fav_snacks, "but you meet traffic on", street)

print()
print("""The traffic is being caused by some old lady.
Her shopping bag has torn and all her items are on the floor. 
No one seems to be helping her.""")

print()
vehicle = input("What vehicle are you in?: ")


print()
print("You get down from the", vehicle,
      "and go up to her. You start picking up her groceries, but there is no where to put it.")
print("You look around and you see a newspaper vendor and small store.")

print()
vendor = input("Choose between a newspaper vendor or a small store: ")

print()
print("You pick the", vendor, "It's a faster option",
      "You hurriedly run there to ask for a bag.")
print("The vendor asks if you want paper or plastic.")

print()
bag = input("Paper or Plastic bag? ")

print()
print("You choose", bag)

print()
print("You go back to the old lady and pack everything into the",
      bag, "bag and hand it to her.")
print("She is grateful and offers to treat you to a meal.")
print("You look at the time. It's to late to go where you are headed.")

print()
treat = input("Want to join her for the treat (Yes/No): ")

print()
print("You decide to get", fav_snacks, "tomorrow", time,
      "For now you turn to the lady and say", treat)
print("It's been a long", time,
      "You deserve the rest. Tomorrow you try again. Who knows, you might just get into another adventure")

print()
print("Well done", "\033[31m", name, "\033[0m")
print()
