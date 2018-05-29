#Get price from user
price = float(input("Please enter the item price: $"))

#Check to ensure a valid price
while price < 0:
    #Invalid data entered. Prompt user again.
    price = float(input("You cannot enter a negative price. Please try again: $"))

#Get quantity from user
quantity = int(input("Please enter the quantity sold: "))

#Check to ensure a valid quantity
while quantity < 1:
    #Invalid data entered. Prompt user again.
    quantity = int(input("Quantity sold must be positive. Please try again: "))

#Calculate total price with valid price and quantity
total_price = price * quantity

#Print total price
print("Total price is $", format(total_price, '.2f'), sep='')

print()

numbr = int(input("Please enter a positive number (-99 to stop): "))
count = 0
total = 0
            
while numbr != -99 and numbr > 0:
    total = total + numbr
    count = count + 1
    numbr = int(input("Please enter a positive number (-99 to stop): "))
print(count, "numbers were entered and total", total)

print()
               
number = 0
while number < 5:
    print ("Number is", number)
    number = number + 1

print()

number = int(input("Please enter a number: "))
product = number * 10

while product < 100:
    print (number, "times 10 is", product)
    number = int(input("Please enter a number: "))
    product = number * 10
