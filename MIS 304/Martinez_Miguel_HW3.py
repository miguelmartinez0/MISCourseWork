#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #3: Local BBQ Restaraunt
#Due Date: Monday, September 19, 2016 at 5:00 P.M.
#Program Description: Program creates a product summary for a customer's total
#cost and total meat purchased after receiving different items and quantities

#Print menu for user to chose items to purchase from
print("MENU ITEMS                PRICES")
print("MEAT")
print("1. Brisket – Extra Lean   $8.69 per 1/2 lb.")
print("2. Brisket – Moist        $8.89 per 1/2 lb.")
print()
print("SIDE ITEMS")
print("3. Cole slaw              $2.29 sm $8.29 lg")
print("4. Potato salad           $2.19 sm $8.09 lg")
print("5. Complete my order")

#Set up menu prices
brisket_xtra_lean = 17.38
brisket_moist = 17.78
cole_slaw_sm = 2.29
cole_slaw_lg = 8.29
potato_salad_sm = 2.19
potato_sald_lg = 8.09

#Establish total meat
total_meat = 0

#Establish total sides
total_side = 0

#Establish meat price
meat_price = 0

#Establish side price
side_price = 0

#Print blank line between menu and user input data
print()

#Prompt user for their name
customer_name = input("Name: ")

#Prompt user for their item number 
item_number = int(input("What is the item number for your order? #"))

#Allow user to order multiple items
while item_number != 5:

    #Check to ensure a valid item number
    while item_number < 0 or item_number > 5:
    
        #Invalid number entered. Prompt user again.
        item_number = int(input("Number must be between 1 and 5. Please try again: #"))
    
    #Prompt the total pounds purchased for item number
    if item_number > 0 and item_number < 3:
        quantity = float(input("How many pounds of the item would you like to purchase? "))

        #Check to ensure a valid quantity entered
        while quantity < 0:
        
            #Invalid quantity entered. Prompt user again.
            quantity = float(input("Quantity must be positive. Please try again: "))

            #Setup total weight of meat
            total_meat = quantity + total_meat

            #Calculate pre-tax price of Brisket Extra-lean
            if item_number == 1:
                meat_price = quantity * 17.38 + meat_price

            #Caluclate pre-tax price of Brisket Moist
            elif item_number == 2:
                meat_price = quantity * 17.78 + meat_price

        #Allow the user to order more food
        if item_number == 1 or item_number == 2:
            item_number = int(input("What else would you like to order? #"))
        
        
    #Prompt the user for the size of the item number
    elif item_number > 2 and item_number < 5:
    
        side_size = input("What is the size of the side item you would like to purchase (Sm or Lg)?")
        #Check to ensure a valid size entered
        while side_size != "Sm" and side_size != "Lg":
            #if either side is true, it is true
        
            #Invalid size entered. Prompt user again.
            side_size = input("Size must be either Sm or Lg. Please try again: ")
        
        #Prompt the amount purchased for each side
        side_quantity = int(input("How many of that side would you like? "))
        #Check to ensure a valid quantity entered.
        while side_quantity < 1:
        
            #Invalid quantity entered. Prompt user again.
            side_quantity = int(input("Quantity must be positive. Please try again: "))
                                  
    
    #User is done with their order
    if item_number == 5 and total_meat != 0 or item_number == 5 and total_side != 0:

        #Print a blank line
        print()

        #Display customer's name
        print("Customer's Name: ", customer_name)

        #Display total meat ordered
        print("Total meat: ", total_meat)

        #Display total sides ordered
        print("Total sides: ", total_side)

        #Display pre_tax price


        #Calculate sales tax
        sales_tax = pre_tax * 0.825

        #Display sales tax
        print("Sales tax: $", format(sales_tax, '.2f'), sep='')

        #Calculate final total
        final_total = pre_tax + sales_tax

        #Display final total
        print("Total due: $", format(final_total, '.2f'), sep='')

#User orders nothing and receives no product summary
if item_number == 5 and total_meat == 0 or item_number == 5 or total_side == 0:
    print("Thank you for shopping with us!")
    
