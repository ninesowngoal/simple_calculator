#This function will add the numbers given by the user and print both the equation and the answer.
def add(number_1, number_2, operation, relative_path):
    add_answer = number_1 + number_2
    add_equation = str(number_1) + " " + operation + " " + str(number_2) + " = " + str(add_answer)
    print(add_equation)
    with open("{}/user_equations.txt".format(relative_path), 'a') as file: #writes the equation to the user_equations text file.
        file.write(add_equation)
        file.write("\n")
        file.close()