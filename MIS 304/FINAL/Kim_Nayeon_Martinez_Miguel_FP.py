#Author: Nayeon Kim, Miguel Martinez Cano
#Homework Number and Name: Final project
#Due Date: 12/16/16 at 5:00 P.M
#Program Description: Main file 

#Import Inventory file
INVENTORY_FILE = "Inventory.txt"

#Create the Updated Inventory File
UPDATED_INVENTORY = "UpdatedInventory.txt"

#Establish sentinels
END = 0

#GLOBAL CONSTANT
TAX = 0.0825

#Import classes
import inventory
import transactionitem

#Define function to process inventory file
def process_file():

    #Create empty dictionary
    inventory_dict = {}
    
    #Open inventory data
    inventory_data = open(INVENTORY_FILE, "r")

    #Read data from file
    for line in inventory_data:

        #Split item
        values = line.split(",")

        #Store information in separate variable
        item_id = values[0]
        name = values[1]
        quantity = int(values[2])
        price = float(values[3])

        #Create an instance
        inventory_item = inventory.Inventory(item_id, name, quantity, price)

        #Add item to dictionary
        inventory_dict[item_id] = inventory_item

    #Close file
    inventory_data.close()

    #Return dictionary
    return inventory_dict

#define function to print menu
def print_menu(inventory_dict):

    #Print header
    print("ID", '\t', 'Item', '\t', '\t', 'Price', '\t', "Qty Available")

    #For loop to print all inventory items
    for value in inventory_dict:

        print(inventory_dict[value])

    #Print sentinel choice
    print('Enter 0 when finished')
    print()

#Define function to get item id from the user
def get_item_id(inventory_dict):

    #Create empty list of keys
    key_list = []

    #For loop to add keys from dictionary to the key list
    for value in inventory_dict:

        #Change to int and add
        key = int(value)
        key_list.append(key)

    #Ask the user what they would like to order
    choice = int(input("What is the ID of the item? "))

    #Validate the user's choice
    while choice != END and choice not in key_list:

        #Invalid item choice. Try again
        choice = int(input("Item ID must be either 0 or in the menu. Please try again. "))

    #Return the choice
    return choice

#Define function to print invoice
def print_invoice(transaction_list):

    #Initialize total
    total = 0

    #For loop to run through all items returned/purchased
    for items in transaction_list:
        print(items)
        price = items.calc_cost()
        total = total + price

    print('Item total: $', format(total,'.2f'), sep='')
    print('Tax: $', format((total*TAX),'.2f'), sep='')
    print('Total Due: $', format(total + (total*TAX), '.2f'), sep='')

#Define function to write the output file
def write_output(ID, name, qty, price, updated_inventory):

        #Write the output file
        updated_inventory.write(ID + ',' + name + ',' + qty + ',' + price + '\n')
  
#Define main function
def main():

    #Initialize the item count
    item_count = 0
    
    #Call function to process file
    inventory_dict = process_file()

    #Call the function to print the menu
    print_menu(inventory_dict)
    
    #Call function to get item id from user
    choice = get_item_id(inventory_dict)

    #Create an empty dictionary for the transaction items
    transaction_list = []

    #Allow the user to order multiple items
    while choice != END:

        #Ask the user if they would like to order or return it
        decision = input("Woud you like to return or purchase that item? (R or P) ")

        #Validate the decision
        while decision != "R" and decision != "P":

            #Invalid input. Prompt user to try again.
            decision = input("Must be either 'R' or 'P'. Please try again. ")

        #Ask the user how many of the item they would like to return or purchase
        quantity = int(input("What is the quantity of this item? "))

        #Create variables for object
        item_object = inventory_dict[str(choice)]
        item_name = item_object.get_name()
        item_price = item_object.get_stock()
        
        #Validate that the quantiy can be purchased
        if decision == "P":
            while quantity <= 0 or quantity > item_object.get_stock():

                #Invalid quantity. Try again.
                quantity = int(input("Quantity must be positive and less than the quantity available. Try again. "))
            
        #Validate that a positive quantity can be returned
        if decision == "R":
            while quantity <= 0:

                #Invalid quantity. Try again.
                quantity = int(input("Quantity must be positive in order to be returned. Try again. "))
        
        #Create an new object for the transaction item
        transaction = transactionitem.TransactionItem()

        #Calculate the cost if a return is made
        if decision == "R":
            item_price = float(-1 * item_object.get_price())

        #Calculate the cost if a purchase is made
        elif decision == "P":
            item_price = float(item_object.get_price())
        
        #Use the mutators to update the object
        transaction.set_id(choice)
        transaction.set_name(item_name)
        transaction.set_qty(quantity)
        transaction.set_price(item_price)

        #Add the transaction to the transaction list
        transaction_list.append(transaction)

        #Update the quantity of the inventory in the dictionary for a return       
        if decision == "R":
            inventory_dict[str(choice)].restock(quantity)

        #Update the quantity of the inventory in the dictionary for a purchase
        elif decision == "P":
            inventory_dict[str(choice)].purchase(quantity)

        #Update the item count
        item_count = item_count + 1

        #Print a blank line between every order
        print()

        #Ask the user for their next order
        print_menu(inventory_dict)
        choice = get_item_id(inventory_dict)

    #Print the invoice if something is ever puchased
    if item_count != END:

        #Call function to print invoice
        print_invoice(transaction_list)

        #Create the updated inventory file
        updated_inventory = open(UPDATED_INVENTORY, 'w')

        #Call on the for loop to write the output file
        for values in inventory_dict:

            item_object = inventory_dict[values]

            #Create the variable to be written on the output file
            final_ID = str(item_object.get_id())
            final_name = str(item_object.get_name())
            final_qty = str(item_object.get_stock())
            final_price = str(item_object.get_price())

            #Call on the function to write the output file
            write_output(final_ID, final_name, final_qty, final_price, updated_inventory)

    #Print a thank you message if nothing is ever purchased
    if item_count == END:

        #Print a thank you message
        print("Thank you for visiting us!")
    
#Call main
main()

