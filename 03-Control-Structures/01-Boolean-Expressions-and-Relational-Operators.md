# Boolean Expressions and Relational Operators in Python

Boolean expressions and relational operators are essential tools in Python for decision-making and controlling program flow. Here's a summary of their functionality:

## Relational Operators

Relational operators compare values and return a boolean result (`True` or `False`):

- **Equality (`==`)**: Checks if two values are equal.
- **Inequality (`!=`)**: Checks if two values are not equal.
- **Greater than (`>`)**: Checks if the left value is greater than the right value.
- **Less than (`<`)**: Checks if the left value is less than the right value.
- **Greater than or equal to (`>=`)**: Checks if the left value is greater than or equal to the right value.
- **Less than or equal to (`<=`)**: Checks if the left value is less than or equal to the right value.

## Boolean Expressions

Boolean expressions combine relational expressions using logical operators:

- **Logical AND (`and`)**: Returns `True` if both conditions are `True`.
- **Logical OR (`or`)**: Returns `True` if at least one condition is `True`.
- **Logical NOT (`not`)**: Negates the boolean value of the condition.

### Examples

```python
x = 5
y = 10

# Relational operators
print(x == y)   # False
print(x < y)    # True

# Boolean expressions
print(x < y and y > 0)    # True
print(x < y or y < 0)     # True
print(not (x == y))       # True
```

### Additional Examples

```python
# Boolean expressions
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)  # True True False True
print(type(bool1))  # <class 'bool'>

bool5 = "True"  # Note: This is a string, not a boolean
print(type(bool5))  # <class 'str'>

# Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = True and True  # True
test_and2 = True and False  # False
test_or = True or True  # True
test_or2 = True or False  # True
test_not = not True  # False
```

### Explanation

- **Relational Operators**: Used to compare values and determine relationships (e.g., equality, greater than).
- **Boolean Expressions**: Combine conditions to evaluate complex logical scenarios.
- **Logical Operators**: Enable combining or negating conditions for more advanced decision-making.

These concepts are foundational for control structures like `if` statements and loops, enabling dynamic and conditional program behavior.