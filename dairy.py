DIARY_FILE = "diary.txt"

def write_entry():
    with open(DIARY_FILE, "a") as file:
        file.write(input("Write your entry for today:\n") + "\n")

def read_entries():
    try:
        with open(DIARY_FILE, "r") as file:
            entries = file.readlines()
            if entries:
                print("\nPrevious entries:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("\nNo previous entries found.")
    except (FileNotFoundError, PermissionError):
        print("\nUnable to access diary file or no previous entries found.")

def main():
    while True:
        print("\n1. Write an entry")
        print("2. View previous entries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Exiting the diary application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
