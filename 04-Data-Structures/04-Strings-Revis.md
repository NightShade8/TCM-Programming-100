# Strings In Python

In Python, the str (string) data type represents a sequence of characters enclosed within single quotes (' ') or double quotes (" "). Strings in Python are immutable, which means they cannot be changed after they are created. Here are some key points about strings in Python:

## 🌟 String Operations in Python

### ✨ Creation
You can create strings using single or double quotes:
```python
my_string = 'Hello, World!'  # Single quotes
my_string = "Hello, World!"  # Double quotes
```

### 🔍 Accessing Characters
Access individual characters using indexing (starting from 0):
```python
print(my_string[0])  # Outputs 'H' (first character)
```

### ➕ String Concatenation
Combine strings using the `+` operator:
```python
greeting = 'Hello' + ' ' + 'World!'  # Results in 'Hello World!'
```

### 📏 String Length
Use `len()` to find the number of characters in a string:
```python
print(len(my_string))  # Outputs the length of the string
```

### ✂️ String Slicing
Extract substrings using slicing:
```python
substring = my_string[7:12]  # Extracts 'World'
```

### 🛠️ String Methods
Python provides built-in methods for string manipulation:
```python
print(my_string.upper())  # Converts to 'HELLO, WORLD!'
```

### 🖋️ String Formatting
Embed values into strings using `%`, `format()`, or f-strings:
```python
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))  # Using %
print("My name is {} and I'm {} years old.".format(name, age))  # Using format()
print(f"My name is {name} and I'm {age} years old.")  # Using f-strings
```

---

### 🧑‍💻 Advanced String Examples
```python
my_name = "Heath"
print(my_name[0])  # Outputs 'H' (first letter)
print(my_name[-1])  # Outputs 'h' (last letter)

sentence = "192.168.138.1"
print(sentence[:4])  # Outputs '192.'

print(sentence.split('.'))  # Splits by '.' into ['192', '168', '138', '1']

sentence_split = sentence.split('.')
sentence_join = '.'.join(sentence_split)
print(sentence_join)  # Joins back into '192.168.138.1'

quote = "He said, 'give me all your money'"
quote = "He said, \"give me all your money\""
print(quote)  # Outputs the quote with proper escaping

too_much_space = "                   hello       "
print(too_much_space.strip())  # Removes leading/trailing spaces

print("A" in "Apple")  # Returns True
print("a" in "Apple")  # Returns False (case-sensitive)

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())  # Returns True (case-insensitive)

# Example of user input handling:
# user_input = input("Enter yes or no: ")
# if user_input.lower().strip() == "yes":
#     print("You agree!")
# else:
#     print("You disagree!")

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))  # Using format()
print("My favorite movie is %s." % movie)  # Using %
print(f"My favorite movie is {movie}.")  # Using f-strings
```