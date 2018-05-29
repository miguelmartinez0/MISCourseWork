#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #1: Product Summary
#Due Date: Monday, September 5, 2016 at 5:00 P.M.
#Program Description: Program creates a product summary that includes total profit,
#,Percentage profit, etc., based on user inputed variables, such as price and cost.

#Prompt and read product name from user
product_name= input("Product Name: ")

#Prompt and read product price from user
product_price= input("Product Price: $")

#Prompt and read product cost from user
product_cost= input("Product Cost: $")

#Prompt and read quantity of t5he product sold from user
quantity_sold= input("Quantity Sold: ")

#Change product_price variable from str to float
product_price= float(product_price)

#Change product_cost variable from str to float
product_cost= float(product_cost)

#Change quantity_sold variable from str to float
quantity_sold= int(quantity_sold)

#Display blank line between input and output
print()

#Display the name of the product
print("Product Name:", product_name)

#Calculate total revenue 
total_revenue= product_price * quantity_sold

#Display total revenue
print("Total Revenue:$", format(total_revenue, '.2f'))

#Calculate total cost
total_cost= product_cost * quantity_sold

#Display total cost
print("Total Cost:$", format(total_cost, '.2f'))

#Display quantity sold
print("Quantity Sold:", quantity_sold)

#Calculate total profit
total_profit= total_revenue - total_cost

#Display total profit
print("Total Profit:$", format(total_profit, '.2f'))

#Calculate percentage profit
percentage_profit= total_profit / total_revenue * 100

#Display percentage profit
print("Percentage Profit:", format(percentage_profit, '.2f'), "%")

