# Gianni Salazar
# February 20, 2023
# This program presents an option with 4 possible states
# then tells the capital of their choice

from time import sleep


# Define main function
def main():
    # Create constants to store state capitals
    # PA is Harrisburg
    # SC is Columbia
    # GA is Atlanta
    # FL is Tallahassee
    PA = "Harrisburg"
    SC = "Columbia"
    GA = "Atlanta"
    FL = "Tallahassee"
    
    # Declare and initialize variables
    # strings for name and menuchoice
    userName = menuChoice = ""
    playAgain = "yes"
    
    
    # Display Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")
    print("WELCOME TO THE CAPITAL PROGRAM!!\n".center(60,"-"))

    # pause for half a second
    # because I wrote from time sleep above I do not repeat the word time here
    sleep(.5)
    
    # Prompt user for name
    userName = input("\nFirst, let me get your name: ").capitalize()
    
    # Greet user by name
    print(f"Hello {userName}, ready to play....")
    # print(f"Hello {userName.capitalize()}, ready to play....")
    # print("Hello", userName.capitalize(), "ready to play....")



    # Outer loop
    while playAgain == "yes":
        menuChoice = ""

    
        # Conditional loops must be evaluated as true the first time the code runs
        #Seeding the loop
        while menuChoice != "A" and menuChoice != "B" and menuChoice != "C" and menuChoice != "D":




            # Display state options "A) PA B) SC C) GA D) FL"
            print("\nPlease choose from the following menu: ")
            print("A) PA \nB) SC \nC) GA \nD) FL")
        
        # Prompt for menuchoice
            menuChoice = input("\nPlease enter your choice: ").upper() # "a" - "A"
            # menuChoice = menuChoice.upper() #"A"
            
            # Selection Structure to determine which capital to display to user
            if menuChoice == "A":
                print(f"The capital of Pennsylvania is {PA}")
            elif menuChoice == "B":
                 print(f"The capital of South Carolina is {SC}")
            elif menuChoice == "C":
                print(f"The capital of Georgia is {GA}")
            elif menuChoice == "D":
                print(f"The capital of Florida is {FL}")
            else:
                print("You must enter a letter from the choices above")

        playAgain = input("Do you want to play again? ")
        
    # Display outro
    print(f"\nThank you {userName} for playing!".title())


        


    print(" _____ ____  ____  ____    ____ ___  _ _____")
    print("/  __//  _ \/  _ \/  _ \  /  _ \\  \///  __/")
    print("| |  _| / \|| / \|| | \|  | | // \  / |  \  ")
    print("| |_//| \_/|| \_/|| |_/|  | |_\\ / /  |  /_ ")
    print(" \____\\____/\____/\____/  \____//_/   \____\ ")
        


main()
# Call main function
