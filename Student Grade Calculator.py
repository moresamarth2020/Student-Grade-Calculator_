def grade_calculator():
    print("----- STUDENT GRADE CALCULATOR -----\n")

    student_name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    total_marks = 0

    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total_marks += marks

    percentage = total_marks / subjects

    if percentage >= 85:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 55:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n----- RESULT -----")
    print("Student Name:", student_name)
    print("Total Marks:", total_marks)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)

grade_calculator()
