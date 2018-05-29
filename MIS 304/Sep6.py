#Simple Decision Structure

#Prompt and read user's age
age = int(input("How old are you? "))

#Compare age entered to the legal age to vote
if age >= 18:
    #Print old enough
    print("Congrats! You are old enought to vote.")
else:
    #Print wait and milk
    print("You're not old enough to vote. Keep drinking your milk.")

#Print election coming up
print("There is a presidential election this November.")

#Print a blank line
print()

#Prompt and read number
number = int(input("Please enter a number: "))

#Determine the absolute value of the number
if number < 0:
    #Multiply by -1
    number = number * -1

#Print absolute value of the number
print("The absolute value is ", number, ".", sep="")

#Print a blank line
print()

#Prompt and read hours worked
hours_worked = float(input("How many hours did you work? "))

#Prompt and read pay rate
pay_rate = float(input("What is your pay rate? "))

#Determine if hours worked is overtime
if hours_worked <= 40:
    #Calculate total pay
    total_pay = hours_worked * pay_rate
else:
    #Calculate overtime total pay
    total_pay = (hours_worked - 40) * pay_rate * 1.5 + 40 * pay_rate

#Display total pay
print("Your total pay is $", format(total_pay, '.2f'), sep="")
                 
