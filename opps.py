class Student:
    name:str
    rollno:int
    course:str
    def __init__(self,name,rollno,course):
        # initialising instance variables
        self.name=name
        self.rollno=rollno
        self.course=course
    def print_student(self):
        print(self.name,self.rollno,self.course)

s1=Student("ram",14,"python")
s2=Student("ami",15,"java")

# s1.set_student("ram",14,"python")
s1.print_student()
s2.print_student()

# constructor initilize instance variable