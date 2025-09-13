while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!\n")
    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:\n")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:\n")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

    elif choice == 3:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:\n")
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * i)

    elif choice == 4:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total += num
        print(f"\nSum of all numbers from {start} to {end} is: {total}")

    elif choice == 5:
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice, please try again!")
