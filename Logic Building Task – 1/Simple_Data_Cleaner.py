def clean_names(name_list):
   

    cleaned_list = []

    for name in name_list:
        # Remove leading and trailing spaces
        trimmed_name = name.strip()

        # Convert to lowercase
        formatted_name = trimmed_name.lower()

        # Add cleaned name to new list
        cleaned_list.append(formatted_name)

    return cleaned_list


def main():
    # Original list of names
    names = [" Alice ", "bob", " CHARLIE "]

    result = clean_names(names)
    print("Original Names :", names)
    print("Cleaned Names  :", result)

if __name__ == "__main__":
    main()
