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
        try:
            #prompt the user for tempGrade and validate it is between 0 - 100
            tempGrade = float(input("Enter a grade (0-100): "))
            if tempGrade < 0 or tempGrade > 100:
                print("Invalid. Grade must be between 0 and 100.\n")
        except ValueError:
            print("You must enter a number")
        #return tempGrade
    return tempGrade


#return type: 1 float for average
#parameters: 3 floats
#purpose: This function calculates and returns the average of the
#three numbers that are passed to the function
def CalcAverage(num1, num2, num3):
    #since nothing needs to be stored locally you can do the math directly
    #in the return statement
    return (num1 + num2 + num3)/ 3
    




#return type: 1 string - letter grade
#parameters: 1 float for average
#purpose: To return a letter grade based on average
def LetterGrade(avg):
    #Create constants to store grade values 90 - 100 A etc
    A = 90
    B = 80
    C = 70
    D = 60

    
    #Use selection structure to return letter based on average
    if avg >= A:
        return "A"
    elif avg >= B:
        return "B"
    elif avg >= C:
        return "C"
    elif avg >= D:
        return "D"
    else:
        return "F"



#return type: none
#parameters: 3 strings - first name, last name, letter
#            1 int for age, 1 float for average
#purpose: This function displays the first and last name, age, average,
#         and letter grade that are passed to the function

def DisplayInfo(fName, lName, letter, age, avg):
    #Display info
    print(f"{'First Name:':<20}{fName:>10}")
    print(f"{'Last Name:':<20}{lName:>10}")
    print(f"{'Age:':<20}{age:>10}")
    print(f"{'Average:':<20}{avg:>10}")
    print(f"{'Letter Grade:':<20}{letter:>10}")
    




def main():
    #Declare variables
    #Name is a local variable to name
    firstName = lastName = ltrGrde = ""
    age = 0
    grade1 = grade2 = grade3 = average = 0.0
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

    #Get 3 grades from user
    grade1 = GetGrade()
    grade2 = GetGrade()
    grade3 = GetGrade()
    #Calculate average
    average = round(CalcAverage(grade1, grade2, grade3))
    
    #Find letter grade
    ltrGrade = LetterGrade(average)
    
    #Display info
    DisplayInfo(firstName, lastName, ltrGrade, age, average)
    
    #Display outro
    print(f"The average of 10, 20 and 32 = {CalcAverage(10,20,32)}")




#Call or invoke the main function

main()
