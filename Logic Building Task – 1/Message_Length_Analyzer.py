
def analyze_messages(message_list):

    for message in message_list:
        # Calculate length of message
        length = len(message)

        # Print message length
        print(f"Message: '{message}'")
        print(f"Length : {length}")

        # Flag messages longer than 10 characters
        if length > 10:
            print("Status : ⚠️ Long message")
        else:
            print("Status : OK")

        print("-" * 40)  # Separator for clarity


def main():
    # Given list of messages
    messages = ["Hi", "Welcome to the platform", "OK"]

    # Analyze messages
    analyze_messages(messages)


# Program execution starts here
if __name__ == "__main__":
    main()
