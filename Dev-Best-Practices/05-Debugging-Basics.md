# 🔧 Python Debugging Basics

## 📝 Overview
Debugging is the process of finding and fixing errors (bugs) in code. This guide covers essential debugging techniques in Python to help troubleshoot common issues.

## 🛠️ Key Debugging Methods

### 1. Print Statements
```python
def add_numbers(a, b):
    print(f"a: {a}, b: {b}")  # Displays input values for verification
    return a + b              # Returns sum of inputs

result = add_numbers(5, 3)    # Calls function with test values
print(f"Result: {result}")    # Shows final output
```

### 2. Code Commenting
```python
def divide_numbers(a, b):
    # result = a / b         # Original division (commented out)
    result = a // b          # Integer division for testing
    return result            # Returns division result
```

### 3. Error Messages
```python
def divide_numbers(a, b):
    return a / b            # Division operation

# ZeroDivisionError example
print(divide_numbers(10, 0)) # Demonstrates error when dividing by zero
```

### 4. Assert Statements
```python
def square_number(n):
    result = n * n          # Calculates square
    assert result >= 0      # Verifies result is non-negative
    return result          # Returns squared value
```

### 5. PDB Debugger
```python
import pdb                  # Imports Python debugger

def add_numbers(a, b):
    pdb.set_trace()        # Sets breakpoint
    result = a + b         # Performs addition
    return result         # Returns sum
```

## 🚨 Common Python Errors
- **SyntaxError**: Missing syntax elements
- **TypeError**: Incompatible data type operations
- **IndexError**: Invalid list/array access
- **ZeroDivisionError**: Division by zero
- **NameError**: Undefined variable usage

## 💡 Best Practices
1. Use print statements strategically
2. Read error messages carefully
3. Test code in small sections
4. Implement assertions for validation
5. Utilize debugging tools effectively
6. Document debugging steps
7. Learn from common errors

## 🎯 Quick Debug Checklist
- [ ] Verify variable values
- [ ] Check function inputs/outputs
- [ ] Review syntax carefully
- [ ] Test edge cases
- [ ] Use appropriate debug tools
- [ ] Document solutions found
