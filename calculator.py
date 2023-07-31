# Basic Operation Functions

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def exponentiate(num1, expo):
    return num1 ** expo

print("Please Enter Operation: \n Addition: + \n Subtraction: - \n Multiplication: * \n Division: / \n Exponentiate: ^ ")

user_operation_input = ""

num1 = 0
num2 = 0

# Retrieves numbers for calculation

def get_numbers():
    global num1
    global num2

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

# Loops the calculation process

while True:

    user_operation_input = input("Select Operation: ")

    if user_operation_input == "+":
        get_numbers()
        print(addition(num1, num2))
    elif user_operation_input == "-":
        get_numbers()
        print(subtraction(num1, num2))
    elif user_operation_input == "*":
        get_numbers()
        print(multiplication(num1, num2))
    elif user_operation_input == "/":
        get_numbers()
        print(division(num1, num2))
    elif user_operation_input == "^":
        get_numbers
        print(exponentiate(num1, num2))
    
    # Check to see if user want's to perform another calculation

    more_calculations = (input("Do you want to perform another calculation (Y for Yes, N for No)? ").upper()).strip()
    
    if more_calculations == "N":
        break
