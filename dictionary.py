def main():
    student_info = open('students.txt', 'a')
    menu_selection = input("What would you like to do? \na. Add a new student\nb. Find information for a student\nc. Drop a student\nd. List all students")
    if menu_selection == a:
        name = str(input("What is the student's name?"))
        sid = str(input("What is the student's id?"))
        email = str(input("What is the student's email address?"))
        new_students = ",".join("\n", name, sid, email)
        student_info.write(new_students)
        
        
    




main()
