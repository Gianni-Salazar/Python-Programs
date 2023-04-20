# Gianni Salazar
# April 10, 2023
# This program will read in a name and some course grades to a list
# and display a gpa and write it out to a file

def main():
    #Declare and intialize string var for user name and file name
    userName = fileName = ""
    # int for grade count
    count = 0
    # float for gpa
    gpa = 0.0
    # List to store grade and name
    courseGrades = []
    nameList = []
    
    # Display intro
    print("Welcome to my program!/n/n")

    
    # Prompt for file name
    fileName = input("Please enter the name of the file (inc ext): ")
    
    # get and store info from file
    with open(fileName, "r") as infile:
        userName = infile.readline().strip()
        courseGrades = infile.readline().split(",") #"99,88.5,77,100,98"

        print(userName)
        print(courseGrades)

    for i in range (len(courseGrades)):
        courseGrades[i] = float(courseGrades[i]) #99
        
    # Display name, grades and gpa back to user
    gpa = sum(courseGrades) / len(courseGrades)


    nameList = userName.split() #["Gianni","Salazar"]

    print(f"First Name:\t{nameList[0]}")
    print(f"Last Name:\t{nameList[1]}")
    print("Your grades in order are:")
    print(sorted(courseGrades))
    print(f"GPA:\t{gpa:.1f}")
    
    
    # write new info out to file
    with open("gpaout.txt", "w") as outfile:
        print(f"First Name:\t{nameList[0]}", file=outfile)
        print(f"Last Name:\t{nameList[1]}", file=outfile)
        print(f"GPA:\t{gpa:.1f}", file=outfile)

        for grade in courseGrades:
            count += 1
            print(f"Grade {count}: {grade}",file=outfile)



    print("Bye")



main()
