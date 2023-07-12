#This function will subtract the numbers given by the user and print both the equation and the answer.
def subtract(number_1, number_2, operation, relative_path):
    subtract_answer = number_1 - number_2
    subtract_equation = str(number_1) + " " + operation + " " + str(number_2) + " = " + str(subtract_answer)
    print(subtract_equation)
    with open("{}/user_equations.txt".format(relative_path), 'a') as file: #writes the equation to the user_equations text file.
        file.write(subtract_equation)
        file.write("\n")
        file.close()