
num1 = {1,2,3,4,5}
num2 = set([4,5,6])
num2.add(7)
num2.remove(5)

print(num2)
print(5 in num2)


#Union:

num1 = {1,2,3,4,5}
num2 = set([4,5,6,7])

print(num1 | num2)


#Intersaction:

num = {1,2,3,4,5}
num2 = set([4,5,6])

print(num1 & num2)


#Difference:

num = {1,2,3,4,5}
num2 = set([4,5,6])

print(num1 - num2)


