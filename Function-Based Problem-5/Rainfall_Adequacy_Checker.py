def rainfall_checker(rainfall_data, required_level):
    total = 0

    for value in rainfall_data:
        total += value

    average = total / len(rainfall_data)

    if average >= required_level:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"

    print("Average Rainfall:", int(average))
    print("Rainfall Status:", status)


rainfall_checker([70, 75, 68, 76], 70)