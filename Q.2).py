# Q.2)

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.gpa = self.calculate_gpa()

    def calculate_gpa(self):
        m1, m2, m3 = self.marks     #unpacking into 3 variables
        gpa = (1/3) * m1 + (1/2) * m2 + (1/4) * m3
        return gpa

def display_student_info(student):
    print(f"Roll No: {student.roll_no}")
    print(f"Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"GPA: {student.gpa:.2f}")

def add_student(students):
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = tuple(map(float, input("Enter Marks (m1 m2 m3): ").split()))
    student = Student(roll_no, name, marks)     #to call the constructor
    students[roll_no] = student         #to add into student, roll_no => key  and student =>values
    print("Student added successfully!")

def display_all_students(students):
    print("\n--- All Students ---")
    for roll_no, student in students.items():
        display_student_info(student)
        print()

def calculate_gpa_of_student(students):
    roll_no = int(input("Enter Roll No of the student: "))
    student = students.get(roll_no)
    if student:
        print(f"GPA of {student.name}: {student.gpa:.2f}")
    else:
        print("Student not found!")

def main():
    students = {}
    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate GPA of a Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
            
        elif choice == '2':
            display_all_students(students)
            
        elif choice == '3':
            calculate_gpa_of_student(students)
            
        elif choice == '4':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
