class Employee:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
        self.e_id=kwargs.get("e_id")
    def __str__(self):
        return self.name

employee=Employee(e_id=100,name="aiswarya",role="hr")
print(employee)

class Dept():
    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("not accessible")
    def __str__(self):
        return self.dept_name

department=Dept(dept_name="CS",user=employee)
print(department)
print(department.user)