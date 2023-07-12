#import os dependency in order to obtain the relative path to files.
import os
relative_path = os.path.dirname(__file__)

from operations import * #imports the addition, subtraction, multiplication and division functions defined in the operations folder.
from calc_options import * #imports numbers and personal_text

print("This is a simple calculator program.") #explanation of the program and its features.
print("It will ask you to input two numbers.")
print("Your first number either be added, subtracted, multiplied or divided by the second number.")
print("Alternatively, you can create a text file in the same folder as this program and it will read and display the equations and answers included in the file.")
print("")

while True:
    user_choice = input("Would you like to load your personal text file? Type 'y' if so and 'n' if not: ")

    if user_choice == 'n' or user_choice == 'no':
        numbers.functions(relative_path)
        #break
    elif user_choice == 'y' or user_choice == 'yes':
        personal_text.load_file(relative_path)
        #break

#Commented out the break function because I thought (from a UX standpoint) that the user might want to switch from inputting two numbers to loading their text file.
#In addition, the user can close the program on their own whenever they want. Rather than the program closing itself for them, which may get annoying.