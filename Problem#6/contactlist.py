def process_user_contacts(user_input):


    # Put word pairs into a dictionary
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    for i in range(len(splitUsers)):
        if(user_input[i] == contact_name):
            break
    print(user_input[i][(len(contact_name)+1)::])

    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")
    

    # Call the function to process user contacts
    process_user_contacts(user_input.split())
