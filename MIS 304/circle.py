#Circle Example
#Class Name: Cirle
#List of Attributes: Radius, Border, Color
#List of Methods: calculate_circumference(parameter here if necessary),
                 #calculate_area()

class Circle:
    #Initializer method
    def __init__(self):
        #Define attributes
        self.radius = 1
        self.border = 1
        self.color = "Black"
    def calculate_circumference(self):
        circumference = self.radius * 2 * 3.14
    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
