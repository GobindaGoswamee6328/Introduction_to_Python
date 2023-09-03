

class student:
    roll = ""
    cgpa = ""

    def __init__(self,roll,cgpa):
       self.roll = roll
       self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, Cgpa : {self.cgpa}")


sobuj = student(102,3.75)
sobuj.display()

joy = student(105,3.45)
joy.display()

