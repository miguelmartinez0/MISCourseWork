#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #6: Employee Benefits
#Due Date: Monday, October 17, 2016 at 5:00 P.M.
#Program Description: This program reads data from a file and creates an output file
# based off the data in the input file using lists and a tuple

#Rename the input file for the program
EMPLOYEE_FILE = "EmployeeData.txt"

#Name the output file with the employee benefits
DATA_FILE = "EmployeeSummaryData.txt"

#Define main function
def main ():
       
    #Call the function to read the input file
    employee_data_tuple = readdata ()

    #Call the function to create a list for the employees' names
    employee_name_list = make_names_list (employee_data_tuple)

    #Calculate the total number of employees
    employee_size = len (employee_name_list)
    
    #Call the function to create a list for the employees' salaries
    employee_salary_list = make_salary_list (employee_data_tuple)

    #Call the function to create a list for the employees' life insurance
    employee_life_list = make_life_insurance_list (employee_data_tuple)

    #Call the function to create a list for the employees' health insurance
    employee_health_list = make_health_insurance_list (employee_data_tuple)

    #Call the function to calculate 401K contributions
    employee_401K_list = calculate_401K_contribution (employee_salary_list)

    #Call the function to calculate life insurance contriubtions
    employee_life_contribution_list = calculate_life_insurance_contribution (employee_life_list, employee_salary_list)

    #Call the function to calculate health insurance contributions
    employee_health_contribution_list = calculate_health_insurance_contribution (employee_health_list)

    #Call the function to calculate total contributions
    employee_total_contribution_list = calculate_total_benefits (employee_401K_list, employee_life_contribution_list, employee_health_contribution_list, employee_size)

    #Call the function to calculate salary total
    salary_total = calculate_all_totals (employee_salary_list)
    
    #Call the function to calculate 401K total
    e401K_total = calculate_all_totals (employee_401K_list)
    
    #Call the function to calculate life insurance total
    life_total = calculate_all_totals (employee_life_contribution_list)
    
    #Call the function to calculate health insurance total
    health_total = calculate_all_totals (employee_health_contribution_list)
    
    #Call the function to calculate final total
    total_total = calculate_all_totals (employee_total_contribution_list)

    #Call the function to print the program summary
    print_program_summary = print_summary (employee_size, salary_total, total_total, e401K_total, life_total, health_total)

    #Open the output file
    output_file = open(DATA_FILE, "w")
    
    #Call the function to write the output file
    write_output_file  (employee_name_list, employee_salary_list, employee_total_contribution_list, employee_size, output_file)

#Define function that reads data from EmployeeData.txt
def readdata ():

    #Try to open the input file and read it
    try:
        #Read the input file
        employee_data = open(EMPLOYEE_FILE, "r")

        #Create a list for all of the data
        employee_data_list = []

        #Read the file for all data
        for employee in employee_data:

            #Strip the new lines from the file
            data = employee.rstrip ('\n')

            #Read the data onto the list
            employee_data_list.append(data)

        #Convert the list into a tuple
        employee_data_tuple = tuple (employee_data_list)

        #Return the employee data tuple
        return employee_data_tuple

    #File is unable to be found
    except FileNotFoundError:

        #Print message saying that file cannot be found
        print ("ERROR! Could not find EmployeeData.txt.")

        #Stop running the code
        import sys
        sys.exit()

    #File has an error in the data
    except ValueError:

        #Print message saying there is an error with the data
        print ("Error! The input file does not contain valid data.")

        #Stop running the code
        import sys
        sys.exit()

    #Exception error
    except Exception as err:

        #Print error
        print (err)

        #Stop running the code
        import sys
        sys.exit()

#Define function that creates a list for the employees' names
def make_names_list (employee_data_tuple):

    #Add the employees' names into the list from the tuple
    name_list = employee_data_tuple [0::4]

    #Return the name list
    return (name_list)
    
#Define function that creates a list for the employees' salaries
def make_salary_list (employee_data_tuple):

    #Add the employees' names into the list from the tuple
    salary_list = employee_data_tuple [1::4]

    #Create a employee salary list with floats
    employees_salary = []

    #Create a loop to convert string list into integer list
    for num in salary_list:

        #Convert the strings into integers
        num = float (num)

        #Append the float salaries into the list
        employees_salary.append(num)

    #Return the salary_list
    return (employees_salary)
    
#Define function that creates a list for the employees' life insurance
def make_life_insurance_list (employee_data_tuple):

    #Add the employees' names into the list from the tuple
    life_list = employee_data_tuple [2::4]

    #Return the life_list
    return (life_list)
    
#Define function that creates a list for the employees' health insurance
def make_health_insurance_list (employee_data_tuple):

    #Add the employees' names into the list from the tuple
    health_list = employee_data_tuple [3::4]

    #Return the health_list
    return (health_list)

#Define function that calculates 401K contributions
def calculate_401K_contribution (employees_salary):

    #Create new list for the 401K contributions
    e401K_list = []

    #Create a loop to add data into the 401K contribtuions list
    for num in employees_salary:

        #Calculate 401K contributions
        e401K = format(num * 0.05, '.2f')

        #Convert the contributions into floats
        e401K = float (e401K)

        #Add the 401K contributions into the list
        e401K_list.append(e401K)

    #Return 401K list
    return (e401K_list)

#Define function that calculates life insurance cost
def calculate_life_insurance_contribution (life_list, employees_salary):

    #Create a new list for the life insurance contributions
    life_contribution_list = []

    #Establish an index to multiply the salary
    index = 0

    #Create a loop to add data into the life insurance contributions list
    for value in life_list:

        #If they opt for life insurance
        if value == "Y":

            #Calculate life insurance contributions
            life_contribution = employees_salary [index] * 0.01

        #If they opt out of life insurance
        else:

            #Pay nothing for life insurance
            life_contribution = 0

        #Move up the index
        index = index + 1

        #Add the life insurance contributions into the life
        life_contribution_list.append(life_contribution)

    #Return the life contribution list
    return (life_contribution_list)

#Define function that calculates health insurance cost
def calculate_health_insurance_contribution (health_list):

    #Create a new list for the health insurnace contributions
    health_contribution_list = []

    #Establish an index
    index = 0

    #Create a loop to add data into the health insurance contributions list
    for value in health_list:

        #If they opt for PPOF
        if value == "PPOF":

            #Calculate health insurance contribution
            health_contribution = 3890

        #If they opt for PPOI
        elif value == "PPOI":

            #Calculate health insurance contribution
            health_contribution = 1875
        
        #If they opt out of health insurance            
        else:

            #Pay nothing for health insurance
            health_contribution = 0

        #Move up the index
        index = index + 1

        #Add the life insurance contributions into the list
        health_contribution_list.append(health_contribution)

    #Return the health contribution list
    return (health_contribution_list)
    
#Define function that calculates total benefits
def calculate_total_benefits (e401K_list, life_contribution_list, health_contribution_list, employee_size):

    #Create a new list for the total contributions
    total_benefit_list = []

    #Setup the index to increment the addition
    index = 0
    
    #Create a loop to add all of the contributions
    for num in range(employee_size):

        #Add the first values in all three lists together
        total = e401K_list [index] + life_contribution_list [index] + health_contribution_list [index]

        #Move to the next value in the list
        index = index + 1

        #Add the total contributions into the list
        total_benefit_list.append (total)

    #Return the total benefits list
    return (total_benefit_list)

#Define function that calculates the total of all lists
def calculate_all_totals (any_list):

    #Create a base value for which all total lists will be added to
    total = 0

    #The for loop that will continue to add numbers for the separate lists
    for value in any_list:

        #Add the values on top of each other
        total = total + value

    #Return total
    return total

#Define function to print the summary of the program
def print_summary (employee_size, salary_total, total_total, e401K_total, life_total, health_total):

    #Print the amount of employees processed
    print ("The number of employees processed is ", employee_size, ".", sep='')

    #Print the total salary
    print ("The total salary is $", format(salary_total, ',.0f'), ".", sep='')

    #Print the total benefits
    print ("The total benefits is $", format(total_total, ',.0f'), ".", sep='')

    #Print the total 401K
    print ("The total 401K contributions is $", format(e401K_total, ',.0f'), ".", sep='')

    #Print the total life insurance contributions
    print ("The total life insurance contributions is $", format(life_total, ',.0f'), ".", sep='')

    #Print the total health insurance contributions
    print ("The total health insurance contributions is $", format(health_total, ',.0f'), ".", sep='')

#Define function to write the output file
def write_output_file (name, salary, benefits, number, output_file):
    
    #Set the index to zero
    index = 0

    #Create the loop that will read the entire list
    for num in range(number):

        #Write the data onto the file
        output_file.write(str(name[index]) + ' earns $' + str(format(salary[index], ',.2f')) + ' and contributes $' + str(format(benefits[index],',.2f')) + \
                         ' towards benefits.' + '\n')

        #Move on to the next file
        index = index + 1
    
#Call on main function
main()

