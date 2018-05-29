#Author: Nayeon Kim, Miguel Martinez Cano
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
        self.__price = new_price

    #Calculate the total cost of the transaction
    def calc_cost(self):
        cost = self.__quantity * self.__price
        return cost

    #Define str method
    def __str__(self):
        transaction_cost = format(self.calc_cost(), '.2f')
        

        string = str(self.__id) + ' ' +self.__name + ' ' + \
            str(self.__quantity) + ' $' + str(transaction_cost)

        return string
        
        
