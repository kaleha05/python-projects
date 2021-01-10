def add_func(num1, num2):
    return num1 + num2

def subtract_func(num1, num2):
    return num1 - num2

def multiply_func(num1, num2):
    return num1 * num2

def divide_func(num1, num2):
    return num1 / num2


print("Calculator program")
print("--------------------")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

user_choice = int(input("Enter the option number: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if user_choice == 1:
    print(num1, " + ", num2, " = ", add_func(num1, num2))
elif user_choice == 2:
    print(num1, " - ", num2, " = ", subtract_func(num1, num2))
elif user_choice == 3:
    print(num1, " * ", num2, " = ", multiply_func(num1, num2))
elif user_choice == 4:
    print(num1, " / ", num2, " = ", divide_func(num1, num2))
else:
    print("Invalid choice of operation!")
