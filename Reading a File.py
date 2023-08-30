
#Size,Read,List:

file = open("Student.txt","r+")

#print(file.readable())

'''
text = file.read()
print(text)

size = len(text)
print(size)

text = file.readlines()
print(text)
'''


#using For-Loop:

for line in file:
    print(line)

file.close()
