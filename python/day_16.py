# Author: Bunmi Akapo
# Date: 24th October 2022
# Description: Using While Loop to make user complete a sentence

# set number of tries to 0
number_of_tries = 0

print("Complete the lyric")
print("Going back to the ______ where I first met you, gonna camp in my sleeping bag I'm not gonna move\n")
while True:
    # begin counting the number of tries
    number_of_tries += 1
    lyric = input(">> ")
    if lyric == "corner":
        print(f"'{lyric}' is correct")
        break
    else:
        print(f"'{lyric}' is wrong. Try again")
print(f"it took you {number_of_tries} tries to get it")
