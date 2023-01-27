# create students database project
l = [
    {'name': 'Usman', 'father': 'Tariq', 'study': 'bscs'}
]

def main_menu():
    print("*"*50)
    print("1- Add a new student: ")
    print("2- View all students: ")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_new_student()
    elif choice == "2":
        all_students()
    else:
        print("Invalid choice.")

def add_new_student():
    name = input("Enter Your name: ")
    father = input("Enter Your father name: ")
    study = input("Enter your study: ")
    # here we create a dictionary
    student = {"name": name, "father": father, "study": study}
    l.append(student)
    print("Student added successfully.")
    input("Press Enter to go back.")
    

def all_students():
    for student in l:
        print({student["name"]}, student)


while True:
    main_menu()
