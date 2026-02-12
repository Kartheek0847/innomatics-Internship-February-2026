def count_errors(logs):
    
    # Use built-in count method
    return logs.count("ERROR")


def main():
    # Given system logs
    logs = ["INFO", "ERROR", "WARNING", "ERROR"]

    # Calculate total errors
    total_error_count = count_errors(logs)

    # Print result clearly
    print("===== Log Analysis Report =====")
    print("Total Logs   :", len(logs))
    print("Error Count  :", total_error_count)


# Program starts here
if __name__ == "__main__":
    main()
