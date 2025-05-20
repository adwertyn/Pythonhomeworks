def check(func):  # Decorator to handle errors
    def wrapper(a, b):
        try:
            print(func(a, b))  # Try running the function
        except ZeroDivisionError:
            print("Denominator can't be zero")  # Handle division by zero
    return wrapper

@check  # Apply the decorator
def div(a, b):
    return a / b  # Division function

a = int(input("Enter numerator: "))  # Get numerator
b = int(input("Enter denominator: "))  # Get denominator
div(a, b)  # Call decorated function
