## 🐍 Python Dictionaries Overview

In Python, a dictionary is an unordered collection of key-value pairs. It is a versatile and powerful data structure that allows you to store, retrieve, and manipulate data based on unique keys.

---

### 📖 Dictionary Basics

#### 🔑 Dictionary Creation
To create a dictionary, enclose key-value pairs within curly braces `{ }`, separating each pair with a colon `:`.

```python
# Creating a dictionary with student details
student = {
    "name": "Alice",  # Key: "name", Value: "Alice"
    "age": 20,        # Key: "age", Value: 20
    "major": "Computer Science"  # Key: "major", Value: "Computer Science"
}
```

---

#### 🔍 Dictionary Access
Access values in a dictionary by referring to their corresponding keys.

```python
# Accessing values using keys
print(student["name"])  # Output: "Alice"
print(student["age"])   # Output: 20
```

---

#### ✏️ Dictionary Modification
Dictionaries are mutable, allowing you to modify values or add new key-value pairs.

```python
# Modifying an existing value
student["age"] = 21  # Updates "age" to 21

# Adding a new key-value pair
student["city"] = "London"  # Adds "city" with value "London"
```

---

### 🔧 Dictionary Operations

#### 📏 Length
Use `len()` to get the number of key-value pairs in a dictionary.

```python
# Getting the number of key-value pairs
print(len(student))  # Output: 3
```

#### 🔄 Iteration
Iterate over keys, values, or key-value pairs using loops.

```python
# Iterating through keys and values
for key in student:
    print(key, student[key])  # Output: "name Alice", "age 21", "major Computer Science"
```

#### ❌ Deletion
Remove a key-value pair using the `del` keyword.

```python
# Deleting a key-value pair
del student["age"]  # Removes the "age" key and its value
```

---

### 🍹 Practical Examples

```python
# Dictionary of drinks with prices
drinks = {"White Russian": 8, "Old Fashioned": 12, "Lemon Drop": 5}  # Key: drink name, Value: price
print(drinks)

# Dictionary of employees grouped by department
employees = {
    "Finance": ["Bob", "Linda", "Tina"],  # Finance department employees
    "IT": ["Gene", "Louise", "Teddy"],    # IT department employees
    "HR": ["Jimmy Jr.", "Mort"]           # HR department employees
}
print(employees)

# Adding a new department
employees['Legal'] = ["Mr. Frond"]  # Adds "Legal" department with one employee
print(employees)

# Updating with another department
employees.update({"Sales": ["Andie", "Ollie"]})  # Adds "Sales" department with two employees
print(employees)

# Modifying the price of a drink
drinks['White Russian'] = 9  # Updates the price of "White Russian" to 9
print(drinks)

# Accessing a value using the get() method
print(drinks.get("White Russian"))  # Output: 9
```

---

Dictionaries are powerful tools for organizing and manipulating data efficiently. They are widely used in Python for tasks requiring quick access to data based on unique keys. 🚀
