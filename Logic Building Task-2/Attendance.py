attendance = ["P", "P", "A", "P", "P"]
present_count = 0
for day in attendance:
    if day == "P":
        present_count += 1
total_days = len(attendance)
percentage = (present_count / total_days) * 100
print("Attendance Percentage:", percentage)
