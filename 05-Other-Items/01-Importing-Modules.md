## 📦 Importing Modules in Python

Importing modules in Python allows you to access and use code from external files or libraries. This promotes code reusability, modularity, and maintainability. Below are different ways to import modules:

### 🌐 Importing Entire Modules
To import an entire module, use the `import` keyword followed by the module name:
```python
import math  # Import the math module

result = math.sqrt(25)  # Use the sqrt() function from the math module
print(result)  # Output: 5.0
```

### 🎯 Importing Specific Functions or Variables
You can import specific functions or variables directly:
```python
from math import sqrt  # Import only the sqrt() function from the math module

result = sqrt(25)  # Use the imported sqrt() function directly
print(result)  # Output: 5.0
```

### ✏️ Importing Modules with an Alias
Assign an alias to a module using the `as` keyword:
```python
import math as m  # Import the math module with an alias 'm'

result = m.sqrt(25)  # Use the sqrt() function with the alias
print(result)  # Output: 5.0
```

### 🌟 Importing All Functions and Variables
Use the `*` wildcard to import everything from a module (not recommended due to potential namespace conflicts):
```python
from math import *  # Import all functions and variables from the math module

result = sqrt(25)  # Use the sqrt() function directly
print(result)  # Output: 5.0
```

### 🛠️ Practical Example
Here’s a practical example of importing modules:
```python
# Import system functions and parameters
import sys  

# Import datetime with an alias
from datetime import datetime as dt  

print(sys.version)  # Print the Python version
print(dt.now())  # Print the current date and time
```

By importing modules, you can leverage the Python standard library and third-party libraries to enhance your programs efficiently. 🚀
