def process_and_print(input_string):
      # Split into separate strings
    split = input_string.split()
    list = []
    for i in range(len(split)):
        if(float(split[i]) < 0):
            list.append(int(split[i]))

    # Convert strings to integers and filter out negative values
    list.sort(reverse = True)
    string = ""
    for i in range(len(list)):
        string += str(list[i]) + " "
                   
    print(string+ "\n")

    # Sort integers in reverse order
  
    # Print sorted integers
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
