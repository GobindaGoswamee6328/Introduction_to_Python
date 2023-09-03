'''
num2 = int(input("Enter a Number : "))
result = 20 / num2
print(result)
print("Done")

'''

try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
    print("Done")

except ZeroDivisionError:
    print("Dividing by Zero is not Possible")

except IndexError:
    print("Index Error")

finally:
    print("Successful")
