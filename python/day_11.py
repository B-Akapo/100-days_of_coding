# Author: Bunmi Akapo
# Date: 16th October 2022
# Description: check how many seconds are in a given year

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
leap_year = (days_in_year + 1) * hours_in_day * minutes_in_hour * seconds_in_minute

input_year = int(input("Please enter a year: "))

if input_year % 4 != 0:
    print(f"there are {seconds_in_year} in {input_year}")
elif input_year % 4 == 0:
    print(f"there are {leap_year} in {input_year}")


