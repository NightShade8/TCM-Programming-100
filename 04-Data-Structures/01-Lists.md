# 📋 Python Lists

In Python, a **list** is a versatile and mutable data structure that can hold a collection of items. It allows you to store multiple values of different data types in a single variable. Here's a detailed explanation of lists in Python:

---

## 🛠️ List Creation

To create a list, you enclose comma-separated values within square brackets `[ ]`. Here's an example:

```python
fruits = ["apple", "banana", "orange"] 
```

---

## 🔍 List Access

You can access individual elements in a list using **indexing**. Indexing starts from `0` for the first element and goes up to the length of the list minus one.

```python
print(fruits[0])    # Output: "apple" (Access the first element)
print(fruits[2])    # Output: "orange" (Access the third element)
```

---

## ✏️ List Modification

Lists are **mutable**, meaning you can modify their elements. You can assign new values to specific positions or use methods to modify the list itself.

```python
fruits[1] = "grape"     # Replace "banana" with "grape"
fruits.append("kiwi")   # Add "kiwi" to the end of the list
fruits.remove("apple")  # Remove "apple" from the list
```

---

## ⚙️ List Operations

Python provides various operations that can be performed on lists. Some common operations include:

### ➕ Concatenation
You can use the `+` operator to combine two or more lists.

```python
fruits = ["apple", "banana", "orange"]
fruits2 = ["grape", "kiwi"]

combined = fruits + fruits2
print(combined)  # Output: ["apple", "banana", "orange", "grape", "kiwi"]
```

### 📏 Length
The `len()` function returns the number of elements in a list.

```python
print(len(fruits))  # Output: 3
```

### ✂️ Slicing
You can extract a sublist from a list using slicing.

```python
sublist = fruits[1:3]
print(sublist)  # Output: ["banana", "orange"]
```

### 🔄 Iteration
You can use a loop to iterate over the elements of a list.

```python
for fruit in fruits:
    print(fruit)  # Output: "apple", "banana", "orange"
```

---

## 🎥 Example: Working with Movie Lists

```python
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1])  # Output: "The Hangover" (Access the second item)
print(movies[0])  # Output: "When Harry Met Sally" (Access the first item)
print(movies[1:3])  # Output: ["The Hangover", "The Perks of Being a Wallflower"] (Slice from index 1 to 2)
print(movies[1:])  # Output: ["The Hangover", "The Perks of Being a Wallflower", "The Exorcist"] (From index 1 to end)
print(movies[:2])  # Output: ["When Harry Met Sally", "The Hangover"] (Up to index 2, exclusive)
print(movies[-1])  # Output: "The Exorcist" (Access the last item)

print(len(movies))  # Output: 4 (Count the items in the list)

movies.append("JAWS")  # Add "JAWS" to the end of the list
print(movies)

movies.insert(2, "Hustle")  # Insert "Hustle" at index 2
print(movies)

movies.pop()  # Remove the last item ("JAWS")
print(movies)

movies.pop(0)  # Remove the first item ("When Harry Met Sally")
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies  # Combine two lists
print(our_favorite_movies)
```

---

## 📚 Nested Lists

Lists can also contain other lists, creating a **nested list**.

```python
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]

bobs_grade = grades[0][1]  # Access Bob's grade (82)
print(bobs_grade)

grades[0][1] = 83  # Update Bob's grade to 83
print(grades)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6 (Access the third element of the second list)
```

---

Lists are powerful data structures in Python that allow you to store and manipulate collections of items. They are widely used for managing and processing data in various applications. 🚀