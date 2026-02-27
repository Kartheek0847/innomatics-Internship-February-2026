def parking_management(capacity, logs):
    parked = 0
    peak_usage = 0

    for entry in logs:
        if entry == "IN":
            parked += 1
        elif entry == "OUT" and parked > 0:
            parked -= 1

        if parked > peak_usage:
            peak_usage = parked

    print("Currently Parked Vehicles:", parked)

    if parked > capacity:
        print("Parking Status: Full - Alert")
    else:
        print("Parking Status: Available")


parking_management(50, ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"])