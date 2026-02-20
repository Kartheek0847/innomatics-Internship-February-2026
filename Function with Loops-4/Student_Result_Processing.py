def process_result(marks):
    total = 0
    
    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 50:
        return "Pass"
    else:
        return "Fail"


student_marks = [60, 55, 70, 45]

result = process_result(student_marks)

print("Result:", result)