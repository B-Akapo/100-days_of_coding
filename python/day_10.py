# Author: Bunmi Akapo
# Date: 11th October 2022
# Description: part 1. calculating the bill including tip shared by friends

bill = float(input("What was the total Bill? "))
percentage = int(input("How much percentage tip do you want to leave? "))
new_bill = (percentage / 100) * bill
total_bill = new_bill + bill
people = int(input("How many people are sharing the bill? "))
individual_bill = total_bill / people

# roundup bill to two decimal places
individual_bill = round(individual_bill, 2)

print(f"The total bill is {total_bill} with {people} of you that brings the bill to {individual_bill} each")
