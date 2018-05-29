#Author: Nayeon Kim, Miguel Martinez Cano
#Homework Number and Name: Final project
#Due Date: 12/10/16
#Program Description: Inventory class

#Define Inventory class
class Inventory:

    #Define initializer method
    def __init__(self, new_id, new_name, new_stock, new_price):

        #Define attributes of class
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price

    #Define method to get id
    def get_id(self):
        
        return self.__id

    #Define method to get name
    def get_name(self):

        return self.__name

    #Define method to get stock
    def get_stock(self):

        return self.__stock

    #Define method to get price
    def get_price(self):

        return self.__price

    #Define method to restock
    def restock(self, new_stock):

        #Validate input
        if new_stock > 0:

            #Add stock to inventory
            self.__stock = self.__stock + new_stock

            return True

        else:

            #Print error message
            print("Invalid quantity- must be a positive integer.")

            return False

    #Define method to purchase
    def purchase(self, purch_qty):

        #Validate purchase quantity
        if purch_qty <= self.__stock:

            #Subtract purchase quantity from stock
            self.__stock = self.__stock - purch_qty

            return True
            
        else:

            #Print that there is not enough of this item
            print("There is not enough of this item in stock.")

            return False

    #Define method for __str__
    def __str__(self):

        string = self.__id + '\t' + self.__name + '\t' + ' $' + \
                 str(self.__price) + '\t' + str(self.__stock)
             
        return string
        
        

        
            
    

    

        
