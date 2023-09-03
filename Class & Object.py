
class student:
    roll = ""
    cgpa = ""


sobuj = student()
print(isinstance(sobuj,student))
sobuj.roll = 103
sobuj.cgpa = 3.45
print(f"Roll : {sobuj.roll}, Cgpa : {sobuj.cgpa}")


joy = student()
print(isinstance(joy,student))
joy.roll = 105
joy.cgpa = 3.70
print(f"Roll : {joy.roll}, Cgpa : {joy.cgpa}")
