#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #8: The COOP
#Due Date: Monday, November 7, 2016 at 5:00 P.M.
#Program Description: Program uses OO to allow customers to make purchases and returns

#Import item info
import iteminfo

#Import payment info
import paymentinfo

#Establish variables for the program
SHORTS = 32
SHIRT = 83
SOCKS = 39

SHORTS_PRICE = 18.97
SHIRT_PRICE = 29.95
SOCKS_PRICE = 2.99

#Define user defined function to print the product menu
def print_product_menu():
    print("ID     Item      Price")
    print("32     Shorts    $18.97")
    print("83     Shirt     $29.95")
    print("39     Socks     $2.99")

#Define user defined function to get the transcation type and validate
def get_transaction_type():

    #Ask the user for their transaction type
    item_mode = input("Would you like to make a purchase or return? ('Buy' or 'Return') ")

    #Validate that the transaction type is valid
    while item_mode != 'Buy' and item_mode != 'Return':

        #Invalid entry. Try again.
        item_mode = input("Transcation type must be either 'Buy' or 'Return'. Please try again. ")

    return item_mode

#Define user defined function to get the item id of the item in question
def get_item_id():

    #Ask the user for ID number of the item
    item_num = int(input("What is the ID number of the item in question? "))

    #Validate that the ID number is correct
    while item_num != SHORTS and item_num != SHIRT and item_num != SOCKS:

        #Invalid entry. Try again.
        item_num = int(input("Invalid ID number. Please try again. "))

    return item_num

#Define user defined function to get the item quantity
def get_item_quantity():

    #Ask the user for the item quantity
    item_qty = int(input("How many of the item? "))

    #Validate that the item quantity is positive
    while item_qty < 1:

        #Invalid entry. Try again.
        item_qty = int(input("Quantity must be positive. Please try again. "))

    return item_qty

#Define user defined function to determine the item name
def determine_item_name(item_num):

    #Determine the item name for shorts
    if item_num == SHORTS:
        item_name = "Shorts"
        return item_name

    #Determine the item name for a shirt
    elif item_num == SHIRT:
        item_name = "Shirt"
        return item_name

    #Determine the item name for socks
    elif item_num == SOCKS:
        item_name = "Socks"
        return item_name

#Define user defined function to determine the item price
def determine_item_price(item_num):

    #Determine the item price for shorts
    if item_num == SHORTS:
        item_price = SHORTS_PRICE
        return item_price

    #Determine the item price for a shirt
    elif item_num == SHIRT:
        item_price = SHIRT_PRICE
        return item_price

    #Determine the item price for socks
    elif item_num == SOCKS:
        item_price = SOCKS_PRICE
        return item_price

#Define the main function
def main():

    #Create an item
    item_info1 = iteminfo.ItemInfo()

    #Create a payment
    payment_info1 = paymentinfo.PaymentInfo()
    
    #Call on the function to print the menu
    print_product_menu()

    #Call on the function to get the transcation type
    new_mode = get_transaction_type()

    #Use the mutator to change the transcation type
    item_info1.update_mode(new_mode)

    #Call on the function to get the ID number from the user
    new_item_num = get_item_id()

    #Use the mutator to change the item ID
    item_info1.set_item_num(new_item_num)

    #Call on the function to get the item quantity
    new_qty = get_item_quantity()

    #Use the mutator to change the item quantity
    item_info1.update_qty(new_qty)

    #Call on the function to determine the item name
    new_name = determine_item_name(new_item_num)

    #Use the mutator to change the item name
    item_info1.set_item_name(new_name)

    #Call on the function to determine the item price
    new_price = determine_item_price(new_item_num)

    #Use the mutator to change the item price
    item_info1.set_price(new_price)

    #Ask for user's name
    new_name = input("What is the the name on the credit card used to make the purchase/return? ")

    #Use the mutator to change the credit card name
    payment_info1.set_name(new_name)

    #Ask for the credit card type
    new_type = input("Credit Card Type (MC, VISA, or AMEX): ")

    #Validate that the credit card type is allowed
    while new_type != "MC" and new_type != "VISA" and new_type != "AMEX":

        #Invalid entry. Try again
        new_type = input("CC Type must be either 'MC', 'VISA', or 'AMEX'. Please try agin. ")

    #Use the mutator to change the credit card type
    payment_info1.update_cc_type(new_type)

    #Ask for the credit card number
    new_cc_num = input("Credit Card Number: ")

    #Validate that the credit card number entered is valid for MC and VISA
    while (new_type == "MC" or new_type == "VISA") and len(new_cc_num) != 16:
        #Invalid credit card number entered. Try again.
        new_cc_num = input("CC Number must be 16 digits. Please try again. ")

    #Validate that the credit card number entered is valid for AMEX
    while new_type == "AMEX" and len(new_cc_num) != 15:
        #Invalid credit card number entered. Try again.
        new_cc_num = input("CC Number must be 15 digits. Please try again. ")

    #Use the mutator to change the credit card type
    payment_info1.update_cc_number(new_cc_num)

    #Ask for the credit card expiration date
    new_exp_date = input("Credit Card Expiration Date: ")

    #Validate that the credit card expiration date is valid
    while new_exp_date[2] != '/' and new_exp_date[0:2].isdigit() and new_exp_date[3:5].isdigit():
        #Invalid expiration date entered. Try again.
        new_exp_date = input("Expiration date must follow the format of 'MM/YY'. Please try again. ")
        
    #Use the mutator to change the credit card expiration date
    payment_info1.update_exp_date(new_exp_date)

    #Print the total
    print ("Item Info: ", item_info1.get_item_num(), item_info1.get_item_name())
    print ("Quantity: ", item_info1.get_qty())
    print ("Total: ",item_info1.calculate_total())
    print ("Credit Card Name: ",payment_info1.get_name())
    print ("Credit Card Type: ", payment_info1.get_cc_type())
    print ("Credit Card Number: ", payment_info1.mask_cc_num())
    print ("Credit Card Expiration Date: ", payment_info1.get_cc_exp_date())       
    
#Call the main function
main()
