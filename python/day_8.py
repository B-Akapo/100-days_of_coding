# Author: Bunmi Akapo
# Date: 5th October 2022
# Description: create daily affirmation statement taking user input

name = input("Hello there. What's your name? ")
print()
print("Nice to meet you", name)
print("I am Paula")

while True:
    try:
        print()
        feeling = input("How are you feeling today? Great or Not-so-great? ")
        print()
        if feeling == "Great" or feeling == "great":
            print()
            print("I am glad to hear that", name)
            print(
                "Keeping a positive outlook in life makes things much easier and happier.")
            print("By the way, I have a question for you...")
            break
        elif feeling == "Not-so-great" or feeling == "not-so-great" or feeling == "not so great":
            print("AWWW!!, thats sad to year", name)
            print("I know what will cheer you up.")
            print("Just answer one question...")
            break
        else:
            print("I didn't catch that")
            print()
    except ValueError:
        print("Invalid")
        continue


while True:
    try:
        print()
        day = input("What day of the week is it? ")

        if day in {"Monday", "monday"} and feeling in {"Great", "great"}:
            print()
            print(day, "is a great day of the week, you can see it as a new beginning")
            print("or and opportunity to achieve your goals. have a great week")
            break
        elif day in {"Monday", "monday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print("I know", day, "can seem kind of hard")
            print("But you have to find the strength to push through.")
            print("See it as a new beginning or and opportunity to achieve your goals")
            print("I am rooting for you", name, "I know you can do it.")
            break
        elif day in {"Tuesday", "tuesday"} and feeling in {"Great", "great"}:
            print()
            print("Second day of day week. I like", day, "because it is the beginning of the countdown to the weekend")
            break
        elif day in {"Tuesday", "tuesday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print("Hey", name, "You made it to the second day of the week. I am proud of you")
            print("Keep your head up it can only get better")
            break
        elif day in {"Wednesday", "wednesday"} and feeling in {"Great", "great"}:
            print()
            print("Hey go getter! Its middle of the week. How far have you gone with your goals?")
            print("Honestly you deserve and ice cream")
            break
        elif day in {"Wednesday", "wednesday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print("Hey", name, "I want you to be proud of yourself. You are doing well")
            print("Half of the week is gone and you are still standing strong")
            print("Well done", name, "I am proud of you.")
            break
        elif day in {"Thursday", "thursday"} and feeling in {"Great", "great"}:
            print()
            print("Whewwwww!!! Its thursday. Why not catch a little break and enjoy happy hour")
            print("Come on then, off you go with your friends. You deserve it")
            break
        elif day in {"Thursday", "thursday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print("You are stronger than you think. You made it to thursday. I know its been a rough week")
            print("So i just thought to let you know I am rooting for you and I love you.")
            print("You are not alone")
            break
        elif day in {"Friday", "friday"} and feeling in {"Great", "great"}:
            print()
            plans = input("What are your plans for the weekend? ")
            print("hmmmmmm. I know you plan on", plans, "you could also have a quiet night with some friends/family.")
            break
        elif day in {"Friday", "friday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            plans = input("What are your plans for the weekend? ")
            print(plans, "??? I know it's been a stressful week. But you made it to the end. Well done")
            print("why not rest in and call someone and talk. It would be good for you to let out steam. ")
            break
        elif day in {"Saturday", "saturday"} and feeling in {"Great", "great"}:
            print()
            print(day, "laundry day, picnic day, shopping day!!! why not choose something that makes you happy to do today")
            break
        elif day in {"Saturday", "saturday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print(day, "laundry day, picnic day, shopping day!!! why not choose something that makes you happy to do today")
            print("You deserve and need it after the week you have been through. Go spoil yourself")
            break
        elif day in {"Sunday", "sunday"} and feeling in {"Great", "great"}:
            print()
            print("Tomorrow is another week. What goals have you set for yourself?")
            print("Whatever it is, I know you will knock it out of the park. Good luck")
            break
        elif day in {"Sunday", "sunday"} and feeling in {"Not-so-great", "not-so-great", "not so great"}:
            print()
            print("You dont have to dread the week you know.... You are beautiful and strong and will accomplis a lot this week.")
            break
        else:
            print("I didn't catch that?")
    except ValueError:
        print("Invalid")
        continue
