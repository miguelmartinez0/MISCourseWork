#Program header goes here

#Declare constants
SANDWICH = 3.05
DELUXE_SANDWICH = 3.65
SPICY_SANDWICH = 3.29
NUGGETS_8PC = 3.05
MAX_MENU = 5
TAX_RATE = 0.0825

#Define main function
def main():
    #Declare list of items user will order
    item_list = []
    
    #Declare list of prices for items user ordered
    price_list = []

    #Display the menu
    menu()

    #Print a blank line
    print()

    #Ask user for all items they want to order
    #You MUST get all of the items the user wants to buy FIRST
    while item_number != MAX_MENU:
        ask_user_for_item()
        for item_number in ask_user_for_item:
            item_list.append (item_number)
    print(item_list) #Check to see if the list worked
    #After getting all items from the user, convert to individual prices
    #You MUST convert all items to prices - store the prices in a list
    index = 0



    #After converting items to prices, calculate the total price of all items
    #Use the prices in the list to calculate the total due




    #Calculate sales tax
    tax = total_price * TAX_RATE

    #Calculate final price
    final_price = total_price + tax

    #Print receipt
    #NEED TO PRINT NUMBER OF ITEMS ORDERED
    print("Thank you for ordering", "NEEDS TO BE CHANGED TO COUNT", "of our delicious food items.")
    print("Total price: $", format(total_price, ".2f"), sep="")
    print("Sales tax: $", format(tax, ".2f"), sep='')
    print("Total due: $", format(final_price, ".2f"), sep='')
    
#Define function to ask user for item to order
def ask_user_for_item():
    #Get item from user
    item_number = int(input("What item would you like to order? "))

    #Ensure item user entered is valid
    while item_is_invalid(item_number):
        #Prompt user again if item entered is invalid
        item_number = int(input("Invalid item. Please try again: "))        

    return item_number

#Define function to validate the item the user entered
def item_is_invalid(item_selected):
    #Determine whether item is in valid input range
    if item_selected < 1 or item_selected > MAX_MENU:
        #Item is invalid 
        invalid = True
    else:
        #Item is valid
        invalid = False

    return invalid

#Define menu function
def menu():
    print("Yummy sandwich menu")
    print("1. Chicken Sandwich\t\t$", SANDWICH, sep="")
    print("2. Deluxe Chicken Sandwich\t$", DELUXE_SANDWICH, sep="")
    print("3. Spicy Chicken Sandwich\t$", SPICY_SANDWICH, sep="")
    print("4. 8 pc Nuggets\t\t\t$", NUGGETS_8PC, sep="")
    print("5. Complete order")
    
#Call main function
main()
