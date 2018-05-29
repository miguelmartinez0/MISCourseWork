#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Program Description: Program uses OO to allow customers to make purchases at a candy storye

#Import all files
import dessert
import candy
import cookie
import icecream
import sundae

#Estalblish variable names
CANDY = 1
COOKIE = 2
ICE_CREAM = 3
SUNDAE = 4
EXIT = 5

SALES_TAX = 0.0825
invoice = 0

#Define user defined function to print the menu
def print_menu():
    print("Dessert Menu")
    print("1.     Candy")
    print("2.     Cookie")
    print("3.     Ice Cream")
    print("4.     Sundae")
    print("5.     Exit")

#Define the user defined function to get the user's choice
def get_order():

    #Ask the user for their order
    order = int(input("What would you like to order #"))

    #Validate that the order number is valid
    while order < CANDY or order > EXIT:

        #Invalid entry. Try again.
        order = int(input("Order must be a number between 0-5. Please try again. #"))

    return order

#Define the user defined function to order candy
def order_candy(dessert_list):
    
    #Ask the user for whatever kind of candy they would like
    candy_kind = input("What kind of candy would you like? ")

    #Create a candy object with the new kind
    candy1 = candy.Candy("Candy", candy_kind)

    #Ask the user for the weight of the candy
    new_weight = float(input("How much, in pounds, would you like to purchase? "))

    #Validate that the weight entered is valid
    while new_weight <= 0:

        #Invalid weight entered. Try again.
        new_weight = float(input("Weight must be a positive number. Please try again. "))

    #Use the mututator to update the object's weight
    candy1.update_weight(new_weight)

    #Ask the user for the price per pound of the candy they want to purchase
    new_price = float(input("What is the candy's price per pound? $"))

    #Validate that the price per pound entered is valid
    while new_price <= 0:

        #Invalid price per pound entered. Try again.
        new_price = float(input("Price per pound must be positive. Please try again. $"))

    #Use the mutator to update the object's price per pound
    candy1.update_price_per_pound(new_price)

    #Add the dessert to the list
    dessert_list.append(candy1)
        
#Define the user defined function to order cookies
def order_cookies(dessert_list):

    #Ask the uder for whatever kind of cookie they would like
    cookie_kind = input("What kind of cookies would you like? ")
    
    #Create a cookie object
    cookie1 = cookie.Cookie("Cookie", cookie_kind)

    #Ask the user how many cookies they would like
    new_quantity = int(input("How many cookies would you like? "))

    #Validate that the number of cookies entered is correct
    while new_quantity <= 0:

        #Invalid quantity entered. Try again.
        new_quantity = int(input("Quantity must be positive. Please try again. "))

    #Use the mutator to update the object's quantity
    cookie1.update_quantity(new_quantity)

    #Ask the user for the price per dozen
    new_price = float(input("What is the price per dozen? $"))

    #Validate that the price per dozen is valid
    while new_price <= 0:

        #Invalid price entered. Try again.
        new_price = float(input("Price per dozen must be positive. Please try again. $"))

    #Use the mutator to update the object's price per dozen
    cookie1.update_price_per_dozen(new_price)

    #Add the dessert to the list
    dessert_list.append(cookie1)
    
#Define the user defined function to order ice cream
def order_ice_cream(dessert_list):

    #Ask the user what kind of ice cream they would like
    ice_cream_kind = input("What flavor of ice cream would you like? ")
    
    #Create an ice cream object
    icecream1 = icecream.IceCream("Ice Cream", ice_cream_kind)

    #Ask the user what size of ice cream they would like
    new_size = input("What ice cream size would you like? ")

    #Validate that the size is correct
    while new_size != "S" and new_size != "M" and new_size != "L":

        #Invalid size entered. Try again.
        new_size = input("Size must be either 'S', 'M', or 'L'. Please try again. ")

    #Use the mutator to change the size of the object
    icecream1.update_size(new_size)

    #Add the dessert to the list
    dessert_list.append(icecream1)

#Define the user defined function to order sundaes
def order_sundae(dessert_list):

    #Ask the user for what kind of sundae they would like
    sundae_kind = input("What flavor would you like the ice cream for your sundae? ")

    #Create a sundae object
    sundae1 = sundae.Sundae("Sundae", sundae_kind)

    #Ask the user what size of sundae they would like
    new_size = input("What sundae size would you like? ")

    #Validate that the size is correct
    while new_size != "S" and new_size != "M" and new_size != "L":

        #Invalid size entered. Try again.
        new_size = input("Size must be either 'S', 'M', or 'L'. Please try again. ")

    #Use the mutator to update the sundae size
    sundae1.update_size(new_size)

    #Ask the user how many toppings they would like
    new_toppings = int(input("How many toppings would you like? "))

    #Validate that the number of toppings entered is valid
    while new_toppings <= 0:

        #Invalid number entered. Try again.
        new_toppings = int(input("Number must be positive. Please try again. "))

    #Use the mutator to change the number of toppings
    sundae1.update_toppings(new_toppings)

    #Add the dessert to the list
    dessert_list.append(sundae1)
    
#Define the main function
def main():

    #Create an invoice check to not allow the user to see the invoice
    invoice = 0

    #Initialize the subtotal
    subtotal = 0
    
    #Create a list for the different desserts to be added
    dessert_list = []
    
    #Call on the function to print the product menu
    print_menu()

    #Call on the function to get the user's order
    order_number = get_order()

    #If user never orders anything then don't prompt them to order more items
    if order_number == EXIT:

        #Print message thanking them for visiting
        print("Thank you so much for visiting Serendipity 3!")

    #Allow the user to order multiple items
    while order_number != EXIT:

        #User orders candy
        if order_number == CANDY:

            #Call on the function to order candy
            order_candy(dessert_list)

        #User orders cookie
        if order_number == COOKIE:

            #Call on the function to order cookies
            order_cookies(dessert_list)

        #User orders ice cream
        if order_number == ICE_CREAM:

            #Call on the function to order ice cream
            order_ice_cream(dessert_list)

        #User orders sundae
        if order_number == SUNDAE:

            #Call on the function to order a sundae
            order_sundae(dessert_list)

        #Stop them from seeing the invoice
        invoice = invoice + 1

        #Ask the user for their next order item
        order_number = get_order()

    #Prevent the customer from seeing the invoice
    if invoice != 0:

        #Print an empty line between the user input and invoice
        print()
        
        #Print the items in the list for the invoice
        for dessert in dessert_list:
            print (dessert)

            #Calculate the subtotal cost of one item
            cost = dessert.calculate_cost()

            #Convert the cost into a float
            cost = float(cost)
            
            #Add the costs of all the items
            subtotal = subtotal + cost

        #Calculate the sales tax
        tax = subtotal * SALES_TAX
        
        #Calculate the grand total
        total = subtotal + tax

        #Print the total amount of desserts
        print("Total Desserts Purchased: ", len(dessert_list))

        #Print the subtotal
        print ("Subtotal: $", format(subtotal, '.2f'), sep='')

        #Print the tax
        print ("Sales Tax: $", format(tax, '.2f'), sep='')

        #Print the grand total
        print ("Total Due: $", format(total, '.2f'), sep='')

#Call the main function
main()
