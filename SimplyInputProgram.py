# Gianni Salazar
# This program will ask for a name and age and display them


# Define main function
def main():
    # Display Intro
    # The print function will display and move on
    print("Welcome To My Information Gathering Program!")

    # Prompt user for name
    # The input function displays to the screen and waits for user interaction
    # Never use an input function by itself, will always be variable = input
    name = input("Enter your name: ")
    # Prompt user for age
    age = input("Enter your age: ")
    
    # Display user name
    print("Name: "+ name)
    # Display user age
    print("Age:"+ age)

    # using concatenation (only between strings)
    print("Name:", name + ".")
    #Display user age
    print("Age: " + age)

    #This way uses f formatting which is the newest and best practice way
    print(f"Name: {name}")
    print(f"Age: {age}.")
    
    # Display outro
    print(f"Thank you {name} for using my program")

# Call the main function
main()

    
