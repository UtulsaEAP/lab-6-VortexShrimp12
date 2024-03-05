def calculate_car_wash_price(service_choice1, service_choice2):

    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
   
   #type your code here 
    for i in range(len(services)):
        if(services[i] == service_choice1):
            total += services[i]
    print(base_wash)
    print(service_choice1)
    print(total)
    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
