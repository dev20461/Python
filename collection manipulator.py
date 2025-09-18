from datetime import datetime

# Student Database (List of Dictionaries)
students = []

# Function to add a student
def add_student():
    print("\nEnter student details:")
    student_id = input("Student ID: ")
    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    grade = input("Grade: ")
    subjects = input("Subjects (comma-separated): ").split(",")

    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    except ValueError:
        print("Invalid date format! Age set to 0.")
        age = 17

    # Store student info
    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "DOB": dob,
        "Grade": grade,
        "Subjects": [s.strip() for s in subjects]
    }
    students.append(student)
    print("\nStudent added successfully!")
def display_students():
    if not students:
        print("\nNo students found!")
        return
    print("\n--- Display All Students ---")
    for s in students:
        print(f"Student ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | "
              f"Grade: {s['Grade']} | Subjects: {', '.join(s['Subjects'])}")

def update_student():
    sid = input("\nEnter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            print("Leave blank if no change.")
            new_name = input(f"New Name ({s['Name']}): ") or s["Name"]
            new_grade = input(f"New Grade ({s['Grade']}): ") or s["Grade"]
            new_subjects = input(f"New Subjects (comma-separated) [{', '.join(s['Subjects'])}]: ")

            s["Name"] = new_name
            s["Grade"] = new_grade
            if new_subjects:
                s["Subjects"] = [sub.strip() for sub in new_subjects.split(",")]
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    sid = input("\nEnter Student ID to delete: ")
    global students
    students = [s for s in students if s["ID"] != sid]
    print("Student deleted (if existed).")

def display_subjects():
    all_subjects = set()
    for s in students:
        all_subjects.update(s["Subjects"])
    if all_subjects:
        print("\nSubjects Offered:", ", ".join(all_subjects))
    else:
        print("\nNo subjects found!")
def main():
    while True:
        print("\nWelcome to the Student Data Organizer!")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
           print("invalid choice,try again")
           