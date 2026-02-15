employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}
highest_employee = ""
highest_salary = 0
for name in employees:
    if employees[name] > highest_salary:
        highest_salary = employees[name]
        highest_employee = name
print("Highest Salary:", highest_employee, "-", highest_salary)
