def server_load(cpu_readings):
    total = 0

    for value in cpu_readings:
        total += value

    average = total / len(cpu_readings)

    if average < 50:
        status = "Normal"
    elif average <= 80:
        status = "Warning"
    else:
        status = "Critical"

    print("Average CPU Load:", int(average), "%")
    print("Server Status:", status)


server_load([45, 60, 70, 85, 90])