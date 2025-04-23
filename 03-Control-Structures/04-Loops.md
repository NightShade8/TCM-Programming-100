# 🔄 Python Loops Overview

Looping in Python allows you to repeat a block of code multiple times. It is essential for iterating over data structures, automating repetitive tasks, and controlling program flow. Python provides two main types of loops: `for` loops and `while` loops.

---

## 🔁 `for` Loop

The `for` loop iterates over a sequence (e.g., list, tuple, string, or range) or any iterable object. It executes a block of code for each item in the sequence.

### Syntax:
```python
for item in sequence:
    # Code to execute for each item
```

### Example:
```python
fruits = ["apple", "banana", "orange"]  # A list of fruits
for fruit in fruits:  # Loop through each fruit in the list
    print(fruit)  # Print the current fruit
```

**Output:**
```
apple
banana
orange
```

---

## 🔂 `while` Loop

The `while` loop executes a block of code as long as a given condition is `True`. It stops when the condition becomes `False`.

### Syntax:
```python
while condition:
    # Code to execute while the condition is true
```

### Example:
```python
count = 0  # Initialize a counter
while count < 5:  # Loop while count is less than 5
    print(count)  # Print the current value of count
    count += 1  # Increment count by 1
```

**Output:**
```
0
1
2
3
4
```

---

## 🚨 Special Statements: `break` and `continue`

- **`break`**: Exits the loop prematurely.
- **`continue`**: Skips the current iteration and moves to the next one.

---

## 🛠️ Practical Examples

### `for` Loops:
```python
vegetables = ["cucumber", "spinach", "cabbage"]  # A list of vegetables
for veggie in vegetables:  # Loop through each vegetable
    print(veggie)  # Print the current vegetable

for i in range(5):  # Loop through numbers 0 to 4
    print(i)  # Print the current number

word = "Python"  # A string to iterate over
for letter in word:  # Loop through each letter in the string
    print(letter)  # Print the current letter
```

### `while` Loops:
```python
i = 1  # Initialize a counter
while i < 10:  # Loop while i is less than 10
    print(i)  # Print the current value of i
    i += 1  # Increment i by 1
```

---

By mastering loops, you can efficiently process data, automate tasks, and build powerful Python programs! 🚀