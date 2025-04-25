## Writing Reusable and Testable Code 🧪

Writing testable code involves structuring your code to make it easy to test individual components (e.g., functions or classes) without relying on external systems like databases, APIs, or user input. Testable code adheres to principles such as **separation of concerns**, **clear inputs and outputs**, and **minimal side effects**.

---

### Example: Refactoring for Testability 🔄

#### Non-Testable Code Example ❌
```python
def atm_withdrawal():
    balance = int(input("Enter your current balance: "))  # Takes user input for balance
    amount = int(input("Enter the amount to withdraw: "))  # Takes user input for withdrawal amount
    
    if amount > balance:
        print("Insufficient funds")  # Prints error if withdrawal exceeds balance
    elif amount <= 0:
        print("Invalid amount")  # Prints error for invalid withdrawal amount
    else:
        balance -= amount  # Deducts amount from balance
        print(f"Transaction successful. Your new balance is: {balance}")  # Prints success message
```

**Problems:**
- **Hardcoded I/O:** Relies on `input()` and `print()`, making it hard to test.
- **No Clear Inputs/Outputs:** No parameters or return values, making testing scenarios difficult.

---

#### Refactored Testable Code ✅
```python
def atm_withdrawal(balance, amount):
    # Checks if withdrawal amount exceeds balance
    if amount > balance:
        return "Insufficient funds", balance
    # Checks if withdrawal amount is invalid (non-positive)
    elif amount <= 0:
        return "Invalid amount", balance
    else:
        # Deducts amount from balance and returns success message
        balance -= amount
        return "Transaction successful", balance
```

**Improvements:**
- **Clear Inputs and Outputs:** Accepts `balance` and `amount` as parameters and returns results.
- **No Side Effects:** No reliance on external systems like user input or print statements.

---

### Writing Tests for the Refactored Code 🧑‍💻

Using the `unittest` framework, you can write tests to verify the function's behavior under different scenarios.

```python
import unittest
from atm import atm_withdrawal  # Imports the function to be tested

class TestATMWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        # Simulates withdrawal exceeding balance
        message, new_balance = atm_withdrawal(100, 150)
        self.assertEqual(message, "Insufficient funds")  # Verifies error message
        self.assertEqual(new_balance, 100)  # Verifies balance remains unchanged

    def test_invalid_amount(self):
        # Simulates invalid withdrawal amount
        message, new_balance = atm_withdrawal(100, -20)
        self.assertEqual(message, "Invalid amount")  # Verifies error message
        self.assertEqual(new_balance, 100)  # Verifies balance remains unchanged

    def test_successful_transaction(self):
        # Simulates successful withdrawal
        message, new_balance = atm_withdrawal(100, 50)
        self.assertEqual(message, "Transaction successful")  # Verifies success message
        self.assertEqual(new_balance, 50)  # Verifies updated balance

if __name__ == "__main__":
    unittest.main()  # Runs the test cases
```

---

### Key Principles for Writing Testable Code 📜

1. **Avoid Side Effects:** Minimize interactions with external systems like files, databases, or user input.
2. **Clear Inputs and Outputs:** Functions should accept parameters and return results for predictability.
3. **Small, Focused Functions:** Keep functions concise and focused on a single responsibility.
4. **Use Dependency Injection:** Pass external dependencies (e.g., database connections) as parameters to enable mocking during tests.
5. **Write Tests in Parallel:** Develop tests alongside your code to ensure correctness from the start.

---

### Why This Approach Works 🚀

- **No Dependencies:** The function is independent of external systems.
- **Easy to Verify:** Returns values that can be checked in tests.
- **Separation of Concerns:** Focuses solely on withdrawal logic, making it easier to reason about and test.

By following these principles, you can write code that is both reusable and testable, ensuring higher quality and maintainability in your projects. 🛠️
