#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Sundae
#Class Name: Sundae
#List of Attributes: Toppings
#List of Methods:__init__(name, kind), get_toppings(),
#update_toppings(new_toppings), calculate_cost(), __str__()

#Define cost per topping
TOPPINGS_COST = 0.29

#Import superclass
import icecream

#Define the Sundae class - inherits from Sundae
class Sundae(icecream.IceCream):
    #Initializer method
    def __init__(self, name, kind):

        #Call the initialiore of parent and pass parent attribute values
        super().__init__(name, kind)

        #Set default values for Sundae attributes
        self.__toppings = 1

    #Retreive the candy's toppings
    def get_toppings(self):
        return self.__toppings

    #Mutators to allow code outside of Sundae to update the values
    #of the hidden attributes
    
    #Update the sundae's toppings
    def update_toppings(self, new_toppings):
        #Ensure that the toppings are positive
        if new_toppings > 0:
            #Change the toppings of the sundae
            self.__toppings = new_toppings
            return True
        else:
            #Print a message that the toppings was not changed.
            print ("Invalid toppings. Toppings not changed.")
            return False

    #Calculate the cost of the sundae
    def calculate_cost(self):
        sundae_cost = self.get_price() + (self.__toppings * TOPPINGS_COST)
        sundae_cost = format(sundae_cost, '.2f')
        return sundae_cost

    #Create a string with the values of the object's attributes
    def __str__(self):
        
        sundae_print = super().__str__()

        return sundae_print
        
