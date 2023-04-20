# Gianni Salazar
# This program calculates the number of calories consumed by a customer
# based on the number of cookies the customer ate.


# Define main function
def main():
    # Declare constants
    # 40 cookies per bag
    # 10 servings per bag
    # 300 calories per serving
    COOKIES_PER_BAG = 40
    SERVINGS_PER_BAG = 10
    CALORIES_PER_SERVING = 272.25

    #Calculate calories per cookie CALORIES_PER_COOKIE = CALORIE_PER_SERVING / (COOKIES_PER_BAG / SERVINGS_PER_BAG)
    CALORIES_PER_COOKIE = CALORIES_PER_SERVING / (COOKIES_PER_BAG / SERVINGS_PER_BAG)
    
    # Declare and initialize variables
    # string to store user name
    userName = ""
    # whole var to store cookies eaten
    cookiesEaten = 0
    # real var to store calories consumed
    caloriesConsumed = 0.0
    
    # Display "WELCOME TO THE CALORIE COUNTER!!"
    print("WELCOME TO CALORIE COUNTER!!\n\n")
    # Prompt for name by displaying "Please enter your name:"
    userName = input("Please enter you name: ")
    # Prompt for cookies eaten by displaying "Please enter the number of cookies consumed:"
    # using the input alone always stores the answer as a string
    cookiesEaten = int(input("\nPlease enter the number of cookies consumed: "))  #"5"
    
    # Calculate calories consumed = cookies eaten * 75 calories
    caloriesConsumed = cookiesEaten * CALORIES_PER_COOKIE
    
    # Display calories consumed calliong the user by name
    print(f"Okay {userName}, you consumed {round(caloriesConsumed)} calories!")
    
    # Display Outro
    print("\n\nThank you for using my program!")
    
# Call or invoke the main function
main()
