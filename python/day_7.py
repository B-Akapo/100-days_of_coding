# Author: Bunmi Akapo
# Date: 5th October 2022
# Description:  program that checks a real backstreet boys fan
# and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

fan_check = input("are you a backstreet boys fan? ")

if fan_check == "yes" or fan_check == "Yes":
    print("We'll see about that 😈")

    first_album = input("What was their first album? ")
    if first_album == "backstreet boys" or first_album == "Backstreet Boys" or first_album == "Backstreet boys":
        print("Lucky guess. Let's try another")
    else:
        print("Aha I knew you were fake")

    grammy = input("Do they have a grammy? ")
    if grammy == "no" or grammy == "No":
        print("Sadly you are right. They deserve one though")
    else:
        print("get out of my sight fakey")

    brooklyn_99 = input("which seasonal recently used I want it that way in one of its scenes? ")
    if brooklyn_99 == "brooklyn 99" or brooklyn_99 == "Brooklyn 99":
        print("You are a super fan.")
    else:
        print("Get out fakey")
else:
    print("I see you a not a person of culture")
