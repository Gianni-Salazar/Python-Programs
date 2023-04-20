# Gianni Salazar
# Feb 13, 2023
# This program is a multi-way decision. And a nested decision
# This program will display an insurance premium on an age input

# Define main function
def main():
    


    # Declare constants for insurance premiums
    # 1000 for 35 or under, 1500 for 36 - 59
    # Cut off age of 35 and 59
    YOUNGINSCOSTNONSMOKER = 1000
    YOUNGINSCOSTSMOKER = 2000
    MIDINSCOSTNONSMOKER = 1500
    MIDINSCOSTSMOKER = 2500
    OLDINSCOSTNONSMOKER = 2000
    OLDINSCOSTSMOKER = 3000
    CUTOFFAGEYOUNG = 35
    CUTOFFAGEMID = 59

    # Declare and intialize string var for name
    # and whole var for user age
    userNAME = smoke = ""
    userAGE = 0
    
    # Display Intro
    print("Welcome to the Insurance Quote Program\n")
    
    # Prompt for name
    userName = input("Please enter your name: ")
    # Prompt for age
    userAge = int(input(f"Please enter your age {userName}: "))

    # Outer selection structure
    if userAge >= 18:
        # Prompt user if they smoke
        smoker = input("Do you smoke, yes or no? ")
        
        # Display premium by age
        # A multi-way decision has only 1 if, as many elifs as needed,
        # and only 1 else
        # If condition in the if is true the body of the if will execute
        # If the condition in the if is not true the interpreter will move on to
        # the elif and check that condition
        # If the condition in the elif is true the body of the elif will execute
        # This will continue for as
        if userAge <= CUTOFFAGEYOUNG and smoker == "yes":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTSMOKER:,.2f}")
        elif userAge <= CUTOFFAGEYOUNG and smoker == "no":
            print(f"\nYour insurance premium is ${YOUNGINSCOSTNONSMOKER:,.2f}")
        elif userAge <= CUTOFFAGEMID and smoker == "yes":
            print(f"\nYour insurance premium is ${MIDINSCOSTSMOKER:,.2f}")
        elif userAge <= CUTOFFAGEMID and smoker == "no":
            print(f"\nYour insurance premium is ${MIDINSCOSTNONSMOKER:,.2f}")
        elif userAge > CUTOFFAGEMID and smoker == "yes":
            print(f"\nYour insurance premium is ${OLDINSCOSTSMOKER:,.2f}")
        elif userAge > CUTOFFAGEMID and smoker == "no":
            print(f"\nYour insurance premium is ${OLDINSCOSTNONSMOKER:,.2f}")
        else:
            print("You must answer yes or no")
        # Display Outro
        print(f"\nThank you {userName} for your business!")

    #This else goes with the outer if
    else:
        print("You must be 18 or over to buy insurnce")


# Call main function
main()





















