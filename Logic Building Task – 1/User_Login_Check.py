"""
Author: Karthik Chowdary

"""

def main():
    # Predefined valid credentials
    username = "admin"
    password = "1234"

    # Collect user input
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    # Validate credentials
    if entered_username == username and entered_password == password:
        print("Login Successful")
    else:
        print("Invalid Credentials")


# Entry point of the program
if __name__ == "__main__":
    main()
