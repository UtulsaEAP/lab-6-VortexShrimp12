def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    while(user_input != "quit"):
        print("eating " + tokens[1] + " " + tokens[0]+ " a day keeps you happy and healthy.")
        user_input = input()
        tokens = user_input.split()
        if(tokens[0] == "quit"):
            break

    

if __name__ == "__main__":
    food_input()
