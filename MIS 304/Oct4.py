#Open studentnames file
student_name = open ("StudentNames.txt", "r")

#Start with zero students in the class
count = 0

#For every name in the file
for student in student_name:

    #Equate every name to the name variable
    name = student.rstrip('\n')

    #Print every student name
    print ("Student Name:", name)

    #Add how many students are in the class
    count = count + 1

#Print how many students there are in the class
print ("There were", count, "students in the file.")
    
#Close studentnames files
student_name.close()

print ()

STUDENT_FILE = "StudentNames.txt"

def main():

    #Open input file and read it
    student_data = open(STUDENT_FILE, "r")

    #Start with zero students in the class
    count = 0

    #For every name in the file
    for name in student_data:

        #Equate every name to the name variable
        name = name.rstrip ('\n')

        #Printe every student name
        print (name)

        #Add how many students are in the class
        count = count + 1

    #Close the input file
    student_data.close()

    #Print how many students are in the class
    print ("There were", count, "students in the file.")

#Call the main function
main()
           
#Define new function
def write():
    class_data = open ("ClassList.txt", "w")
    for classes in range (3):
           class_name = input("Please enter a class (e.g. MIS304): ")
           class_data.write
    
