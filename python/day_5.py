# Author: Bunmi Akapo
#Date: 3rd October 2022
#Description: code using if/else statement to see if a user is fit to be a lawyer

print("""Let's see if you'll make an awesome lawyer.
Answer yes or no to the following questions""")

print()
talk = input("Do you like to talk? ")
print()

if talk == "yes":
    print("Have you considered law? ")

print()
organised = input("Are you organised physically and mentally? ")
print()

if organised == "yes":
    print("Maybe you should look at administration? ")

print()
extrovert = input("Are you an extrovert? ")
print()

if extrovert == "yes":
    print("Law is perfect for you? ")

else:
    print("You'll make a fine Administrator")




