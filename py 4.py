data = []
total_elements = 0
average_value = 0

print("Welcome to the Data Analyzer and Transformer Program")

def calculate_average(numbers):
    """Calculate the average of the dataset."""
    return sum(numbers) / len(numbers)

def find_duplicates(numbers):
    """Find duplicate values in the dataset."""
    duplicates = []
    for value in numbers:
        if numbers.count(value) > 1 and value not in duplicates:
            duplicates.append(value)
    return duplicates

def find_unique(numbers):
    """Find unique values in the dataset."""
    unique_values = []
    for value in numbers:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

def display_summary(*args, **kwargs):
    """Display dataset summary using *args and **kwargs."""
    print("\nData Summary:")
    print("- Total elements:", len(args))
    print("- Minimum value:", min(args))
    print("- Maximum value:", max(args))
    print("- Sum of all values:", sum(args))
    average = calculate_average(args)
    print("- Average value:", round(average, 2))
    for key, value in kwargs.items():
        print("-", key, ":", value)

def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_data(numbers, threshold):
    """Filter data using lambda and filter()."""
    return list(filter(lambda x: x >= threshold, numbers))

def update_global(numbers):
    """Update global dataset summary."""
    global total_elements
    global average_value
    total_elements = len(numbers)
    average_value = calculate_average(numbers)

def get_statistics(numbers):
    """Return minimum, maximum, sum and average values."""
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = calculate_average(numbers)
    return minimum, maximum, total, average

def display_2d(matrix):
    """Display a 2D list in grid format."""
    print("\n2D Array:")
    for row in matrix:
        print(" ".join(map(str, row)))

def get_user_data(numbers):
    """Convert 2D list into a 1D list."""
    user_data = []
    for row in numbers:
        user_data.extend(row)
    return user_data

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    choice = input("\nPlease enter your choice: ")

    if choice == "1":
        print("\nChoose Data Type:")
        print("1. 1D Array")
        print("2. 2D Array")
        data_type = input("\nPlease enter your choice: ")

        if data_type == "1":
            values = input("\nEnter data for a 1D array (separated by spaces): ")
            data = list(map(int, values.split()))
            print("\nData has been stored successfully!")

        elif data_type == "2":
            rows = int(input("\nEnter number of rows: "))
            columns = int(input("Enter number of columns: "))
            data = []

            for i in range(rows):
                values = input("Enter values for row " + str(i + 1) + " (separated by spaces): ")
                row = list(map(int, values.split()))

                if len(row) == columns:
                    data.append(row)
                else:
                    print("Please enter exactly", columns, "values.")
                    break

            if len(data) == rows:
                print("\n2D data has been stored successfully!")
                display_2d(data)

        else:
            print("\nInvalid data type choice!")

    elif choice == "2":
        if len(data) == 0:
            print("\nPlease enter your data first!")
        else:
            if type(data[0]) == list:
                numbers = get_user_data(data)
            else:
                numbers = data

            unique_values = find_unique(numbers)
            duplicate_values = find_duplicates(numbers)

            display_summary(*numbers,
                unique_values=unique_values,
                duplicate_values=duplicate_values)

    elif choice == "3":
        number = int(input("\nEnter a number to calculate its factorial: "))

        if number < 0:
            print("\nFactorial is not possible for negative numbers.")
        else:
            result = factorial(number)
            print("\nFactorial of", number, "is:", result)

    elif choice == "4":
        if len(data) == 0:
            print("\nPlease enter your data first!")
        else:
            if type(data[0]) == list:
                numbers = get_user_data(data)
            else:
                numbers = data

            threshold = int(input("\nEnter a threshold value to filter out data above this value: "))
            filtered_data = filter_data(numbers, threshold)

            print("\nFiltered Data (values >= " + str(threshold) + "):")
            print(*filtered_data, sep=", ")

    elif choice == "5":
        if len(data) == 0:
            print("\nPlease enter your data first!")
        else:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            sort_choice = input("\nEnter your choice: ")

            if type(data[0]) != list:
                if sort_choice == "1":
                    data.sort()
                    print("\nSorted Data in Ascending Order:")
                    print(*data, sep=", ")

                elif sort_choice == "2":
                    data.sort(reverse=True)
                    print("\nSorted Data in Descending Order:")
                    print(*data, sep=", ")

                else:
                    print("\nInvalid sorting choice!")

            else:
                if sort_choice == "1":
                    sorted_data = sorted(data, key=lambda row: row[0])
                    print("\n2D Data in Ascending Order:")
                    display_2d(sorted_data)

                elif sort_choice == "2":
                    sorted_data = sorted(data, key=lambda row: row[0], reverse=True)
                    print("\n2D Data in Descending Order:")
                    display_2d(sorted_data)

                else:
                    print("\nInvalid sorting choice!")

    elif choice == "6":
        if len(data) == 0:
            print("\nPlease enter your data first!")
        else:
            if type(data[0]) == list:
                numbers = get_user_data(data)
            else:
                numbers = data

            minimum, maximum, total, average = get_statistics(numbers)
            update_global(numbers)

            print("\nDataset Statistics:")
            print("- Minimum value:", minimum)
            print("- Maximum value:", maximum)
            print("- Sum of all values:", total)
            print("- Average value:", round(average, 2))

    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 7.")
