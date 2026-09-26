class Student:
    def __init__(self, name, student_id, email, age, department, *marks):
        self.name = name
        self.student_id = student_id
        self.__email = email       # Encapsulation
        self.age = age
        self.department = department
        self.__marks = marks       # Encapsulation

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

    def calculate_result(self):
        if len(self.__marks) == 0:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            return "A+"
        elif average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "F"

    def get_student_type(self):
        return "Student"

    # Method overloading using default argument
    def update_info(self, email=None, age=None):
        if email:
            self.__email = email

        if age:
            self.age = age

        print("Information updated.")


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester, *marks):
        super().__init__(
            name, student_id, email, age, department, *marks
        )
        self.semester = semester

    # Method overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic, *marks):
        super().__init__(
            name, student_id, email, age, department, *marks
        )
        self.research_topic = research_topic

    # Method overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


# Creating objects

student1 = UndergraduateStudent(
    "Junayed",
    "UG101",
    "junayed@gmail.com",
    18,
    "CSE",
    4,
    85, 78, 90
)

student2 = GraduateStudent(
    "Rahim",
    "GR201",
    "rahim@gmail.com",
    24,
    "CSE",
    "Artificial Intelligence",
    88, 92, 85
)


# Display information

print("----- Undergraduate Student -----")
student1.display_info()
print("Type:", student1.get_student_type())
print("Result:", student1.calculate_result())

print()

print("----- Graduate Student -----")
student2.display_info()
print("Type:", student2.get_student_type())
print("Result:", student2.calculate_result())


# Polymorphism

print("\n----- Polymorphism -----")

students = [student1, student2]

for student in students:
    print(student.get_student_type())


# Method overloading / default argument

print("\n----- Updating Information -----")

student1.update_info(age=19)
student1.update_info(email="newemail@gmail.com", age=20)