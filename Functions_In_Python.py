# Simple Function
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Function with Default Argument
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

# Lambda Function
add = lambda x, y: x + y

# Recursive Function
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Higher-Order Function
def apply_function(func, *args):
    return func(*args)

# Usage
print(greet("Python"))             # Simple function
print(power(5))                    # Default argument
print(power(2, 3))                 # Default overridden
print(add(3, 7))                   # Lambda function
print(factorial(5))                # Recursive function
print(apply_function(power, 2, 4)) # Higher-order function
