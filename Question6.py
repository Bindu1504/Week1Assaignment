'''
Write a program that repeatedly asks the user to input an integer. Use a `try-except` block to handle `ValueError` in case the user enters a non-integer value. The program should keep asking for input until a valid integer is provided, and then print the integer.

'''



while True:
    user_input = input("Enter an integer: ")

    try:
        number = int(user_input)
        print("You entered the integer:", number)
        break
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
