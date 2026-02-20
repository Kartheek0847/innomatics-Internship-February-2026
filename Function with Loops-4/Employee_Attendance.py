def check_attendance(attendance_list):
    present_days = 0

    for day in attendance_list:
        if day == "P":
            present_days += 1

    percentage = (present_days / len(attendance_list)) * 100

    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


attendance = ["P", "P", "A", "P", "P", "A", "P"]

status = check_attendance(attendance)

print("Attendance Status:", status)