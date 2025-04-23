### 🐍 Python Conditional Statements Overview

Conditional statements in Python allow you to control the flow of your program by executing specific blocks of code based on certain conditions. Here's a quick summary with added comments for clarity:

#### ✅ `if` Statement
Executes a block of code if a condition is true.
```python
x = 5  # Assign a value to x
if x > 0:  # Check if x is greater than 0
    print("x is positive")  # This line runs if the condition is true
```

#### 🔄 `if-else` Statement
Specifies two blocks of code: one for when the condition is true, and another for when it's false.
```python
x = 5  # Assign a value to x
if x > 0:  # Check if x is greater than 0
    print("x is positive")  # Runs if the condition is true
else:
    print("x is not positive")  # Runs if the condition is false
```

#### 🔀 `if-elif-else` Statement
Checks multiple conditions and executes the corresponding block of code for the first true condition.
```python
x = 5  # Assign a value to x
if x > 0:  # Check if x is greater than 0
    print("x is positive")  # Runs if the first condition is true
elif x < 0:  # Check if x is less than 0
    print("x is negative")  # Runs if the second condition is true
else:
    print("x is zero")  # Runs if none of the above conditions are true
```

#### 💡 Example Functions
```python
# Simple drink decision
def drink(money):
    # Check if the money is enough for a drink
    if money >= 2:
        return "You've got yourself a drink!"  # Sufficient money
    else:
        return "No drink for you!"  # Insufficient money

print(drink(3))  # Output: You've got yourself a drink!
print(drink(1))  # Output: No drink for you!

# Alcohol purchase decision
def alcohol(age, money):
    # Check if the person meets the age and money requirements
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"  # Meets both conditions
    elif (age >= 21) and (money < 5):
        return "Come back with more money."  # Old enough but lacks money
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"  # Has money but too young
    else:
        return "You're too young and too poor."  # Fails both conditions

print(alcohol(21, 5))  # Output: We're getting a drink!
print(alcohol(21, 4))  # Output: Come back with more money.
print(alcohol(20, 5))  # Output: Nice try, kid!
print(alcohol(20, 4))  # Output: You're too young and too poor.
```

Conditional statements are essential for implementing logic and branching in your code. They make your programs dynamic and responsive! 🚀
