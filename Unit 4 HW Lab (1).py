#Gianni Salazar
#March 19, 2023
#Snack Bar Menu progran for unit 4 assignment


#IMPORT LIBRARY
from time import sleep

def snackshack():

    #DECLARE CONSTANTS

    CHEESE_PIZZA = 1
    PEPPERONI_PIZZA = 2
    HOT_DOG = 3
    PRETZEL = 4
    BOTTLED_WATER = 5
    LEMONADE = 6
    EXIT = 7

    CHEESE_PIZZA_PRICE = 2.50
    PEPPERONI_PIZZA_PRICE = 2.50
    HOT_DOG_PRICE = 1.75
    PRETZEL_PRICE = 1.50
    BOTTLED_WATER_PRICE = 1.25
    LEMONADE_PRICE = 1.30


    TAX = 0.07


    #DECLARE AND INITIALIZE VARIABLES

    subtotal = 0.0
    grand_total = 0.0
    order = ""
    order_again = ""
    choice = ""
    
    #GREET USER
    print(f"Welcome to the Snack Shack".center(80))
    print()
    print("*" * 110)

    #GET THE NAME OF THE USER FOR ORDER
    userName = input("May I please have a name for the order?\n").capitalize()
    print(f"\nThank you {userName} here is our Menu:\n")

    #LOOP FOR ORDERING
    while choice != EXIT:
        #PROVIDE MENU
        print("-" * 20, "MENU", "-" * 20)
        print()
        print(f"[1] Slice of Cheese Pizza... ${CHEESE_PIZZA_PRICE:.2f}")
        sleep(.75)
        print(f"[2] Slice of Pepperoni Pizza... ${PEPPERONI_PIZZA_PRICE:.2f}")
        sleep(.75)
        print(f"[3] Hotdog... ${HOT_DOG_PRICE:.2f}")
        sleep(.75)
        print(f"[4] Pretzel... ${PRETZEL_PRICE:.2f}")
        sleep(.75)
        print(f"[5] Bottled Water... ${BOTTLED_WATER_PRICE:.2f}")
        sleep(.75)
        print(f"[6] Lemonade... ${LEMONADE_PRICE:.2f}")
        sleep(.75)
        print("[7] Exit")
        print()
        print()

        #GET INPUT FROM MENU CHOICE
        choice = int(input("Please enter the number of the item you would"
                           " like to order: "))

        #PROVIDE ERROR STATEMENT IF USER ENTERS INVALID INPUT
        if choice <= 0 or choice >= 7:
            price = 0.0
            print("\nInvalid menu choice. Please enter a number 1-6 to order, or enter 7 to exit.")

        #CREATE VARIABLE TO DISPLAY ORDER NAME AND SUBTOTAL
        if choice == CHEESE_PIZZA:
            order = "Cheese Pizza"
            price = CHEESE_PIZZA_PRICE
        elif choice == PEPPERONI_PIZZA:
            order = "Pepperoni Pizza"
            price = PEPPERONI_PIZZA_PRICE
        elif choice == HOT_DOG:
            order = "Hot Dog"
            price = HOT_DOG_PRICE
        elif choice == PRETZEL:
            order = "Pretzel"
            price = PRETZEL_PRICE
        elif choice == BOTTLED_WATER:
            order = "Bottled Water"
            price = BOTTLED_WATER_PRICE
        elif choice == LEMONADE:
            order = "Lemonade"
            price = LEMONADE_PRICE

            #CALCULATE SUBTOTAL
        subtotal += price
        #DISPLAY ITEM ADDED AND SUBTOTAL
        print(f"\n{order} has been added to your order. Your subtotal is now ${subtotal:.2f}\n")

    #CALCULATE ORDER TAX AND GRAND TOTAL
    orderTax = subtotal * TAX
    grandTotal = subtotal + orderTax

    #DISPLAY RECIEPT FOR CUSTOMER
    print()
    print("-" * 40)
    print(f"Order for {userName}:")
    print()
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${orderTax:.2f}")
    print(f"Grand Total : ${grandTotal:.2f}")
    print("-" * 40)
    print()
    #ASK USER IF AN ADDITONAL PERSON WILL BE ORDERING
    order_again = input("Would you like to place an order for another person? (yes or no): ").lower()
        
    if order_again == "no":
        print()
        print("Thank you for ordering at the Snack Shack! Hope to see you again!")
    elif order_again == "yes":
        print()
        print()
        snackshack()
        

        
    
        
                    
        





snackshack()














    
