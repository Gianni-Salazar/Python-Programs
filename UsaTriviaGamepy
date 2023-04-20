# Gianni Salazar
# USA Trivia Game


from time import sleep

# Define main function
def main():
    
    # Welcome message
    print("Welcome to USA Trivia".center(100))
    print()
    print("*" * 100)
    print()
          
    # Get user's name
    userName = input("Please enter your name: ")
    print()
    
    # Get user's age
    userAge = int(input("Please enter your age: "))
    
    # Validate user's age
    if userAge < 18:
        print(f"I am sorry {userName}, but you must be 18 or order to play")
        return


    # Start the game
    start_Game(userName)

def start_Game(userName):

    # Set up trivia questions and answers
    questions = ["What is the capital of the United States?", "Which is the smallest state"
    " in the US?", "Which state is the coldest state?", "What is the most populous city"
    " in the US?"]

    answers = ["Washington D.C.", "Rhode Island", "Alaska", "New York City"]

    
    # Show the menu
    print("Menu:")
    print("[1] Play USA Trivia")
    print("[2] View High Scores")
    print("[3] Quit")
    print()
          
    # Get the user's choice
    choice = int(input("Enter you choice: "))
    print()
    # Use a multi-selection structure to do something different for each option
    if choice == 1:
        print("Let's play some USA Trivia \U0001F603\n")
        score = 0
    # Ask each question and check the user's answer
        for i in range (len(questions)):
            print("Question " + str(i+1) + ": " + questions[i])
            answer = input("Enter your answer: ")
            print()
            if answer.lower() == answers[i].lower():
                print("Correct! \U0001F44D\n")
                score += 1
            else:
                print("Incorrect \U0001F615, the correct answer is " + answers[i])
                print()
    # Pause 2 seconds between questions
            sleep(2)
    # Show final score
        print("\nYour final score is: " + str(score) + " out of " + str(len(questions)))
    elif choice == 2:
        print("\n\U0001F605 I don't know how to do that yet... Awkward...")
    elif choice == 3:
        print(f"\nThank you for playing {userName}! \U0001F3C6")
        return
    else:
        print("\nInvalid choice, please try again.\n")
        start_Game(userName)
        
    # Ask the user if they want to play again
    start_Game_over = input("\nWould you like to play again? [yes or no]: ").lower()
    
    # Use a nested selection structure to validate the user's input
    if start_Game_over == "yes":
        print("\nNew game coming up\n")
        start_Game(userName)
    elif start_Game_over == "no":
        print(f"\nThanks for playing {userName}!")
    else:
        print("\nInput invalid, please enter yes or no.\n")
        start_Game(userName)


# Call the main fucntion
main()
