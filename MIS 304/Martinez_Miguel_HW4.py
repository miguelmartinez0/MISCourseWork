#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #4:
#Due Date: Monday, October 3, 2016 at 5:00 P.M.
#Program Description: Through user-defined functions, this program allows for users to
#go order their items and receive a receipt with a grand total and applicable discounts.

#Define function that prints menu
def print_menu ():
    print ("GRAPEFRUIT ELECTRONICS")
    print ("1. gPod                 $249")
    print ("2. gPad Pro             $599")
    print ("3. gPhone 7 Plus        $769")
    print ("4. gMac               $1,499")
    print ("5. gMacBook Pro       $1,999")
    print ("6. gMac Pro           $2,999")
    print ("7. Grapefruit Watch     $299")
    print ("8. Complete order")

#Establish total quantity
total_quantity = 0

#Start with a total price
total_price = 0

#Start with a discount
discount = 0

#Start with a pre-tax price
pre_tax_price = 0

#Start with a sales tax
sales_tax = 0

#Start with a final price
final_price = 0

#Create a varible to allow customers to order more
order_flag = 0

#Define function that allows customers to order
def order_item ():
    
    #Prompt user for their item number
    number = int(input("What is the item number for your order? #"))

    return(number)

#Define function that allows customer to input quantity of order
def ask_quantity ():
    
    #Prompt the quantity ordered for the item number
    quantity = int(input("How much of the item would you like ? "))

    return(quantity)

#Define function that validates item number
def validate_item_number (number):

    #Check to ensure a valid item number
    while number < 1 or number > 8:

        #Invalid number entered. Prompt user again.
        number = int(input("Number must be between 1 and 8. Please try again: #"))

    return(number)

#Define function that validates the quantity entered
def validate_item_quantity (quantity):

    #Check to ensure a valid item quantity
    while quantity < 0:

        #Invalid quantity entered. Prompt user again.
        quantity = int(input("Quantity must be positive. Please try again: "))

    return(quantity)

#Define function that determines item price and quantity
def determine_item_price (number, quantity, total_price, total_quantity):

    #Calculate price for gpod
    if  number == 1:
        total_price = quantity * 249 + total_price

    #Calculate price for gpad pro
    elif number == 2:
        total_price = quantity * 599 + total_price

    #Calculate price for gphone7 plus
    elif number == 3:
        total_price = quantity * 769 + total_price

    #Calculate price for gmac
    elif number == 4:
        total_price = quantity * 1499 + total_price

    #Calculate price for gmacbook pro
    elif number == 5:
        total_price = quantity * 1999 + total_price

    #Calculate price for gmac pro
    elif number == 6:
        total_price = quantity * 2999 + total_price

    #Calculate price for grapefruit watch
    elif number == 7:
        total_price = quantity * 299 + total_price

    #Calculate the total number of items ordered
    total_quantity = quantity + total_quantity
    
    return(total_price, total_quantity)

#Define function that calculates bulk discount percentage
def determine_discount (discount, total_price, total_quantity):

    #Calculate discount for orders larger than 15
    if total_quantity > 15:
        discount = total_price * 0.25

    #Calculate discount for orders between 10 and 15
    if total_quantity > 9 and total_quantity < 16:
        discount = total_price * 0.20

    #Calculate discount for orders between 5 and 9
    if total_quantity > 4 and total_quantity < 10:
        discount = total_price * 0.15

    #Calculate pre-tax price
    pre_tax_price = total_price - discount

    return(discount, pre_tax_price)

#Define function that calculates sales tax
def calculate_tax (pre_tax_price):

    #Calculate sales tax
    sales_tax = pre_tax_price * 0.0825

    return (sales_tax)

#Define function that calculates final price
def calculate_final_price (pre_tax_price, sales_tax):

    #Calculate final price
    final_price = pre_tax_price + sales_tax

    return (final_price)

#Define function that prints the receipt
def print_receipt (user_name, fnl_price, final_item, discount_price, pre_tax_price, sales_tax, final_price):

    #Print receipt shoud one be needed
    if fnl_price != 0 and final_item != 0:

        #Print user name
        print ("Customer's Name", user_name)

        #Print total price
        print ("Total Price: $", format(fnl_price, '.2f'), sep='')

        #Print total quantity
        print ("Total Quantity: ", final_item, sep='')

        #Print discount percentage for orders larger than 15
        if final_item > 15:
            print ("Discount Amount: 25%")
        
        #Print discount percentage for orders between 10 and 15    
        elif final_item > 9 and final_item < 16:
            print ("Discount Amount: 20%")

        #Print discount percentage for orders between 5 and 9
        elif final_item > 4 and final_item < 10:
            print ("Discount Amount: 15%")

        #Print discount amount, if one exists
        if discount_price != 0:
            print ("Discount Amount: $", format(discount_price, '.2f'), sep='')

        #Print pre-tax price, if one exists
        if discount_price != 0:
            print ("Final Price: $", format(pre_tax_price, '.2f'), sep='')

        #Print sales tax
        print ("Sales Tax: $", format(sales_tax, '.2f'), sep='')

        #Print total due
        print ("Total Due: $", format(final_price, '.2f'), sep='')

    #Print thank you message for not ordering anything
    else:
        print("Thank you for shopping with us!")
    
#Define main function
def main ():
    
    #Call the function to print menu for customer to see
    print_menu()

    #Print blank line between menu and user input
    print()
    
    #Prompt user for their name
    user_name = input ("Name: ")

    #Call the function to allow customer to order
    item_number = order_item()

    #Call the function to validate item number
    valid_item_number = validate_item_number (item_number)

    #Call the function to allow a customer to input item quantity
    item_quantity = ask_quantity ()

    #Call the function to validate valid item quantity
    valid_quantity = validate_item_quantity (item_quantity)

    #Call the function to determine item price
    (fnl_price, final_item) = determine_item_price (valid_item_number, valid_quantity, total_price, total_quantity)

    #Call the function to determine discount
    (discount_price, pre_tax_price) = determine_discount (discount, fnl_price, final_item)

    #Call the function to calculate sales tax
    sales_tax = calculate_tax (pre_tax_price)

    #Call the function to calculate final price
    final_price = calculate_final_price (pre_tax_price, sales_tax)

    #Print blank line between user input and receipt
    print()

    #Call the function to print the receipt
    print_receipt (user_name, fnl_price, final_item, discount_price, pre_tax_price, sales_tax, final_price)
    
#Call main function to run program
main()
