def max_semester_marks():
    semesters = int(input("Enter no of semester: "))
    for sem in range(1, semesters + 1):
        subjects = int(input(f"Enter no of subjects in {sem} semester: "))
        marks = list(map(int, input(f"Marks obtained in semester {sem}: ").split()))
        if all(0 <= m <= 100 for m in marks):
            print(f"Maximum mark in {sem} semester: {max(marks)}")
        else:
            print("You have entered invalid mark.")

max_semester_marks()
