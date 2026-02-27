def theatre_occupancy(total_seats, booked_seats):
    booked_count = len(booked_seats)
    occupancy = (booked_count / total_seats) * 100

    print("Occupancy:", int(occupancy), "%")

    if occupancy == 100:
        print("Show Status: Housefull")
    elif occupancy >= 75:
        print("Show Status: Almost Full")
    else:
        print("Show Status: Seats Available")


bookings = [1] * 150
theatre_occupancy(200, bookings)