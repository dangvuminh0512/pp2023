student = []
course = []

class Student():
    def __init__(self):
       self.name = input("student name:")
       self.id = input("student id")
       self.dob = input("student dob")
       self.mark = []
    def getname(self):
        return self.name
    def getid(self):
        return self.id
    def getdob(self):
        return self.dob
    def setmark(self,mark):
        self.mark.append(mark)
    def getmark(self):
        return self.mark
def inputstudent():
    num_of_student = int(input("enter number of student:"))
    for i in range(num_of_student):
        student.append(Student())
def printstudent():
    for Student in student:
        print(Student.getname(),":",Student.getid(),Student.getdob())
class Course():
    def __init__(self,coursename,courseid):
       self.coursename = coursename
       self.courseid = courseid
    def get_coursename(self):
       return self.coursename
    def get_courseid(self):
       return self.courseid
def inputcourse():
    num_of_course = int(input("enter number of course:"))
    for i in range(num_of_course):
        coursename = input("course name:")
        courseid = input("course id:")
        course.append(Course(coursename,courseid))
def printcourse():
    for Course in course:
        print(Course.get_coursename(),":",Course.get_courseid())
def inputmark():
    course_id = input("enter the course id to put the mark: ")
    courseid = []
    for Course in course:
        courseid.append(Course.get_courseid())
    if course_id not in courseid:
        print("type again")
        return
    for i in range(len(student)):
        n = int(input("enter the mark :"))
        student[i].setmark(n)
def printmark():
    id = input("enter the course id to put the mark: ")
    courseid = []
    for Course in course:
        courseid.append(Course.get_courseid())
    if id not in courseid:
        print("type again")
        return
    else:
        for Student in student:
            print(Student.getname(), ":", Student.getmark())
inputstudent()
inputcourse()
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        inputmark()
    elif choice == "2":
        printcourse()
    elif choice == "3":
        printstudent()
    elif choice == "4":
        printmark()
    elif choice == "5":
        break



