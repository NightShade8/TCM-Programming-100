# 🧵 Strings in Python

## 📌 Overview
In Python, the `str` (string) data type represents a sequence of characters enclosed within single quotes (`' '`) or double quotes (`" "`). Strings in Python are **immutable**, which means they cannot be changed after they are created.

---

## ✨ Key Features of Strings

### **1️⃣ Creation**
You can create strings using single quotes, double quotes, or triple quotes for multi-line strings.

```python
my_string = 'Hello, World!' 
my_string = "Hello, World!"
```

---

### **2️⃣ Accessing Characters**
You can access individual characters within a string using **indexing**, starting from `0`.

```python
print(my_string[0])  # Output: 'H'
```

---

### **3️⃣ String Concatenation**
You can concatenate (join) two or more strings using the `+` operator.

```python
greeting = 'Hello' + ' ' + 'World!' 
print(greeting)  # Output: 'Hello World!'
```

---

### **4️⃣ String Length**
The `len()` function can be used to determine the length (number of characters) of a string.

```python
print(len(my_string))  # Output: length of the string
```

---

### **5️⃣ String Slicing**
You can extract a substring from a string using **slicing**, specifying the start and end indices.

```python
substring = my_string[7:12] 
print(substring)  # Output: 'World'
```

---

### **6️⃣ String Methods**
Python provides various built-in methods to manipulate and transform strings. Examples include `upper()`, `lower()`, `strip()`, `split()`, `replace()`, and more.

```python
print(my_string.upper())  # Output: 'HELLO, WORLD!'
```

---

### **7️⃣ String Formatting**
String formatting allows you to embed values within a string. This can be done using the `%` operator, the `format()` method, or **f-strings**.

```python
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))  # Old-style formatting
print(f"My name is {name} and I'm {age} years old.")  # f-string formatting
# Both will output: My name is Alice and I'm 30 years old.
```

---

## 🛠️ Examples

### **1️⃣ Basic String Operations**
```python
# Strings
print("Hello, World")
print('Hello, World')
print("""This string runs
multiple lines!""")  # Triple quotes for multi-line strings
print("This is a " + "string!")  # Concatenating strings
```

---

### **2️⃣ Special Characters**
```python
print('\n')  # New line
print('Test that new line out')
```

---

## 📚 Summary
Strings are a fundamental data type in Python, offering a wide range of features for manipulation and formatting. Whether you're working with simple text or complex string operations, Python's string methods and formatting options make it easy to handle text efficiently. 🚀