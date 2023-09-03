'''
try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 / num2
    print(result)

except(ValueError,ZeroDivisionError):
    print("You Have entered wrong Input")

finally:
  print("Thanks!")
'''

def voter (age):
    if age < 18:
        raise ValueError(" Invalid Voter ")
    return " You are allowed to Vote "

try:
    print(voter(20))
    print(voter(16))
except ValueError as error:
    print(error)

