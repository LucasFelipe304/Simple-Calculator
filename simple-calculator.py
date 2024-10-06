def options():
    print("""
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Exit the program
""")
options()

while True:
    choose_option = str(input('Choose your option: ')).strip()

    if choose_option == '1':
        n1 = float(input('Enter a number (N1): '))
        n2 = float(input('Enter a number (N2): '))
        def add(x, y):
            return x + y
        add_result = add(n1, n2)
        print(add_result)

    elif choose_option == '2':
        n1 = float(input('Enter a number (N1): '))
        n2 = float(input('Enter a number (N2): '))
        def subtract(x, y):
            return x - y
        subtract_result = subtract(n1, n2)
        print(subtract_result)

    elif choose_option == '3':
        n1 = float(input('Enter a number (N1): '))
        n2 = float(input('Enter a number (N2): '))
        def multiply(x, y):
            return x * y
        multiply_result = multiply(n1, n2)
        print(multiply_result)

    elif choose_option == '4':
        n1 = float(input('Enter a number (N1): '))
        n2 = float(input('Enter a number (N2): '))
        def divide(x, y):
            if y == 0:
                return "Error: Division by zero is not allowed."
            return x / y
        divide_result = divide(n1, n2)
        print(divide_result)

    elif choose_option == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please choose an option between 1 and 5.")