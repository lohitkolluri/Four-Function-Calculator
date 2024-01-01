<h1 align="center" id="title">Arbitrary Precision Four Function Calculator</h1>

<p id="description">The Arbitrary Precision Four-Function Calculator is a custom implementation capable of handling large integers with arbitrary precision. It allows performing basic arithmetic operations such as addition subtraction multiplication and division on numbers of any size.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Arbitrary Precision
*   Basic Arithmetic Operations
*   Exponentiation and Nth Root
*   Temperature Conversion
*   Memory Functions

<h2>🛠️ Installation Steps:</h2>

1. **Create BigInt Instances:**
   ```python
   num1 = BigInt("12345678901234567890")
   num2 = BigInt("98765432109876543210")
   ```

2. **Perform Arithmetic Operations:**
   ```python
   result = num1 + num2
   result = num1 - num2
   result = num1 * num2
   result = num1 / num2
   ```

3. **Exponentiation and Root:**
   ```python
   result = num1 ** 3  # num1 raised to the power of 3
   result = num1.root(2)  # Calculate the square root of num1
   ```

4. **Temperature Conversion:**
   ```python
   celsius = num1.to_celsius()
   fahrenheit = num1.to_fahrenheit()
   ```

5. **Memory Functions:**
   ```python
   num1.memory_store()  # Store num1 in memory
   result = num1.memory_recall()  # Recall the number stored in memory
   num1.memory_clear()  # Clear the memory
   ```

6. **Command Line Interface:**
   ```
   Enter the first number: 12345678901234567890
   Enter the second number: 98765432109876543210
   Enter the operator (+, -, *, /, ^, root, to_celsius, to_fahrenheit, memory_store, memory_recall, memory_clear): +
   Result: 111111111111111111100
   ```
<h2>🛡️ License:</h2>

This project is licensed under the [MIT License](LICENSE)
