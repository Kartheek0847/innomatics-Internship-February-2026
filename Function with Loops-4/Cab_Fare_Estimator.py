def calculate_fare(distance, peak):
    base_fare = 50
    fare = base_fare + (12 * distance)

    if peak == "yes":
        fare = fare + (fare * 0.25)

    return fare


while True:
    km = float(input("Enter distance in km: "))
    peak_hour = input("Is it peak hour? (yes/no): ")

    total_fare = calculate_fare(km, peak_hour.lower())

    print("Total Fare: ₹", total_fare)

    retry = input("Do you want to calculate again? (yes/no): ")
    if retry.lower() != "yes":
        break