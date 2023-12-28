# Arbitrary Precision Four-Function Calculator

The **Arbitrary Precision Four-Function Calculator** is a custom implementation capable of handling large integers with arbitrary precision. It allows performing basic arithmetic operations such as addition, subtraction, multiplication, and division on numbers of any size.

## Features

1. **Arbitrary Precision:** The calculator can handle large numbers with precision limited only by the available memory.

2. **Basic Arithmetic Operations:** The calculator supports the following arithmetic operations:
   - Addition (`+`)
   - Subtraction (`-`)
   - Multiplication (`*`)
   - Division (`/`)

3. **Exponentiation and Nth Root:** The calculator can raise a number to an integer exponent and calculate the nth root of a number.

4. **Temperature Conversion:** It provides utility functions to convert a number to Celsius and Fahrenheit.

5. **Memory Functions:** The calculator includes memory functions to store and recall numbers for future calculations.

## Usage

To use the **Arbitrary Precision Four-Function Calculator**, follow these steps:

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

## Important Notes

1. The calculator can handle very large numbers with arbitrary precision, but extremely large calculations might take some time to complete.

2. For division operations, the result will be returned as a tuple of two `BigInt` instances - quotient and remainder.

3. The calculator only supports basic arithmetic operations and utility functions. Complex mathematical functions are not included.

4. It can raise a `BigInt` number to an integer exponent, but fractional exponents are not supported.

5. The calculator does not handle invalid input gracefully. Entering invalid numbers or operators may lead to unexpected results or errors.

