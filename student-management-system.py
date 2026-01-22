students = []

def add_student():
    name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "name": name,
        "matric_number": matric_number,
        "department": department
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students available.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Matric Number:", student["matric_number"])
        print("Department:", student["department"])
        print("------------------------")


def search_student():
    matric = input("Enter matric number to search: ")

    for student in students:
        if student["matric_number"] == matric:
            print("Student Found!")
            print("Name:", student["name"])
            print("Department:", student["department"])
            return

    print("Student not found.\n")


def main_menu():
    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


main_menu()
