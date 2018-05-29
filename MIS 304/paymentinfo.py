#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #8: The COOP
#Due Date: Monday, November 7, 2016 at 5:00 P.M.
#Payment Info
#Class Name: Payment Info
#List of Attributes: Person Name, CC Type, CC Number, CC Exp Date
#List of Methods:__init__(), get_name(), set_name(new_name), get_cc_type(),
#update_cc_type(new_type), get_cc_number(), update_cc_number(new_cc_num),
#get_cc_exp_date(), update_exp_date(new_exp_date), mask_cc_num(), __str__()

#Define class
class PaymentInfo:
    #Initializer method
    def __init__(self):
        
        #Define attributes
        self.__person_name = "John Smith"
        self.__cc_type = "MC"
        self.__cc_number = 1234123412341234
        self.__cc_exp_date = "01/01"

#Retrieve the customer's name
    def get_name(self):
        return self.__person_name

    #Retrieve the credit card type 
    def get_cc_type(self):
        return self.__cc_type

    #Retrieve the credit card number
    def get_cc_number(self):
        return self.__cc_number

    #Retrieve the credit card's expiration date
    def get_cc_exp_date(self):
        return self.__cc_exp_date

    #Mutators to allow code outside of PaymentInfo to update the values
    #of the hidden attributes

    #Update the person's name
    def set_name(self, new_name):
        #Change the name of the person
        self.__person_name = new_name
        
    #Update the credit card type
    def update_cc_type(self, new_type):
        #Make sure the credit card type entered is valid
        if new_type == "MC" or new_type == "VISA" or new_type == "AMEX":
            self.__cc_type = new_type
            return True
        else:
            #Print a message saying that the credit card type was not changed.
            print ("Invalid credit card type enterd. CC type not changed.")
            return False

    #Update the credit card number
    def update_cc_number(self, new_cc_num):
        #Make sure the credit card number entered is valid
        if len(new_cc_num) == 16 or len(new_cc_num) == 15 and new_cc_num.isdigit():
            self.__cc_number = new_cc_num
            return True
        else:
            #Print a message saying that the credit card number was not changed.
            print ("Invalid credit card number enterd. CC number not changed.")
            return False

    #Update the credit card expiration date
    def update_exp_date(self, new_exp_date):
        #Make sure the credit card expiration date entered is valid
        if new_exp_date[2] == '/' and new_exp_date[0:2].isdigit() and new_exp_date[3:5].isdigit():
            self.__cc_exp_date = new_exp_date
            return True
        else:
            #Print a message saying that the credit card expiration date was not changed.
            print ("Invalid credit card expiration date enterd. CC expiration date not changed.")
            return False

    #Mask the credit card number
    def mask_cc_num(self):
        masked_cc_num = self.__cc_number[-4:].rjust(len(self.__cc_number), "X")
        return masked_cc_num
    
    #Create a string with the values of the object's attributes
    def __str__(self):
        payment_info_print = self.__person_name + " used a " + self.__cc_type + " credit card. The credit card number is " + str(self.__cc_number) + \
                             " with an expiration date of " + self.__cc_exp_date

        return payment_info_print
