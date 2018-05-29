#Author: Miguel Martinez Cano
#Homework Number & Name: Final Project
#Due Date: Tuesday, December 14, 2016 at 5:00 P.M.
#TransactionItem
#Class Name: TransactionItem
#List of Attributes: ID, Name, Quantity, Price
#List of Methods:__init__(), get_id(), set_id(new_id), get_name(), set_name(new_name),
#get_qty(), set_qty(new_qty), get_price(), set_price(new_price), calc_cost(), __str__()

#Define the TransactionItem class
class TransactionItem:

    #Define init method
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__quantity = 0
        self.__price = 0

    #Define accessor for id
    def get_id(self):
        return self.__id

    #Define accessor for name
    def get_name(self):
        return self.__name

    #Define accessor for quantity
    def get_qty(self):
        return self.__quantity

    #Define accessor for price
    def get_price(self):
        return self.__price

    #Define mutator for id
    def set_id(self, new_id):
        self.__id = new_id

    #Define mutator for name
    def set_name(self, new_name):
        self.__name = new_name

    #Define mutator for quantity
    def set_qty(self, new_qty):
        #Ensure quantity is positive
        if new_qty > 0:
            self.__quantity = new_qty

    #Define mutator for price
    def set_price(self, new_price):
        #Ensure price is positive for a purchase
        if new_price > 0:
            self.__price = new_price
            
        #Price is negative for a return
        else:
            self.__price = new_price

    #Calculate the total cost of the transaction
    def calc_cost(self):
        cost = self.__quantity * self.__price
        return cost

    #Define str method
    def __str__(self):
        transaction_cost = self.calc_cost()

        #Return was made
        if transaction_cost < 0:
            string = self.__quantity + self.__name + " were returned at a price of $" + \
            self.__price + " and an ID number of " + self.__id

        #Purchase was made
        else:
            string = self.__quantity + self.__name + " were purchased at a price of $" + \
            self.__price + " and an ID number of " + self.__id

        return string
        
        
