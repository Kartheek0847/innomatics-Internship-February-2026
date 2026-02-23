def transaction_check(amount):
    limit = 50000

    if amount <= limit:
        status = "Approved"
    else:
        status = "Rejected"

    print("Transaction Amount:", amount)
    print("Transaction Status:", status)


transaction_check(60000)