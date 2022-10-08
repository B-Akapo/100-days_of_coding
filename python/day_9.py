# Author: Bunmi Akapo
# Date: 8th October 2022
# Description: Telling a user their generational group after inputting the year of their birth

import datetime
year_of_birth = int(input("Please enter the year you were born: "))

today = datetime.date.today()
current_year = today.year

if (year_of_birth < 1883):
    print("You must be a vampire because I dont know how are you still alive?")
elif (year_of_birth >= 1883) and (year_of_birth <= 1900):
    print("Lost Generation")
elif (year_of_birth >= 1901) and (year_of_birth <= 1927):
    print("Greatest Generation")
elif (year_of_birth >= 1928) and (year_of_birth <= 1945):
    print("Silent Generation")
elif (year_of_birth >= 1946) and (year_of_birth <= 1964) or (year_of_birth == 64):
    print("Baby Boomers")
elif (year_of_birth >= 1965) and (year_of_birth <= 1980):
    print("Generation X")
elif (year_of_birth >= 1981) and (year_of_birth <= 1996):
    print("Millennials")
elif (year_of_birth >= 1997) and (year_of_birth <= 2012):
    print("Generation Z")
elif (year_of_birth > 2012) and (year_of_birth <= current_year):
    print("Generation Alpha")
else:
    print("Are you sure you exist??")
