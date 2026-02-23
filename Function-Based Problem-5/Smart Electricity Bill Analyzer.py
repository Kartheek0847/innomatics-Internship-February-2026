def electricity_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + ((units - 100) * 5)
    else:
        bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    if bill < 500:
        usage = "Low Usage"
    elif bill <= 1500:
        usage = "Moderate Usage"
    else:
        usage = "High Usage"

    print("Total Bill:", bill)
    print("Usage Level:", usage)


electricity_bill(250)