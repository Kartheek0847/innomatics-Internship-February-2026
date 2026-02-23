def attendance_eligibility(attendance):
    present = 0

    for day in attendance:
        if day == "P":
            present += 1

    percentage = (present / len(attendance)) * 100

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Attendance Percentage:", percentage)
    print("Exam Eligibility:", status)
attendance_eligibility(["P", "P", "A", "P", "P"])