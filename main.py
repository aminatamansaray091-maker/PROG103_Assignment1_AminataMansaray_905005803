


while True:
    print("\n--- Student Grading System ---")


    name = input("Enter student name (at least 3 characters): ")
    while len(name) < 3 or name.isdigit():
        print("Name must be at least 3 characters long and must not contain numbers")
        name = input("Enter student name (at least 3 characters): ")


    student_id = input("Enter student ID (must be 5 digits):")
    while len(student_id) <10 or not student_id.isdigit():
        print("Student ID must be exactly 10 digits.")
        student_id = input("Enter student ID (must be 10 digits): ")


    score = float(input(f"Enter {name}'s score (0-100): "))


    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student: {name} | ID: {student_id} | Grade: {grade}")

    # Ask if user wants to continue
    choice = input("Do you want to grade another student? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting the grading system. Goodbye!")
        break
