## 🐍 Python Variables and Methods

In Python, variables and methods are fundamental concepts used in programming. Here's an explanation of each:

---

### 📦 Variables

A **variable** is a named storage location used to store data or values in a program. It acts as a placeholder for data that can be accessed, modified, or used in calculations throughout the program. Variables in Python are dynamically typed, meaning their data type can change during program execution.

#### Example: Variable Assignment

```python
# Variable assignment
x = 10
name = "John"
is_true = True

# Variable usage
y = x + 5
print("Hello, " + name)
if is_true:
    print("The condition is true")
```

In the example above:
- `x`, `name`, and `is_true` are variables assigned with different data types (integer, string, and boolean, respectively).
- They are used in calculations and print statements to perform operations and display values.

---

### 🔧 Methods

A **method** is a block of reusable code that performs a specific task or action. Methods are associated with objects or classes and are called upon to perform certain operations. In Python, methods are commonly referred to as **functions**. Built-in functions and user-defined functions both fall under the category of methods.

#### Example: Built-in and User-defined Methods

```python
# Built-in method example
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print("Length:", length)

# User-defined method example
def greet(name):
    print("Hello, " + name)

greet("Alice")
```

In the example above:
- `len()` is a built-in method that calculates the length of a list (`numbers` in this case).
- The user-defined method `greet()` takes a parameter `name` and prints a greeting message. It is called with the argument `"Alice"` to print `"Hello, Alice"` to the console.

---

### 🧪 Additional Examples

```python
# Variables and methods
age = 35  # int
name = "Heath"  # string
gpa = 3.7  # float

print(int(age))
print(int(35.1))
print(int(35.9))  # Will it round? No!

quote = "All is fair in love and war."
print(quote)

print(quote.upper())  # Uppercase
print(quote.lower())  # Lowercase
print(quote.title())  # Title case
print(len(quote))  # Count characters

print("My name is " + name + " and I am " + str(age) + " years old.")
```

---

### 📝 Key Takeaways

- **Variables** store data, while **methods** encapsulate reusable blocks of code for specific tasks.
- Understanding their usage and relationship is crucial for building functional and efficient programs.

---

### 🚀 Practice Exercise

Try creating your own variables and methods! For example:
1. Create a variable to store your favorite quote.
2. Write a method to print the quote in uppercase, lowercase, and title case.
3. Count the number of characters in the quote using a built-in method.

Happy coding! 🎉