# Student Result Manager

students = []

def add_student():
    number = int(input("How many students do you want to add? "))

    for i in range(number):
        name = input("Enter student name: ")
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
        math = int(input("Enter Math marks: "))

        student = {
            "name": name,
            "physics": physics,
            "chemistry": chemistry,
            "math": math
        }

        students.append(student)

    print("Students added successfully!")


def view_students():

    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")

    for student in students:

        total = (
            student["physics"]
            + student["chemistry"]
            + student["math"]
        )

        percentage = total / 3

        print("----------------------------")
        print("Name:", student["name"])
        print("Physics:", student["physics"])
        print("Chemistry:", student["chemistry"])
        print("Math:", student["math"])
        print("Percentage:", percentage)


def save_students():

    file = open("students.txt", "w")

    for student in students:

        file.write(
            f"{student['name']},"
            f"{student['physics']},"
            f"{student['chemistry']},"
            f"{student['math']}\n"
        )

    file.close()


def load_students():

    try:

        file = open("students.txt", "r")

        for line in file:

            data = line.strip().split(",")

            student = {
                "name": data[0],
                "physics": int(data[1]),
                "chemistry": int(data[2]),
                "math": int(data[3])
            }

            students.append(student)

        file.close()

    except FileNotFoundError:
        pass


load_students()

while True:

    print("\n===== Student Result Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
        save_students()

    elif choice == 2:
        view_students()

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")