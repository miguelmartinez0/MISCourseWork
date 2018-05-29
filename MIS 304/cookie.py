#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Cookie
#Class Name: Cookie
#List of Attributes: Quantity, Price per Dozen
#List of Methods:__init__(name, kind), get_quantity(), update_quantity(new_quantity),
#get_price_per_dozen(), update_price_per_dozen(new_price), calculate_cost(), __str__()

#Import superclass
import dessert

#Define the Cookie class - inherits from Dessert
class Cookie(dessert.Dessert):
    #Initializer method
    def __init__(self, name, kind):
        
        #Call the initializor of parent and pass parent attribute values
        super().__init__(name, kind)

        #Set default values for Cookie attributes
        self.__quantity = 1
        self.__price_per_dozen = 1

    #Retreive the cookie's quantity
    def get_quantity(self):
        return self.__quantity

    #Retreive the cookie's price per dozen
    def get_price_per_dozen(self):
        return self.__price_per_dozen
    
    #Mutators to allow code outside of Cookie to update the values
    #of the hidden attributes
    
    #Update the cookies's quantity
    def update_quantity(self, new_quantity):
        #Ensure quantity is positive
        if new_quantity > 0:
            #Change the quantity of the cookie
            self.__quantity = new_quantity
            return True
        else:
            #Print a message that the quantity was not changed.
            print ("Invalid quantity. Quantity not changed.")

    #Updates the cookies's price per dozen
    def update_price_per_dozen(self, new_price):
        #Ensure price per pound is positive
        if new_price > 0:
            #Change the price per pound of the cookie
            self.__price_per_dozen = new_price
            return True
        else:
            #Print a message that the price per dozen was not changed.
            print ("Invalid price per dozen. Price per dozen not changed.")
            return False

    #Calculate the cost of the cookie
    def calculate_cost(self):
        cookie_cost = (self.__quantity * self.__price_per_dozen) / 12
        cookie_cost = format (cookie_cost, '.2f')
        return cookie_cost

    #Create a string with the values of the object's attributes
    def __str__(self):

        cost = self.calculate_cost()
        
        cookie_print = super().__str__() + " $" + str(cost)

        return cookie_print
