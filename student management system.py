class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_no = input("Enter Roll Number: ")

        if roll_no in self.students:
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        self.students[roll_no] = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        for roll_no, details in self.students.items():
            print(f"\nRoll No: {roll_no}")
            print(f"Name   : {details['Name']}")
            print(f"Age    : {details['Age']}")
            print(f"Course : {details['Course']}")

    def search_student(self):
        roll_no = input("Enter Roll Number to search: ")

        if roll_no in self.students:
            student = self.students[roll_no]
            print("\nStudent Found:")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}")
        else:
            print("Student not found!")

    def update_student(self):
        roll_no = input("Enter Roll Number to update: ")

        if roll_no in self.students:
            print("Enter new details:")

            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            self.students[roll_no] = {
                "Name": name,
                "Age": age,
                "Course": course
            }

            print("Student updated successfully!")
        else:
            print("Student not found!")

    def delete_student(self):
        roll_no = input("Enter Roll Number to delete: ")

        if roll_no in self.students:
            del self.students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Thank you for using the Student Management System!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()