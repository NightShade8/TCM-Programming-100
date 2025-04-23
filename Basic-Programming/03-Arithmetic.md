# 🧮 Arithmetic in Python

## 📘 Overview

In Python, the `math` module is a built-in module that provides various mathematical functions and constants. It allows you to perform advanced mathematical operations in your Python programs. To use the `math` module, you need to import it first using the `import` statement.

---

## 🔢 Math Functions in the `math` Module

- **`math.sqrt(x)`**: Calculates the square root of `x` (e.g., √x).
- **`math.pow(x, y)`**: Raises `x` to the power of `y` (e.g., xʸ).
- **`math.exp(x)`**: Calculates the exponential value of `x` (`e^x`).
- **`math.log(x)`**: Calculates the natural logarithm of `x` (base `e`).
- **`math.log10(x)`**: Calculates the logarithm of `x` to base 10.
- **`math.sin(x)`, `math.cos(x)`, `math.tan(x)`**: Calculate the sine, cosine, and tangent of `x`, respectively (where `x` is in radians).
- **`math.degrees(x)`**: Converts `x` from radians to degrees.
- **`math.radians(x)`**: Converts `x` from degrees to radians.

---

## ➕➖✖️➗ Math Operators

- **Addition (`+`)**: Adds two numbers.
- **Subtraction (`-`)**: Subtracts one number from another.
- **Multiplication (`*`)**: Multiplies two numbers.
- **Division (`/`)**: Divides one number by another.
- **Integer Division (`//`)**: Performs division and returns the quotient as an integer (rounds down).
- **Modulo (`%`)**: Returns the remainder of division.
- **Exponentiation (`**`)**: Raises a number to a power.

---

## 📝 Examples

### 🧠 Using Math Functions

```python
import math

# Using math functions
print(math.sqrt(25))  # Output: 5.0
print(math.pow(2, 3))  # Output: 8.0
print(math.sin(math.pi / 2))  # Output: 1.0
```

### 🛠️ Using Math Operators

```python
x = 10
y = 3

# Using math operators
print(x + y)  # Output: 13
print(x / y)  # Output: 3.3333333333333335
print(x // y)  # Output: 3
print(x % y)  # Output: 1
print(x ** y)  # Output: 1000
```

### 🎯 Additional Examples

```python
# Basic arithmetic
print(50 + 50)  # Add ➕
print(50 - 50)  # Subtract ➖
print(50 * 50)  # Multiply ✖️
print(50 / 50)  # Divide ➗

# PEMDAS (Order of Operations)
print(50 + 50 - 50 * 50 / 50)

# Exponents
print(50 ** 2)  # Exponentiation

# Modulo
print(50 % 6)  # Modulo - takes what is left over

# Division
print(50 / 6)  # Division with decimals
print(50 // 6)  # No remainder
```
