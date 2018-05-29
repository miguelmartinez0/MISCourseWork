#Program header goes here

#Define constants
MIS_FILE = "MISMajors.txt"
ACC_FILE = "ACCMajors.txt"

ALL_MAJORS = 1
MIS_ONLY = 2
ACC_ONLY = 3
SINGLE_MAJORS = 4
DOUBLE_MAJORS = 5
EXIT = 6

#Define main function
def main():
    #Create empty dictionaries
    mis_set = set()
    acc_set = set()

    #Load data from input file into sets
    #YOU WILL NEED TO ADD LOGIC TO MAKE THIS FUNCTION WORK
    create_sets(mis_set, acc_set)
    #YOU DID THIS
    print (mis_set)
    print (acc_set)
    #You STOPPED HERE

    #Display menu for user
    print_menu()

    #Get user's choice
    menu = get_user_choice()

    #Loop through menu
    while menu != EXIT:
        if menu == ALL_MAJORS:
            #INSERT CODE HERE TO VIEW ALL MAJORS
            #YOU DID THIS
            all_majors = mis_set.union (acc_set)

            for student in all_majors:
                print (student)

            #PRINT NUMBER OF STUDENTS
            print(len(all_majors), "students")

        elif menu == MIS_ONLY:
            #INSERT CODE HERE TO VIEW ONLY MIS MAJORS
            print("View MIS majors.")


            #PRINT NUMBER OF MIS MAJORS

        elif menu == ACC_ONLY:
            #INSERT CODE HERE TO VIEW ONLY ACC MAJORS
            print("View ACC majors.")


            #PRINT NUMBER OF ACC MAJORS

        elif menu == SINGLE_MAJORS:
            #INSERT CODE HERE TO VIEW STUDENTS WITH ONLY ONE MAJOR
            print("View students with only one major.")


            #PRINT NUMBER OF SINGLE MAJORS

        elif menu == DOUBLE_MAJORS:
            #INSERT CODE HERE TO VIEW STUDENTS WITH TWO MAJORS
            print("View students with double majors.")



            #PRINT NUMBER OF DOUBLE MAJORS

        #Get user's choice
        menu = get_user_choice()

#Define function to create dictionaries
def create_sets(mis_major_set, acc_major_set):
    #Open input files
    mis_majors_file = open(MIS_FILE, 'r')
    acc_majors_file = open(ACC_FILE, 'r')
    
    for mis in mis_majors_file:
        
        #YOU DID THIS
        #Populate the mis majors set
        mis_major_set.add(mis.rstrip('\n'))

    for acc in acc_majors_file:
        #Populate the acc majors set
        acc_major_set.add(acc.rstrip('\n'))

    mis_majors_file.close()
    acc_majors_file.close()
    #YOU STOPPED HERE

    ##Do not return anything from this function
    ##Like lists and dictionaries, sets are passed by reference

#Define function to get user's menu choice
def get_user_choice():

    #Prompt user
    choice = int(input("What would you like to do? "))

    #Validate user input
    while choice < ALL_MAJORS and choice > EXIT:
        choice = int(input("Invalid menu option. Please select again: "))

    return choice

#Define menu function
def print_menu():
    print("Please select an option from the menu below:")
    print("1. View all students.")
    print("2. View students only majoring in MIS.")
    print("3. View students only majoring in ACC.")
    print("4. View students with a single major.")
    print("5. View students with a double major.")
    print("6. Exit")

#Call main function
main()
