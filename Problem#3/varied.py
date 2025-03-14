def process_input(input_string):
    # Split into separate strings
    splitNumbers = input_string.split()
    list = []
    # Convert strings to floats
    for i in range(len(splitNumbers)):
        list.append(float(splitNumbers[i]))
    
    largest = max(list)
    average = sum(list) / len(list)
    # Get max and average
    max_value = largest
    average_value = average
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
