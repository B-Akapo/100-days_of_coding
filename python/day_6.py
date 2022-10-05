# Author: Bunmi Akapo
# Date: 5th October 2022
# Description: user logins with their username and password correctly and then gets individual greeting.

username = input("Enter username: ")
password = input("Please enter password: ")

if (username == "Bunmi") and (password == "abcdefgh"):
        print("Welcome", username)

elif (username == "Austin") and (password == "ijklmnop"):
    print("Welcome", username)

elif (username == "Gabriel") and (password == "qrstuvwx"):
    print("Welcome", username)

else:
    print("invalid user/password")
