#Create a list variable with integers
grade_list = [98, 76, 89, 90, 65, 86]

#Create a list variable with strings
name_list = ['Mickey Mouse', 'Cinderella', 'Wall-E']

#Create a list variable with integers and strings
employee_list = ['Jon Smith', 6500.00, 24]

#Make a list that is empty and data will eventually be put in for the variable
course_list = []

#Remove the brackets and commas in the list variable
for grade in grade_list:

    #Print each grade on a separate line
    print (grade)

#Index allows to access one certain number in the list
"""#grade_list [index]""" #index will be an integer, not a string

print ()

#Print certain grades on separate lines
print (grade_list[0]) #1st item in the list
print (grade_list[5]) #6th item in the list
"""print (grade_list[6])""" #7th item in the list, NONEXISTENT so ERROR

#Len lets you know how many elements are in the list
size = len(grade_list)

#Print the number of elements in the list
print (size)

print ()

#EXAMPLE 1
#Define main function
def main():
    
    #Define list
    my_list = [5, 10, 15, 20, 25]

    #Print the old list
    print (my_list)

    #Establish the index
    index = 0

    #Remove brackets and commas in the list variable
    for num in my_list:

        #Update each number in the list by multiplying it by two
        my_list [index] = num * 2

        #Print the new values of the list
        print (my_list[index])
        
        #Increment index to read the next element in the list
        index = index + 1

    #Print the new list
    print (my_list)
    

#Call main function
main()

print()

#Add a 7th grade to grade list variable at the end
grade_list.append (78)

print (grade_list)

#Add a new 3rd grade with a grade of 84, making the total number of elements 8
grade_list.insert (2, 84)

print (grade_list)

#Print the amount of elements after the append and insert functions
print ("The number of grades is", len(grade_list))

print()

#EXAMPLE 2
#IN a separate python file



