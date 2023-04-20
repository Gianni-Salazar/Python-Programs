# Sherry Cox
# Jan 31, 2023
# This program will get user input for name, hours worked, and hourly pay
# then calculate and display the weekly gross pay and annual gross pay

import math

# This style pre-loads the sleep function into the interpreter - it executes a bit faster
from time import sleep

# Define a main function
def main():
    # Declare a constant WEEKS to store 52 weeks in a year
    YEAR = 52
    
    # Declare and initialize string var to store username
    userName = ""
    # whole var to store hours worked
    hoursWorked = 0
    # real vars to store hourly pay, weekly gross pay, annual pay
    hourlyPay = grossPay = annualPay = 0.0

    # You can initialize variables of dif data types on 1 line
    # But it is messy
    # userName, hoursWorked, hourlyPay = "", 0, 0.0
    
    # Display Intro
    print("WELCOME TO MY GROSS PAY CALCULATOR!\n\n")

    # use the sleep function for a pause
    # becasue I wrote from time import sleep above I do not repeat the word time here
    sleep(.5)
    
    # Prompt for users name
    userName = input("Please enter your name: ")
    # Pause for .5 sec
    sleep(1)
    # Prompt for number of hours worked
    # hoursWorked = int(input("\nPlease enter the number of hours you worked in a week: "))
    # This way will not work because input only takes 1 argument
    # hoursWorked = int(input("\nOkay", userName, "Please enter the number of hours you worked in a week: "))
    # We used to use concatenation to make it 1 argument
    # hoursWorked = int(input("\nOkay " + userName + " Please enter the number of hours you worked in a week: "))
    hoursWorked = int(input(f"\nOkay {userName} Please enter the number of hours you worked in a week: "))

    # Prompt for hourly pay
    hourlyPay = float(input("Please enter your hourly pay: $"))
    
    # Calculate weekly gross Pay = hourly pay * hours worked
    grossPay = hourlyPay * hoursWorked
    # Set annual pay = weekly gross pay * WEEKS
    annualPay = grossPay * YEAR
    sleep(.5)
    
    # Display weekly gross pay and annual pay to user
    print("\nYour weekly gross pay is: $", grossPay)  # $ 1200.0
    
    # This is an old style - Do not use it please
    print("%s makes %d per hour, so makes $%0.02f" % (userName, hourlyPay, grossPay))
    
    #This is better but still not good - also have to convert float to a string for it to work
    print("\nYour weekly gross pay is: $"+ str(grossPay))   #$1200.0
    
    #This uses the format function
    print("\nYour weekly gross pay is: $", format(grossPay, ",.2f"))
    
    #This uses the .format method
    print("\nYour weekly gross pay is: ${:,.2f}".format(grossPay))
    
    #Best practice is f formatting
    print(f"\nYour weekly gross pay is: ${grossPay:,.2f}")   # $1,200.00
    print(f"\nYour annual gross pay is: ${annualPay:,.2f}")
    sleep(.5)


    # Selection structure
    # If user makes 50,000+ a year display "You can live alone on that salary"
    # If user makes under 50,000 display "Sorry, you don't make enough yet to live alone"
    if annualPay >= 50000:
        print("You can live alone on that salary")
    else:
        print("Sorry, you don't make enough yet to live alone")
    



    
    # Display square root of 64
    print(f"The square root of 64 is {math.sqrt(64)}")
    sleep(.5)
    
    # Display outro
    print(f"\nThank you {userName} for using my program!")


# Call main function
main()













