#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Candy
#Class Name: Candy
#List of Attributes: Weight, Price per Pound
#List of Methods:__init__(name, kind), get_weight(), update_weight(new_weight),
#get_price_per_pound(), update_price_per_pound(new_price), calculate_cost(), __str__()

#Import superclass
import dessert

#Define the Candy class - inherits from Dessert
class Candy(dessert.Dessert):
    #Initializer method
    def __init__(self, name, kind):
        
        #Call the initializor of parent and pass parent attribute values
        super().__init__(name, kind)

        #Set default values for Candy attributes
        self.__weight = 1
        self.__price_per_pound = 1

    #Retreive the candy's weight
    def get_weight(self):
        return self.__weight

    #Retreive the candy's price per pound
    def get_price_per_pound(self):
        return self.__price_per_pound
    
    #Mutators to allow code outside of Candy to update the values
    #of the hidden attributes
    
    #Updates the candy's weight
    def update_weight(self, new_weight):
        #Ensure weight is positive
        if new_weight > 0:
            #Change the weight of the candy
            self.__weight = new_weight
            return True
        else:
            #Print a message that the weight was not changed.
            print ("Invalid weight. Weight not changed.")

    #Updates the candy's price per pound
    def update_price_per_pound(self, new_price):
        #Ensure price per pound is positive
        if new_price > 0:
            #Change the price per pound of the candy
            self.__price_per_pound = new_price
            return True
        else:
            #Print a message that the price per pound was not changed.
            print ("Invalid price per pound. Price per pound not changed.")
            return False

    #Calculate the cost of the candy
    def calculate_cost(self):
        candy_cost = self.__weight * self.__price_per_pound
        candy_cost = format (candy_cost, '.2f')
        return candy_cost

    #Create a string with the values of the object's attributes
    def __str__(self):

        cost = self.calculate_cost()
        
        candy_print = super().__str__() + " $" + str(cost)
        return candy_print
        

    
        
