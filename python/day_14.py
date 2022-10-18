# Author: Bunmi Akapo
# Date: 17th October 2022
# Description: Rock Paper Scissors game

from getpass import getpass

print("""It is time for an epic game of rock paper scissors

Are you ready??

Players set your thumb!!!

GOOOOOOOOOOO""")

p1 = getpass("\nPlayer 1 Choose your weapon rock, paper, scissors: ")
p1 = p1.lower()
p2 = getpass("\nPlayer 2 Choose your weapon rock, paper, scissors: ")
p2 = p2.lower()

if p1 == p2:
    print(f"\nYou both picked '{p1}' it's a tie")

elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
    print(f"\nPlayer 1 picked '{p1}' and player 2 picked '{p2}' Player 1 Wins")
else:
    print(f"\nPlayer 2 picked '{p2}' and player 1 picked '{p1}' Player 1 Wins")
