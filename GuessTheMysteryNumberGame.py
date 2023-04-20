#Gianni Salazar
#April 2, 2023
#This program will be a Guess the Mystery Number Game


from random import randint



def DisplayRules(ROUNDS):
    print(f"\nYou will be given {ROUNDS} chances to guess the Mystery Number.")
    print(f"Once you guess the Mystery Number correctly, YOU WIN!")
    print(f"\nGood Luck!\n")


def MysteryNumber():
    
    return randint(1,100)



def DisplayMenu():

    menuChoice = 0


    while menuChoice !=1 and menuChoice != 2 and menuChoice != 3:
        try:
            print("1)Play\n2)Rules\n3)Quit\n")
            menuChoice = int(input("Please select 1-3 from the Menu: "))
            if menuChoice <1 or menuChoice > 3:
                print("\n ERROR - Please type 1, 2, or 3 only to select an option from the Menu\n")
        except:
            print("Please enter a number")


    return menuChoice



def GetGuess():

    userGuess = 0

    while userGuess > 100 or userGuess < 1:

        try:
            userGuess = int(input("Enter your guess (1-100): "))

            if userGuess > 100 or userGuess < 1:
                print(f"\nYour guess must be between 1 - 100\n")

        except:
            print("\nPlease enter a number\n")
            
    return userGuess

                
def GuessWin(mysteryNumber, userGuess):
    print(mysteryNumber)
    if userGuess > mysteryNumber:
        print(f"\n----- {userGuess} is too High -----\n")

    elif userGuess < mysteryNumber:
        print(f"\n----- {userGuess} is too Low -----\n")

    elif userGuess == mysteryNumber:
        print("\nCongratulations! You guessed the Mystery Number")
        print("  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  ")
        print(" / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ")
        print("( C | o | n | g | r | a | t | u | l | a | t | i | o | n | s )")
        print(" \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ ")
                                        
               



    
def main():
    
    ROUNDS = 7

    results = playAgain = ""
    userGuess = menuChoice = mysteryNumber = 0

    print("*" * 40)
    print("Welcome to Guess the Mystery Number Game")
    print("*" * 40)

    while menuChoice != 3:

        menuChoice = DisplayMenu()

        if menuChoice == 1:
            
            
            mysteryNumber = MysteryNumber()

            for i in range(ROUNDS):
                print(f"\n***** Round {i+1} of {ROUNDS} *****\n")

                userGuess = GetGuess()

    

                GuessWin(mysteryNumber, userGuess)
                

                if userGuess == mysteryNumber:
                    print(f"\n\n\t\t\tYOU WON!\n")
                    break
                
            if userGuess != mysteryNumber:
                print(f"Sorry, You Lost. The Mystery Number was {mysteryNumber}")
                
            playAgain = input(f"\nWould you like to play again? (y/n): ").lower()
            print()

            if playAgain != "y":
                break
                    

        elif menuChoice == 2:

            DisplayRules(ROUNDS)

        else:
            print("\nThank you for playing Guess the Mystery Number!")

main()                

    































def main():
    mysteryNumber = MysteryNumber()
    print(mysteryNumber)


    
