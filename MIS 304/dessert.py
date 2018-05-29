#Author: Miguel Martinez Cano
#Homework Number & Name: Homework #9: Serendipity 3 - New System
#Due Date: Monday, November 14, 2016 at 5:00 P.M.
#Dessert
#Class Name: Dessert
#List of Attributes: Name, Kind
#List of Methods:__init__(start_name, start_kind), get_name(), get_kind(), __str__()

#Define class
class Dessert:
    #Initializer method
    def __init__(self, start_name, start_kind):
        #Define attributes of each Dessert object with starting values
        self.__name = start_name
        self.__kind = start_kind

    #Define accessors
    def get_name(self):
        return self.__name

    def get_kind(self):
        return self.__kind

    #Define __str__method
    def __str__(self):
        dessert_print = self.__name + " " + self.__kind
        return dessert_print
