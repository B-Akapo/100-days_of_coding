# Author: Bunmi Akapo
# Date: 22nd October 2022
# Description: Using While Loop to ask a question till user exits

exit = ""
while exit != "yes":
    animal = input("What animal do you want to listen to? ")
    animal = animal.lower()
    if animal == "cow":
        print(f"the {animal} goes mooooo")
    elif animal == "dog":
        print(f"the {animal} goes woof")
    elif animal == "cat":
        print(f"the {animal} goes meow")
    else:
        print("Sorry we dont have that sound.")
    exit = input("do you wanna leave? ")
