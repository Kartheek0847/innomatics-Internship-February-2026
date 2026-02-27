def delivery_time(distance, traffic, weather):
    # base time calculation
    time = distance * 5

    # traffic delay
    if traffic == "High":
        time += 15
    elif traffic == "Medium":
        time += 8

    # weather delay
    if weather == "Rainy":
        time += 10
    elif weather == "Storm":
        time += 20

    print("Estimated Delivery Time:", time, "minutes")


delivery_time(8, "High", "Rainy")