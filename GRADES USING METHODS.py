class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Grades:", self.grades)

    def calculate_average_grade(self):
        if self.grades:
            average_grade = sum(self.grades) / len(self.grades)
            return average_grade
        else:
            return "No grades available"


def main():
    # Creating a student database
    student1 = Student("John", 20)
    student1.add_grade(85)
    student1.add_grade(90)

    student2 = Student("Alice", 22)
    student2.add_grade(75)
    student2.add_grade(80)
    student2.add_grade(78)

    # Displaying student information
    print("Student 1 information:")
    student1.display_info()
    print("Average Grade:", student1.calculate_average_grade())
    print()

    print("Student 2 information:")
    student2.display_info()
    print("Average Grade:", student2.calculate_average_grade())
    print()

    # Adding a new student
    student3 = Student("Bob", 21)
    student3.add_grade(88)
    student3.add_grade(92)

    print("Student 3 information:")
    student3.display_info()
    print("Average Grade:", student3.calculate_average_grade())

if __name__ == "__main__":
    main()