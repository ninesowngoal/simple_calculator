#This function will multiply the numbers given by the user and print both the equation and the answer.
def multiply(number_1, number_2, operation, relative_path):
    multiply_answer = number_1 * number_2
    multiply_equation = str(number_1) + " " + operation + " " + str(number_2) + " = " + str(multiply_answer)
    print(multiply_equation)
    with open("{}/user_equations.txt".format(relative_path), 'a') as file: #writes the equation to the user_equations text file.
        file.write(multiply_equation)
        file.write("\n")
        file.close()