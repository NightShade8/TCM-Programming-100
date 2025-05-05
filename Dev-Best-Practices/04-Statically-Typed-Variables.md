What Are Statically Typed Variables?
# 📝 What Are Statically Typed Variables?

## 📌 Overview
Statically typed variables are variables where the type is explicitly declared at compile time and cannot change during program execution. This is in contrast to dynamically typed languages like Python.

## 🔑 Key Components
- **Type Declaration**: Variables must have explicit type declarations
- **Compile-Time Checking**: Type errors are caught before execution
- **Type Consistency**: Variables maintain their declared type throughout execution

## 💻 Examples

### Static Typing (Java)
```java
// Declaring an integer variable
int age = 25;

// This would cause a compilation error
// age = "twenty";  // Cannot assign string to int
```

### Static Typing (C++)
```cpp
// Declaring variables with different types
int count = 10;
double price = 99.99;

// This would cause a compilation error
// count = "hello";  // Cannot assign string to int
```

### Dynamic Typing (Python)
```python
# Variable can hold different types
age = 25          # age is now an integer
age = "twenty"    # age is now a string - no error

# Another example of type flexibility
price = 99.99     # price is a float
price = "expensive"  # price is now a string
```

## 🔄 Static vs Dynamic Typing Comparison

| Feature | Static Typing | Dynamic Typing |
|---------|--------------|----------------|
| Declaration | Required | Not required |
| Type Checking | Compile time | Runtime |
| Performance | Faster | Slower |
| Flexibility | Less flexible | More flexible |

## 🎯 Benefits and Drawbacks

### Static Typing
- ✅ Early error detection
- ✅ Better performance
- ❌ Less flexibility
- ❌ More verbose code

### Dynamic Typing
- ✅ More flexible
- ✅ Faster development
- ❌ Runtime errors
- ❌ Performance overhead

## 🛠️ Python Type Hinting
```python
# Example of optional type hinting in Python
def calculate_total(amount: float, tax_rate: float) -> float:
    return amount * (1 + tax_rate)
```

## 📚 Additional Resources
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [Java Documentation](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
- [C++ Type System](https://en.cppreference.com/w/cpp/language/type)