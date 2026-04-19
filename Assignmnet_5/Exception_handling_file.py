def read_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile opened successfully!\n")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist. Please che ck the filename.")

    except PermissionError:
        print("Error: Permission denied. You do not have access to read this file.")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")


read_file()