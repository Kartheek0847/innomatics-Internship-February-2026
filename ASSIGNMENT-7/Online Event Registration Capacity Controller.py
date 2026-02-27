def registration_controller(capacity, registrations):
    if registrations > capacity:
        confirmed = capacity
        waitlisted = registrations - capacity
        status = "Closed"
    else:
        confirmed = registrations
        waitlisted = 0
        status = "Open"

    print("Confirmed Registrations:", confirmed)
    print("Waitlisted Users:", waitlisted)
    print("Registration Status:", status)


registration_controller(100, 105)