#Program header goes here

#Define constants
DATA_FILE = "ContactInfo.txt"

VIEW_SPECIFIC = 1
VIEW_NAMES = 2
VIEW_ALL = 3
ADD_CONTACT = 4
REMOVE_CONTACT = 5
UPDATE_ADDR = 6
EXIT = 7

#Define main function
def main():
    #Create empty dictionaries
    street_dict = {}
    city_dict = {}
    zip_dict = {}

    #Load data from input file into dictionaries
    #YOU WILL NEED TO ADD LOGIC TO MAKE THIS FUNCTION WORK
    create_dictionaries(street_dict, city_dict, zip_dict)

    #Display menu for user
    print_menu()

    #Get user's choice
    menu = get_user_choice()

    #Loop through menu
    while menu != EXIT:
        if menu == VIEW_SPECIFIC:
            #Ask user for name of contact to view
            name = input("Whose contact information would you like to view? ")
            #YOU DID THIS
            #INSERT CODE HERE TO VIEW THE CONTACT INFO 
            address = street_dict[name]
            city = city_dict[name]
            zip_code = zip_dict[name]

            #Call function to display contact info
            display_contact_info(name, address, city, zip_code)
            #display_contact_info(name, street_dict[name], city_dict[name], zip_dict[name])


        elif menu == VIEW_NAMES:
            #INSERT CODE HERE TO VIEW NAMES OF ALL CONTACTS

            for key in street_dict:
                print(key)



        elif menu == VIEW_ALL:
            #INSERT CODE HERE TO VIEW CONTACT INFO FOR ALL CONTACTS

            for key in street_dict:
                
                display_contact_info(key, street_dict[key], city_dict[key], zip_dict[key])
            
                print()
            #YOU STOPPED HERE

        elif menu == ADD_CONTACT:
            #Prompt user for new contact info
            name = input("What is the name of the new contact? ")
            address = input("What is the street address for " + name + "? ")
            city = input("In what city does " + name + " live? ")
            postal_code = input("What is the zip code? ")
            
            #INSERT CODE HERE TO ADD NEW CONTACT INFO




        elif menu == REMOVE_CONTACT:
            #Prompt user for contact to remove
            name = input("Whose contact information would you like to delete? ")

            #INSERT CODE HERE TO REMOVE THE CONTACT





        elif menu == UPDATE_ADDR:
            #Prompt user for contact to update
            name = input("Whose street address would you like to update? ")

            #INSERT CODE HERE TO UPDATE THE STREET ADDRESS FOR THE CONTACT





        #Get user's choice
        menu = get_user_choice()

#Define function to create dictionaries
def create_dictionaries(addr_dict, cities_dict, zips_dict):
    #Open input file
    contact_info_file = open(DATA_FILE, 'r')

    for contact in contact_info_file:
        #Populate each dictionary
        #HINT: You will probably need to separate values in the line from the file
        #YOU DID THIS
        contact_list = contact.split(':') #Split the string at every colon

        name = contact_list[0]
        street = contact_list[1]
        city = contact_list[2]
        zip_code = contact_list[3].rstrip('\n')

        #Add elements into the three different dictionary
        addr_dict[name] = street
        cities_dict[name] = city
        zips_dict[name] = zip_code
    #YOU STOPPED HERE
    ##Do not return anything from this function
    ##Like lists, dictionaries are passed by reference

#Define function to display contact info nicely
def display_contact_info(contact_name, addr, city, zip_code):
    print(contact_name)
    print(addr)
    print(city, ", ", zip_code, sep="")

#Define function to get user's menu choice
def get_user_choice():

    #Prompt user
    choice = int(input("What would you like to do? "))

    #Validate user input
    while choice < VIEW_SPECIFIC and choice > EXIT:
        choice = int(input("Invalid menu option. Please select again: "))

    return choice

#Define menu function
def print_menu():
    print("Please select an option from the menu below:")
    print("1. View contact information for a specific person.")
    print("2. View a list of all contact names.")
    print("3. View contact information for all contacts.")
    print("4. Add a new contact")
    print("5. Remove an existing contact")
    print("6. Update address for an existing contact")
    print("7. Exit")

#Call main function
main()
