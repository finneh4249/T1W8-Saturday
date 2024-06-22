def add (a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_user_input():
    operation = input("Enter an operation (+, -, *, /): ")
    if operation not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operation")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    return operation, a, b

def main():
    while True:
        
        operation, num1, num2 = get_user_input()
        match operation:
            case "+":
                result = add(num1, num2)
            case "-":
                result = subtract(num1, num2)
            case "*":
                result = multiply(num1, num2)
            case "/":
                result = divide(num1, num2)
            case _:
                raise ValueError("Invalid operation")
        
        def round_numbers(a, b, result):
            if result % 1 == 0:
                result = int(result)
        
            if a % 1 == 0:
                a = int(a)
        
            if b % 1 == 0:
                b = int(b)
        
            return a, b, result
        
        result = round_numbers(num1, num2, result)
    
        print(f"{result[0]} {operation} {result[1]} = {result[2]}")
    
        next_calc = input('\nDo you want to continue? y/n: ')
        if next_calc.lower() != 'yes' and next_calc.lower() != 'y':
            break
    
main()

