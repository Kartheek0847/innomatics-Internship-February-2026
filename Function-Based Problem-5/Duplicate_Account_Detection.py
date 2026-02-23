def detect_duplicate_accounts(usernames):
    if len(usernames) != len(set(usernames)):
        print("Duplicate Accounts Found: Yes")
    else:
        print("Duplicate Accounts Found: No")


users = ["user1", "user2", "user1", "user3"]
detect_duplicate_accounts(users)