def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    output = []
    string = ""
    for i in range (len(input_list)):
        if((input_list[i] >= min_val) and (input_list[i] <= max_val)):
            output.append(input_list[i])
            string += str(input_list[i]) + ","
    print(string, end=' ')




if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    filter_list = user_input.split()
    filteredList = []
    for i in range(len(filter_list)):
        filteredList.append(int(filter_list[i]))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    tokens = user_input.split()
    max_and_min = []
    for i in range(len(tokens)):
        max_and_min.append(int(tokens[i]))
    min_val = max_and_min[0]
    max_val = max_and_min[1]

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(filteredList, min_val, max_val)
   
