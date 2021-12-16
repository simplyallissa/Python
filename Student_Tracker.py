def main():
    student_info = open('students.txt', 'a+')
    menu_selection = input("You can choose between the following options: \na. Add a new student\nb. Find information for a student\nc. Drop a student\nd. List all students\nWhat would you like to do? ")
    if menu_selection == 'a':
        name = str(input("What is the student's name?"))
        sid = str(input("What is the student's id?"))
        email = str(input("What is the student's email address?"))
        new_student = (name, sid, email)
        ",".join(new_student)
        student_info.write("\n" + str(new_student))
    elif menu_selection == 'b':
        student_to_lookup = str(input("What student would you like to lookup?"))
        for line in student_info:
            name, sid, email = line.split()
            print(name)
            print("in loop")
            if name == student_to_lookup:
                print(name, sid, email)
            else:
                print("Student not found")
    elif menu_selection == 'c':
        student_to_drop = str(input("What student would you like to drop?"))
        for line in student_info:
            name, sid, email = line.split()
            if name == student_to_drop:
                f.write(line)
                print("Student dropped.")
    elif menu_selection == 'd':
        print(student_info.read())

main()
