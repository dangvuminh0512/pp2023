student = {}
course = {}
def input_student():
    num_of_student = int(input("enter number of student:"))
    for i in range(num_of_student):
        studentid = input("enter student id:")
        studentname = input("enter student name:")
        studentDOB = input("enter student DOB:")
        student[studentid] = {"student_id": studentid, "student_name": studentname, "student_DOB": studentDOB, "courseID": [], "mark": [] }
def input_courses():
    coursenum = int(input("enter number of the course:"))
    for j in range(coursenum):
        courseid = input("enter course id:")
        coursename = input("enter course name:")
        course[courseid] ={"course_id":  courseid, "course_name": coursename}
def print_student():
    for studentid in student:
        print(studentid,": ",student[studentid].get('student_name'),student[studentid].get('student_DOB'))
def print_course():
    for course_id in course:
        print(course_id,": ",course[course_id].get("course_name"))
def input_mark():
    course_id = input("enter the course id to put the mark: ")
    if course_id not in course:
        print("type again")
        return
    for studentsid in student:
        n = float(input("enter the mark :"))
        student[studentsid]['mark'].append(n)
def print_mark():
    course_id = input("enter the course id to put the mark: ")
    if course_id not in course:
        print("type again")
        return
    else:
     for studentid in student:
            print(student[studentid]['student_name'],"",student[studentid]['mark'])
input_student()
input_courses()
while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_mark()
    elif choice == "2":
        print_course()
    elif choice == "3":
        print_student()
    elif choice == "4":
        print_mark()
    elif choice == "5":
        break