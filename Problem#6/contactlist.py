def process_user_contacts(user_input):
    split = user_input
    print(split)

    # Put word pairs into a dictionary
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    for i in range(len(user_input)):
        if(split[i] == contact_name):
            break

    print(split[i+1])

    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input.split())
