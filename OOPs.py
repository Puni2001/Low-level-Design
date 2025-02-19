# 5. Demo Understanding Classes, Objects and Constructors

class Name:
    def __init__(self,firstName, middleName, lastName):
        self.FirstName = firstName
        self.MiddleName = middleName
        self.LastName = lastName
        
class Student:
    def __init__(self,rollNo,sname, course):
        self.RollNo = rollNo
        self.StudentName = sname
        self.Course = course
        
student1 = Student(100,Name('Punith',"Roopa","Shantharaju"),"Python")
student2 = Student(100,Name('Pooja',"s","BCA"),"Python with Django")
student3 = Student(100,Name('Canara',"Bank","Trainee"),"Python With OOPS")

students = [student1, student2, student3]
for student in students:
    print("Student Name: {} {} {}\nRoll No: {}\nCourse: {}\n ".format(student.StudentName.FirstName, student.StudentName.MiddleName, student.StudentName.LastName, student.RollNo,student.Course))