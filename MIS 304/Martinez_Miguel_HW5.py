#Author: Miguel Martinez Cano
#Homeowkr Number & Name: Homework #5: Student Quiz Averages
#Due Date: Monday, October 10, 2016 at 5:00 P.M.
#Program Description: Program will take the quizzes of different students in a class
#and discover the quiz averages of all of the stundents and place them in a new file

#Rename input file for the program
QUIZ_FILE = "Students.txt"

#Name the output file with the quiz averages
AVERAGE_FILE = "QuizAverages.txt"

#Initalize the quiz grades to zero until changed by the user's input
quiz_grade = 0

#Define function that asks user for number of quizzes
def ask_quiz ():

    #Prompt user to enter how many quizzes were administered
    quiz_number = int(input("How many quizzes were administered? "))

    #Return quiz number
    return (quiz_number)

#Define function that validates quiz number
def validate_quiz (quiz_number):

    #Make sure the quizzes entered is a positive number
    while quiz_number < 1:

        #Invalid number. Prompt user to try again
        quiz_number = int(input("Number must be positive. Please try again: "))

    #Return quiz number
    return (quiz_number)

#Define function to calculate quiz average
def calculate_quiz (quiz_number):

    #Try to open the input file and calculate quiz averages
    try:

        #Read the input file
        quiz_data = open(QUIZ_FILE, "r")

        #Create the new output file
        average_file = open(AVERAGE_FILE, "w")

        #Start with zero students in the class
        count = 0

        #Read student's first name
        student_first = quiz_data.readline () .rstrip ('\n')

        #Read student's last name
        student_last = quiz_data.readline () .rstrip ('\n')

        #Read the students' quiz grades
        while student_first != '':

            #Start with zero point totals
            point_total = 0
            
            #Calculate how many quizzes there are
            for num in range (quiz_number):

                quiz_grade = int (quiz_data.readline ())

                point_total = point_total + quiz_grade
                    
            #Calculate quiz average
            quiz_average = point_total / quiz_number
            
            #Print average
            print(student_last, ", ", student_first, " ", format(quiz_average, '.2f'), sep="")

            #Count the number of students processed
            count = count + 1

            #Read the next student's first name
            student_first = quiz_data.readline () .rstrip ('\n')
            
            #Read the next student's last name
            student_last = quiz_data.readline () . rstrip ('\n')

        #Return the number of students processed
        return (count)

        #Return the quiz average
        average_file.write (student_last + "," + student_first + " " + str(quiz_average) + '\n')

        #Close the input file
        quiz_data.close()

        #Close the output file
        average_file.clsoe()

    #File is unable to be found
    except FileNotFoundError:

        #Print message saying that file cannot be found
        print ("Cound not find Students.txt in current directory.")

    #File has an error in the data
    except ValueError:

        #Print message saying there is an error with the data
        print ("Quizzes entered does not match the number of quizzes in the file.")

    #Exception error
    except Exception as err:

        #Print error
        print (err)

#Define function to print student information
def print_info (count):

    #Print how many students were processed in the file
    print ("The number of students processed is ", count, ".", sep="")

    #Print the name of the output file
    print ("The name of the output file with the quiz averages is QuizAverages.txt")

#Define main function
def main ():

    #Call on function to ask for quiz number
    quiz_num = ask_quiz ()

    #Call on function to validate quiz number
    valid_quiz_number = validate_quiz (quiz_num)

    #Print blank line in between user input and output
    print()

    #Call on function to calculate quiz average
    calc_quiz_grade = calculate_quiz (valid_quiz_number)

    #Print a blank line
    print()
    
    #Call on function to print student information
    print_student_info = print_info (calc_quiz_grade)
    
#Call main function to run program
main ()
