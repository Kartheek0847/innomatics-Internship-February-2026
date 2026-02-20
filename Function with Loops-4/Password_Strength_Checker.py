def check_password(password):
    if len(password) < 8:
        return "Weak Password"

    has_digit = False
    has_special = False
    special_chars = "@#$"

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch in special_chars:
            has_special = True

    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password"


user_password = input("Enter password: ")

print(check_password(user_password))