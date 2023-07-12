from operations import * #import the operations defined in the task 9/operations folder.

def functions(relative_path):
    while True:
            try:
                number_1 = float(input("Please enter a number: "))
                number_2 = float(input("Please enter another number: "))
            except ValueError:
                print("You didn't input a number, please try again.") #if the user inputs anything other than a number, it will ask them to try again.
                continue #User will input a number again.

            while True:
                operation = input("What would you like to do with these numbers (+, -, x, /)?:") #ask which the user would like to do.

                if operation == "+":
                    addition.add(number_1, number_2, operation, relative_path)
                    break
                if operation == "-":
                    subtraction.subtract(number_1, number_2, operation, relative_path)
                    break
                if operation == "x":
                    multiplication.multiply(number_1, number_2, operation, relative_path)
                    break
                if operation == "/":
                    division.divide(number_1, number_2, operation, relative_path)
                    break
                elif operation != "+" and operation != "-" and operation != "x" and operation != "/":
                    print("That is not a valid operation. Please try again.") #if the user somehow inputs something other than those, will return this "error".
                    continue #will go back to asking the user which operation they would like to do.
            
            if operation == "+" or operation == "-" or operation == "x" or operation == "/": #code below will loop back to asking for 2 numbers should the user specify. Otherwise will stop.
                while True:
                    user_continue = input("Would you like to continue (type 'y' to continue and 'n' to stop)?")
                    if user_continue == 'y' or user_continue == "yes" or user_continue == 'continue':
                        break
                    elif user_continue == 'n' or user_continue == 'no' or user_continue == 'stop' or user_continue == 'end':
                        break
                    else:
                        print("That was not a valid answer. Please type either 'y' or 'n'.")
            if user_continue == 'y' or user_continue == "yes" or user_continue == 'continue':
                continue
            elif user_continue == 'n' or user_continue == 'no' or user_continue == 'stop' or user_continue == 'end':
                break