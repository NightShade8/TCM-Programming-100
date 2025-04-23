# Functions in Python

Functions in Python are reusable blocks of code designed to perform specific tasks. They help organize code into logical, modular units, making it more readable, maintainable, and reusable.

## Key Concepts

### Function Definition
A function is defined using the `def` keyword, followed by the function name, parentheses (which may include parameters), and a colon. The function body contains the code to execute. Example:
```python
def greet():
    print("Hello, World!")
```

### Function Call
To execute a function, call it by its name followed by parentheses:
```python
greet()
```

### Function Parameters
Functions can accept parameters to customize their behavior. Parameters are variables that hold values passed to the function:
```python
def greet(name):
    print("Hello, " + name + "!")
greet("Alice")
```
In this example, the `greet()` function accepts a `name` parameter and prints a personalized greeting.

### Return Statement
Functions can return values using the `return` statement. The returned value can be assigned to a variable or used directly:
```python
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 4)
print(result)  # Output: 7
```

## Examples
Here are some practical examples of functions:

1. **Basic Function with Parameters**:
   ```python
   def who_am_i(name, age):
       print(f"My name is {name} and I am {age} years old")
   who_am_i("Heath", 35)
   ```
   *Prints a personalized message using the provided `name` and `age`.*

2. **Adding a Constant**:
   ```python
   def add_one_hundred(num):
       print(num + 100)
   add_one_hundred(100)
   ```
   *Adds 100 to the given number and prints the result.*

3. **Addition of Two Numbers**:
   ```python
   def add(x, y):
       print(x + y)
   add(7, 7)
   ```
   *Adds two numbers and prints the result.*

4. **Multiplication with Return**:
   ```python
   def multiply(x, y):
       return x * y
   result1 = multiply(7, 7)
   result2 = multiply(8, 8)
   print(result1 + result2)
   ```
   *Multiplies two numbers, returns the result, and combines multiple results.*

5. **Square Root Calculation**:
   ```python
   def square_root(x):
       print(x ** 0.5)
   square_root(64)
   ```
   *Calculates and prints the square root of a number.*

6. **New Line Function**:
   ```python
   def nl():
       print('\n')
   nl()
   ```
   *Prints a new line for better formatting.*

Functions are essential for creating modular, efficient, and maintainable code. They allow you to encapsulate logic, reuse code, and improve program structure.