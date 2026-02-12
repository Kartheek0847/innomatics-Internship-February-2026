def analyze_results(scores):
    pass_count = 0
    fail_count = 0
    for mark in scores:
        if mark >= 50:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count


def main():
    # Given marks list
    marks = [45, 78, 90, 33, 60]

    # Analyze results
    passed, failed = analyze_results(marks)

    # Print final result clearly
    print("===== Student Result Analysis =====")
    print(f"Total Students : {len(marks)}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")


# Program execution starts here
if __name__ == "__main__":
    main()
