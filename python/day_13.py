# Author: Bunmi Akapo
# Date: 17th October 2022
# Description: Create a grading system where user inputs score, and you give them a grade

test_name = input("What is the name of the test you took? ")
overall_score = float(input("What is the maximum score you can get in this test? "))
test_score = float(input("What did you score? "))

percentage = (test_score / overall_score) * 100

final_score = round(percentage, 2)

if final_score < 50.00:
    print(f"your overall score is {final_score}%. That means you have a U")
elif 50.00 <= final_score <= 59.99:
    print(f"your overall score is {final_score}%. That means you have a D")
elif 60.00 <= final_score <= 69.99:
    print(f"your overall score is {final_score}%. That means you have a C")
elif 70.00 <= final_score <= 79.99:
    print(f"your overall score is {final_score}%. That means you have a B")
elif 80.00 <= final_score <= 89.99:
    print(f"your overall score is {final_score}%. That means you have a A-")
elif final_score >= 90:
    print(f"your overall score is {final_score}%. That means you have a A+")
