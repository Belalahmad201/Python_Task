
marks = input("Enter student marks: ")


if not marks.isdigit():
    print("Invalid input! Please enter numeric value.")
else:
    marks = int(marks)

    # Checking grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Result
    print("Grade:", grade)

    # Pass or Fail
    if marks >= 50:
        print("Status: Passed")
    else:
        print("Status: Failed")