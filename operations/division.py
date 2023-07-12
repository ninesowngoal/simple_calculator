#This function will divide the numbers given by the user and print both the equation and the answer.
def divide(number_1, number_2, operation, relative_path):
    try:
        divide_answer = number_1 / number_2
        divide_equation = str(number_1) + " " + operation + " " + str(number_2) + " = " + str(divide_answer)
        print(divide_equation)
        with open("{}/user_equations.txt".format(relative_path), 'a') as file: #writes the equation to the user_equations text file.
            file.write(divide_equation)
            file.write("\n")
            file.close()
    except ZeroDivisionError:
        print("You cannot divide by zero, please try again.")