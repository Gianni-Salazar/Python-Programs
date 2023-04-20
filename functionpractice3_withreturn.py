#Gianni Salazar
#March 20, 2023
#This program demonstrates non-value returning function


from jenslibrary import GetAge, GetName

#function definitions
#return type: none
#Parametrs: none
#Purpose: This function displays an intro
def DisplayIntro():
    #Display Intro
    print("WELCOME TO MY PROGRAM!!\n\n")


#return type:
#parameter: 1 String for a name
#Purpose: This function displays a greeting to the user by name
def DisplayGreeting(tempName):
    #Display hello name
    print(f"Hello {tempName}")

    
#return: 1 float for a grade
#parameters: none
#purpose: This function prompts the user for a grade and validates that
#grade is between 0 and 100
def GetGrade():
    #Declare a local variable
    #float tempGrade
    tempGrade = -1.0

    while tempGrade < 0 or tempGrade > 100:
        #prompt the user for tempGrade and validate it is between 0 - 100
        tempGrade = float(input("Enter a grade (0-100): "))
        if tempGrade < 0 or tempGrade > 100:
            print("Invalid. Grade must be between 0 and 100.\n")
        
        #return tempGrade
    return tempGrade






def main():
    #Declare variables
    #Name is a local variable to name
    firstName = lastName = ""
    age = 0
    
    #Display Intro
    #print("WELCOME TO MY PROGRAM!!\n\n")
    #call or invoke display intro function
    DisplayIntro()


     
    #Prompt for name
    firstName, lastName = GetName()

    
    #Display hello name
    #print(f"Hello {name}")
    #Call greeting function
    #Can only use the local variables to pass to the function
    #Here name is the actual parameter or argument
    DisplayGreeting(firstName)

    #Get the age
    age = GetAge() #must store the return value in a local variable

    #display age
    print(f"Age: {age}")

    #You can call a function directly in a print
    #print(f"Age: {GetAge()}")




#Call or invoke the main function

