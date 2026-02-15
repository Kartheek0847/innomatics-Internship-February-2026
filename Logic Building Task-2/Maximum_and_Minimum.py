numbers = [45, 22, 89, 10, 66]
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("List:", numbers)
print("Max:", max_value)
print("Min:", min_value)
