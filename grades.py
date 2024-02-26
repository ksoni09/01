GRADES_FILE = "grades.txt"

def read_grades():
    try:
        with open(GRADES_FILE, "r") as file:
            grades = file.readlines()
            grades = [float(grade.strip()) for grade in grades]
        return grades
    except FileNotFoundError:
        print("No previous grades found.")
        return []
    except ValueError:
        print("Invalid data found in grades file.")
        return []

def write_grade(grade):
    with open(GRADES_FILE, "a") as file:
        file.write(str(grade) + "\n")

def calculate_average(grades):
    if not grades:
        print("No grades available to calculate average.")
        return
    average = sum(grades) / len(grades)
    print("Your average grade is:", average)

def main():
    print("Welcome to the Grade Tracker Program!")
    print("1. Enter a new grade")
    print("2. Calculate average grade")
    print("3. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                grade = float(input("Enter your grade: "))
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100")
                write_grade(grade)
                print("Grade added successfully!")
            except ValueError as e:
                print("Invalid input:", e)
        elif choice == "2":
            grades = read_grades()
            calculate_average(grades)
        elif choice == "3":
            print("Exiting the Grade Tracker Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()