#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Ice Cream
#Class Name: Ice Cream
#List of Attributes: Size, Price
#List of Methods:__init__(name, kind), get_size(), update_size(new_size),
#get_price(), update_price(new_price), calculate_cost(), __str__()

#Define global constants
SMALL_PRICE = 1.49
MEDIUM_PRICE = 1.99
LARGE_PRICE = 2.49

#Import superclass
import dessert

#Define the Ice Cream class - inherits from Dessert
class IceCream(dessert.Dessert):
    #Initializer method
    def __init__(self, name, kind):
        
        #Call the initializor of parent and pass parent attribute values
        super().__init__(name, kind)

        #Set default values for Ice Cream attributes
        self.__size = "S"
        self.__price = 1

    #Retreive the ice cream's size
    def get_size(self):
        return self.__size

    #Retreive the ice cream's price
    def get_price(self):
        return self.__price
    
    #Mutators to allow code outside of IceCream to update the values
    #of the hidden attributes
    
    #Update the ice cream's size
    def update_size(self, new_size):
        #Ensure size is valid
        if new_size == "S" or new_size == "M" or new_size == "L":
            #Change the size of the ice cream
            self.__size = new_size

            #Call the function to change the price of the ice cream
            self.update_price(self.__size)
            
            return True
        else:
            #Print a message that the size was not changed.
            print ("Invalid size. Size was not changed.")
            return False
        
    #Update the ice cream's price
    def update_price(self, size):
        #Change price for a small
        if size =="S":
            self.__price = SMALL_PRICE
        #Change prie for a medium
        elif size == "M":
            self.__price = MEDIUM_PRICE
        #Change price for a large
        elif size == "L":
            self.__price = LARGE_PRICE
        else:
            #Print a message that the price was not changed
            print ("Invalid price. Price was not changed.")

    #Calculate the cost of the ice cream
    def calculate_cost(self):
        return self.__price
    
    #Create a string with the values of the object's attributes
    def __str__(self):

        cost = self.calculate_cost()
        
        ice_cream_print = super().__str__() + " $" + str(cost)

        return ice_cream_print
