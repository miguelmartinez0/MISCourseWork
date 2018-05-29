#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #7: Class Enrollment
#Due Date: Monday, October 24, 2016 at 5:00 P.M.
#Program Description:

#Rename the input files for the program
CLASS_ENROLL = "StudentData.txt"
MIS_304 = "MIS304.txt"
MIS_325 = "MIS325.txt"

#Create the variable that prints parantheis for the email addresses
paran = '('
thesis = ')'

#Create the sets to make sure the eid's follow three letters followed by three numbers
lc_set = set("abcdefghijklmnopqrstuvwxyz")
num_set = set("0123456789")

#Define the menu options
BOTH_MIS = 1
EITHER_MIS = 2
M304_ONLY = 3
M325_ONLY = 4
JUST_ONE = 5
NEW_STUDENT = 6
ADD_STUDENT = 7
DROP_STUDENT = 8
UPDATE_EMAIL = 9
EXIT = 10

#Define function that prints the menu for the user to choose from
def print_menu ():
    print ("IROM CLASS ANALYSIS")
    print ("1.  Which students take both MIS 304 and MIS 325?")
    print ("2.  Which students are taking either or both MIS classes?")
    print ("3.  Which students are taking MIS 304 but not MIS 325?")
    print ("4.  Which students are taking MIS 325 but not MIS 304?")
    print ("5.  Which students take one MIS class but not both?")
    print ("6.  Enroll a new student in the MIS program")
    print ("7.  Add a student to an MIS class")
    print ("8.  Drop a student from an MIS class")
    print ("9.  Update a student's email address")
    print ("10. Exit")

#Define function that adds data into the sets for both majors
def create_sets (MIS304_set, MIS325_set):

    #Open the input files
    MIS304_file = open (MIS_304, 'r')
    MIS325_file = open (MIS_325, 'r')

    #Populate the MIS 304 set
    for m304 in MIS304_file:
        MIS304_set.add(m304.rstrip('\n'))

    #Populate the MIS 325 set
    for m325 in MIS325_file:
        MIS325_set.add(m325.rstrip('\n'))

    #Close the files
    MIS304_file.close()
    MIS325_file.close()

#Define function that adds data into the dictionaries
def create_dictionaries (name_dictionary, email_dictionary):

    #Open input file
    student_data_file = open(CLASS_ENROLL, 'r')

    #Read a line from the input line to process
    for student in student_data_file:

        #Split the line into different components
        student_list = student.split()

        #Create temporary variables to store data
        new_eid = student_list[0]
        new_first = student_list[1]
        new_last = student_list[2]
        new_email = student_list[3].rstrip('\n')

        #Fill the dictionaries with the information
        name_dictionary[new_eid] = new_first + " " + new_last
        email_dictionary[new_eid] = new_email

    #Return name dictionary
    return name_dictionary
    return email_dictionary

#Define the function that allows the user to input their menu option
def get_user_choice ():

    #Prompt user for their menu option
    menu_number = int(input("What would you like to do? "))

    #Validate user input
    while menu_number < BOTH_MIS or menu_number > EXIT:

        #Invalid number. Ask the user to input another number
        menu_number = int(input("Invalid menu option. Please select again: "))

    #Return the menu number for the rest of the program
    return menu_number

#Define function that gets the studaaent's id from the user
def get_student_eid ():

    #Prompt user for the contact info of the new student
    stdnt_eid = input("What is the eid of the student? ")

    lett = str(stdnt_eid[0:3])
    nums = str(stdnt_eid[3:6])

    #Validate that the eid entered is a valid one
    while not lett.isalpha() and not nums.isdigit():

        #Invalied eid entered. Try again
        stdnt_eid = input("Eid must be three letters followed by three numbers. Please try again. ")
        
    #Return the selected eid
    return stdnt_eid

#Define function that gets the student's information from the user
def get_student_name (student_eid, name_dict):

    #Prompt user for the contact info of the new student
    name = input("What is the name of the new student? ")

    #Validate that the name entered is a valid one
    while " " not in name:

        #Invalid entry. Try again.
        name = input("Space must be present to disntinguish between first and last name. Please try again. ")
        
    #Check to see if it is a new contact
    if name not in name_dict: 
                
        #Add new contact to the name dictionary
        name_dict[student_eid] = name

    #Student already exists in the MIS program
    else:
        print("That student already exists. Select another menu option.")

    #Return the name
    return name

#Define function that creates an email for a new student
def create_email (student_eid, student_name, email_dict):

    #Split the names student_name given into a first and last name
    student_name_split = student_name.split()

    #Get the first inital of the first name for the email address for the student
    char1 = student_name [0]

    #Get the last name for the email address
    char2 = student_name_split [1]

    #Make sure the characters for the email are lowercase
    lower_1 = char1.lower()
    lower_2 = char2.lower()

    #Create the student's email address
    student_email = lower_1 + "." + lower_2 + "@utexas.edu"

    #Add new contact email into the email dictionary
    email_dict[student_eid] = student_email

#Define main function
def main():

    #Create the empty sets
    m304_set = set()
    m325_set = set()

    #Create the empty dictionaries
    name_dict = {}
    email_dict = {}
    
    #Call the function to add data to the sets
    create_sets (m304_set, m325_set)

    #Call the function to add data into the dictionaries
    create_dictionaries (name_dict, email_dict)

    #Print the menu
    print_menu ()

    #Call the function to ask the user to input which menu option they would like
    number = get_user_choice ()

    #Go through the different menu options
    while number != EXIT:

        #User has requested to view the students in both classes
        if number == BOTH_MIS:

            #Look for the union in both sets
            both_mis = m304_set.intersection(m325_set)

            #Print the names and email addresses of each student
            for eid in both_mis:

                #Establish a variable to extract data from the dictionary
                key_value = eid

                #Print the names of the students who are in both classes
                print (name_dict[key_value], " ", paran, (email_dict[key_value]), thesis, sep='')

            #Print the number of students
            print (len(both_mis), "students")

        #User has requested to view the students in either class
        if number == EITHER_MIS:

            #Look for the union in both sets
            either_mis = m304_set.union(m325_set)

            #Print the names and email addresses of each student
            for eid in either_mis:

                #Establish a variable to extract data from the dictionary
                key_value = eid

                #Print the names of the students who are in both classes
                print (name_dict[key_value], " ", paran, (email_dict[key_value]), thesis, sep='')

            #Print the number of students
            print (len(either_mis), "students")

        #User has requested to view the students in just the MIS304 class
        if number == M304_ONLY:

            #Look for the union in both sets
            m304_only = m304_set.difference(m325_set)

            #Print the names and email addresses of each student
            for eid in m304_only:

                #Establish a variable to extract data from the dictionary
                key_value = eid

                #Print the names of the students who are in both classes
                print (name_dict[key_value], " ", paran, (email_dict[key_value]), thesis, sep='')

            #Print the number of students
            print (len(m304_only), "students")

        #User has requested to view the students in just the MIS325 class
        if number == M325_ONLY:

            #Look for the union in both sets
            m325_only = m325_set.difference(m304_set)

            #Print the names and email addresses of each student
            for eid in m325_only:

                #Establish a variable to extract data from the dictionary
                key_value = eid

                #Print the names of the students who are in both classes
                print (name_dict[key_value], " ", paran, (email_dict[key_value]), thesis, sep='')

            #Print the number of students
            print (len(m325_only), "students")

        #User has requested to view the students in only one class
        if number == JUST_ONE:

            #Look for the union in both sets
            just_one = m304_set.symmetric_difference(m325_set)

            #Print the names and email addresses of each student
            for eid in just_one:

                #Establish a variable to extract data from the dictionary
                key_value = eid

                #Print the names of the students who are in both classes
                print (name_dict[key_value], " ", paran, (email_dict[key_value]), thesis, sep='')

            #Print the number of students
            print (len(just_one), "students")
            
        #User has requested to a new student to the MIS program
        if number == NEW_STUDENT:

            #Call the function to ask for the student's eid
            student_eid = get_student_eid()

            #Call the function to ask for the student's name
            student_name = get_student_name(student_eid, name_dict)

            #Call the function to create the student's email
            student_email = create_email(student_eid, student_name, email_dict)
            
         #User has requested to add a student in an MIS class
        if number == ADD_STUDENT:

            #Call the function to ask for the student's eid
            student_eid = get_student_eid()
            
        #User has requested to drop a student from an MIS class
        if number == DROP_STUDENT:

            #Call the function to ask for the student's eid
            student_eid = get_student_eid()

            #Check to see whether the student exists in the dictionary
            if student_eid in name_dict:
                
                #Remove student from name dictionary
                del name_dict[student_eid]
                
                #Remove student from email dictionary
                del email_dict[student_eid]

            else:
                #Print error message
                print(student_eid, "not found to remove.")

            #Check to see whether the students exists in the MIS304 set
            if student_eid in m304_set:
                
                #Remove student from the MIS304 set
                m304_set.discard (student_eid)

            #Check to see whether the students exists in the MIS325 set
            else:
                
                #Remove student from the MIS325 set
                m325_set.discard (student_eid)

        #User has requested to update the email address of one of the students
        if number == UPDATE_EMAIL:

            #Call the function to ask for the student's eid
            student_eid = get_student_eid()

            #New email address
            new_email = input("What is the new email address you would like for that student? ")

            #Validate that the email address is correct
            if "@" not in new_email:

                #Invalid email entered
                new_email = input("A complete email includes '@'. Please try again. ")

            #Append the email address of the student
            email_dict [student_eid] = new_email

        #Allow the user to select another options
        number = get_user_choice ()
        
#Call the main function
main ()
