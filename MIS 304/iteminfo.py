#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #8: The COOP
#Due Date: Monday, November 7, 2016 at 5:00 P.M.
#Item Info
#Class Name: Item Info
#List of Attributes: Item Number, Quantity, Price, Name, Mode
#List of Methods:__init__(), get_item_num(), set_item_num(new_item_num), get_qty(),
#update_qty(new_qty), get_price(), set_price(new_price), get_item_name()
#set_item_name(new_name), get_mode(), update_mode(new_mode), calculate_total()
#__str__()

#Establish item numbers
SHORTS = 32
SHIRT = 83
SOCKS = 39

SHORTS_PRICE = 18.97
SHIRT_PRICE = 29.95
SOCKS_PRICE = 2.99

#Define class
class ItemInfo:
    #Initializer method
    def __init__(self):
        
        #Define attributes
        self.__item_num = 1
        self.__quantity = 1
        self.__price = 1
        self.__name = "Name"
        self.__mode = "Buy"
        
    #Retrieve the item number
    def get_item_num(self):
        return self.__item_num

    #Retrieve the item quantity
    def get_qty(self):
        return self.__quantity

    #Retrieve the item price
    def get_price(self):
        return self.__price

    #Retrieve the item name
    def get_item_name(self):
        return self.__name

    #Retrieve the mode to either make a purchase or return
    def get_mode(self):
        return self.__mode
    
    #Mutators to allow code outside of ItemInfo to update the values
    #of the hidden attributes
    
    #Update the item's number
    def set_item_num(self, new_item_num):
        #Make sure item number is valid
        if new_item_num == SHORTS or new_item_num == SHIRT or new_item_num == SOCKS:
            #Change the number of the item
            self.__item_num = new_item_num
        else:
            #Print a message that the item number was not changed.
            print ("Invalid item number. Item number not changed.")

    #Update the item's quantity
    def update_qty(self, new_qty):
        #Make sure the item quantity is positive
        if new_qty > 0:
            #Change the quantity of the item
            self.__quantity = new_qty
            return True
        else:
            #Print a message that the item quantity was not changed.
            print ("Invalid item quanaity. Item quantity not changed.")
            return False

    #Update the item's price
    def set_price(self, new_price):
        #Determine if the price of the item will be positive or negative
        if self.__mode == "Buy":
            #Positive price
            self.__price = float (new_price)
        elif self.__mode == "Return":
            #Negative price
            self.__price = -1 * float (new_price)

    #Update the item's name
    def set_item_name(self, new_name):
        self.__name = new_name

    #Updat the item's mode
    def update_mode(self, new_mode):
        #Make sure item mode entered is valid
        if new_mode == "Buy" or new_mode == "Return":
            self.__mode = new_mode
            return True
        else:
            #Print a message saying that the item mode was not changed
            print ("Invalid item mode. Item mode not changed.")
            return False

    #Calculate the item total
    def calculate_total(self):
        item_total = self.__price * self.__quantity
        item_total = format (item_total, '.2f')
        return item_total

    #Create a string with the values of the object's attributes
    def __str__(self):
        item_info_print = "The " + self.__name + " has an item number of " + str(self.__item_num) + \
                ". You chose to " + self.__mode + " " + str(self.__quantity) + " at a cost of " + \
                str(self.__price) + " per item."

        return item_info_print
        
