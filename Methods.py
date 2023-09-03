
class student:
    roll = ""
    cgpa = ""

    def set_value(self,roll,cgpa):
       self.roll = roll
       self.cgpa = cgpa

    def display(self):
        print(f"Roll : {self.roll}, Cgpa : {self.cgpa}")


sobuj = student()
sobuj.set_value(102,3.75)
sobuj.display()

joy = student()
joy.set_value(105,3.55)
joy.display()

