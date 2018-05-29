# Program comments go here

#Prompt user for hours worked
hours_worked = input("Please enter hours worked: ")

#Prompt user for pay rate
pay_rate = input("Please enter your pay rate: ")

#Convert strings to float
hours_worked = float(hours_worked)
pay_rate = float(pay_rate)

#Calculate total pay
total_pay = hours_worked * pay_rate                 

#Print everything
print("Hours worked:", hours_worked)
print("Pay rate:", pay_rate)
print("Total pay:", total_pay)

