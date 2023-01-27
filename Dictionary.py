list_of_students = []

def add_new_student():
    name_ = input(" Enter Your Student Name: ")
    father = input("Enter Your Father Name: ")
    age = input("Enter Your Age: ")
    study = input("Enter Your study: ")
    semester = input("Enter Your semester: ")
    status = input("Enter Your status: ")
    height = input("Enter Your Height: ")
    student = {
        "name": name_,
        "father": father,
        "age": age,
        "study": study,
        "semester": semester,
        "status": status,
        "height": height
    }
    list_of_students.append(student)
    print("Student added succesfully")
    print("Press enter to go back")
    input()
    
 

def show_all_students():

    print("********* List of Students ************")
    for student in list_of_students:
        print(f"{student['name']} - {student['study']}")
    print("\n\nPress enter to go back")
    input()
    
def main_menu():

    print("*"*30)
    print("1: Add a new Student")
    print("2: View all students")
    choice = input("What do you want: ")
    if choice == "1":
        add_new_student()
    elif choice == "2":
        show_all_students()
    else:
        print("Invalid Choice")

while True:
    main_menu()











