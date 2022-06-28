class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")
    def __str__(self):
        return self.course_name

djanjo=Course()
djanjo.add_course(course_name="Django",active_status=True)
bigdata=Course()
bigdata.add_course(course_name="Bigdata",active_status=True)

class Batch:
    def add_batch(self,**kwargs):
        self.b_code = kwargs.get("b_code")
        self.bname = kwargs.get("bname")
        self.course=kwargs.get("course")
    def __str__(self):
        return self.b_code

dj1=Batch()
dj1.add_batch(b_code="Dj1",bname="may2k22",course=djanjo)
bd1=Batch()
bd1.add_batch(b_code="Big1",bname="may2k22",course=bigdata)
# print(dj1)
# print(bd1)


class Student:
    def add_stud(self, **kwargs):
        self.student_name = kwargs.get("student_name")
        self.gender = kwargs.get("gender")
        self.roll = kwargs.get("roll")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name

rahul=Student()
rahul.add_stud(student_name="rahul",gender="Male",roll="2342",batch=dj1)
anu=Student()
anu.add_stud(student_name="Anu",gender="Female",roll="6457",batch=bd1)

print(rahul)
print(rahul.batch.course.course_name)
print(anu)

