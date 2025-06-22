'''
Write a program that asks the user to input a number in the form of a string. Use a try-except block to convert the string to an integer. If a ValueError occurs (e.g., if the user inputs a non-numeric string), print an error message. Otherwise, print the integer.

'''



user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print("You entered the integer:", number)
except ValueError:
    print("Error: That is not a valid integer. Please enter numeric characters only.")
