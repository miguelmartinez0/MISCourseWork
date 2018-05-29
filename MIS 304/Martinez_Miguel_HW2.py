#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #2: gBooks Product Summary
#Due Date: Monday, September 12, 2016 at 5:00 P.M.
#Program Description: Program creates a product summary that includes total cost
#and total books received after offering different rates and free books with
#different membership types

#Prompt user for their name
user_name = input("Name: ")

#Prompt user for number of books purchased
books_purchased = int(input("Number of books purchased: "))

#Prompt user for membership type
member_type = input("Membership type (R for regular and P for premium): ")

#If R then offer upgrade
if member_type == "R":
    final_member = input("Would you like to upgrade to premium for $4.95 (Y or N)? ")
    #Upgrade, and thank
    if final_member == "Y":
        print("Thank you for upgrading to premium!")
    #Not upgrade, and thank
    else:
        print("Thank you for your interest!")
#Display thanks for already being premium
else:
    print("Thank you for being a premium member and for your continued support!")

#Create final_member variable for premium member
if member_type == "P":
    final_member = "Y"

#Print a blank line
print()

#Display customer's name
print("Customer's Name:", user_name)

#Display customer type if premium
if member_type == "P" or final_member== "Y":
    #Display that customer is premium
    print("Membership Type:", "Premium")
#Display the customer is regular
else:
    print("Membership Type: Regular")

#Calculate free books for regular
if final_member == "N" and member_type == "R":
    #Display books received if less than 8, no free book
    if books_purchased < 8:
        print("Number of Books Received:", books_purchased)
    #Give one free book
    elif books_purchased > 7 and books_purchased < 13:
        print("Number of Books Received:", (books_purchased + 1))
    #Give two free books
    elif books_purchased > 12:
        print("Number of Books Received:", (books_purchased + 2))
#Calculate free books for premium
else:
    #Display books received if less than 8, no free book
    if books_purchased < 6:
        print("Number of Books Received:", books_purchased)
    #Give one free book
    elif books_purchased > 5 and books_purchased < 10:
        print("Number of Books Received:", (books_purchased + 1))
    #Give two free books
    elif books_purchased > 10:
        print("Number of Books Received:", (books_purchased + 2))

#Calculate price of books for regular
if final_member == "N" and member_type == "R":
    pretax_price = (books_purchased * 12.95)
    #Display pretax price of books
    print("Pre-tax Price of Books: $", format(pretax_price, '.2f'), sep="")

#Calculate price of books for premium
else:
    pretax_price = (books_purchased * 11.49)
    #Display pretax price of books
    print("Pre-tax Price of Books: $", format(pretax_price, '.2f'), sep="")

#Calculate sales tax
sales_tax = pretax_price * 0.0825

#Display sales tax
print("Sales Tax: $", format(sales_tax, '.2f'), sep="")

#Create membership fee variable
if member_type == "R" and final_member == "Y":
    member_fee = 4.95
    #Display membership fee
    print("Membership Fee: $", format(member_fee, '.2f'), sep="")

#Calculate total with upgrade to premium
if member_type == "R" and final_member == "Y":
    #Add sales_tax, pretax_price and member_fee
    grand_total = sales_tax + pretax_price + member_fee
    #Display grand total
    print("Total Amount Due: $", format(grand_total, '.2f'), sep="")
#Calculate total without premium fee
else:
    grand_total = sales_tax + pretax_price
    #Display grand total
    print("Total Amount Due: $", format(grand_total, '.2f'), sep="")


    
    
