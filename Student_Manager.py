class Student:
    def __init__(self, name, sid, email):
        self.name = name
        self.sid = int(sid)
        self.email = email

    def printStudent(self):
        return ""+str(self.name) + ","+str(self.sid)+","+str(self.email)

def saveListToFile(student_list):
    student_info = open('students.txt', 'w')
    for student in student_list:
        student_info.write(student.printStudent() + "\n")

def main():
    # open file
    student_info = open('students.txt', 'r')
    student_list = []

    # create new student for each line
    for line in student_info:
        name, sid, email = line.rstrip('\n').split(',')
        student = Student(name, sid, email)
        student_list.append(student)
    student_info.close()
    # add student to a list


    while True:
        menu_selection = input(
            "You can choose between the following options: \na. Add a new student\nb. Find information for a student\nc. Drop a student\nd. List all students\ne. Sort the list of student by ID or name \nq. Quit\nWhat would you like to do? ")
        if menu_selection == 'a':
            name = str(input("What is the student's name?"))
            while True:
                sid = str(input("What is the student's id?"))
                found_match = False
                for student in student_list:
                    if student.sid == sid:
                        print("please enter a new ID, they must be unique")
                        found_match = True
                if found_match is False:
                    break
            email = str(input("What is the student's email address?"))
            new_student = Student(name, sid, email)
            student_info = open('students.txt', 'a')
            student_info.write(new_student.printStudent()+"\n")
            student_info.close()
            student_list.append(new_student)

        elif menu_selection == 'b':
            student_to_lookup = str(input("What student would you like to lookup? \nPlease either their ID number"))
            found_student = False
            for student in student_list:
                if student.sid == student_to_lookup:
                    print(student.printStudent())
                    found_student = True
            if found_student is False:
                print("could not find student with ID of "+student_to_lookup)

        elif menu_selection == 'c':
            student_to_drop = str(input("What student would you like to drop? \nPlease enter the ID number of the student"))
            student_found = False
            for student in student_list:
                if student.sid == student_to_drop:
                    student_list.remove(student)
                    student_found = True
            if student_found is False:
                print("could not find a student with that ID")
            else:
                saveListToFile(student_list)

        elif menu_selection == 'd':
            for student in student_list:
                print(student.printStudent())
                #print(student.name + " " + student.sid + " " + student.email)
        elif menu_selection == 'e':
            name_or_id = input("a. Sort by Name\nb. Sort by ID ")

            if name_or_id == 'a':
                student_list.sort(key=lambda x: x.name)
            elif name_or_id == 'b':
                student_list.sort(key=lambda x: x.sid)
            else:
                print("please enter a valid menu option")
            saveListToFile(student_list)

        elif menu_selection == 'q':
            exit(0)

main()
