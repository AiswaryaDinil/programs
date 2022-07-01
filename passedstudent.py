# fstudent=open("students.txt")
# allstudents=[stud.rstrip("\n") for stud in fstudent]
#
# ffailed=open("failed.txt")
# failedstudent=[stud.rstrip("\n") for stud in ffailed]
#
# fpassed=open("passed.txt","w")
# passed_student=set(allstudents)-set(failedstudent)
# print(passed_student)
# for st in passed_student:
#     st+="\n"
#     fpassed.write(st)

passed=open("passed.txt","a")
name="anu"
passed.write(name)
