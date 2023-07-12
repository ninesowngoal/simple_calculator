#Will ask the user for the name of their text file, then will print the equations and the answers.
def load_file(relative_path):
    while True:
            try:
                filename = input("What is the name of your text file (you do not need to specify '.txt')?: ")
                with open("{}/{}.txt".format(relative_path, filename), 'r+') as file:
                    for line in file:
                         answers = [eval(line.split('=')[0])]
                         print(line.strip() + str(answers).strip("[]"))
                    file.close()
                    break
            except FileNotFoundError: #error message displayed if file not found.
                print("That file wasn't found. Please check the spelling and try again (perhaps you included .txt).")
                continue
            except SyntaxError: #error message displayed if there is incorrect syntax in the text file.
                print("There was an error in your text file. Please check every equation entered (you may have used 'x' instead of '*').")
            except ZeroDivisionError:
                 print("You have tried to divide by zero, please correct this and try again.")