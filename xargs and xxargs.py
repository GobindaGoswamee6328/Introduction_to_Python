
#xargs:

def student(id,name,cgpa):
    print(id,name,cgpa)

student(102,"Simanta", 3.67)


#Addition:
def add(num1,num2,num3,num4):
    sum = num1 + num2 + num3 + num4
    print(sum)

add(10,20,30,40)


#xxargs:

def students(**details):
    print(details)
    print(details["name"])

students(id=103,name="Joy",cgpa=3.77)
