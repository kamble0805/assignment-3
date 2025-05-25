# Assignment 3 – Module 4: Functions & Modules in Python

This repository contains two Python scripts developed as part of Assignment 3 for the **Python Tutedude Course – Module 4**.

---

## 📘 Task 1: Calculate Factorial Using a Function

**Description**  
This Python script asks the user to enter a number and calculates the **factorial** of that number using a `for` loop inside a function.

**Functionality**
- Takes user input.
- Defines a function `factorial()` that uses a loop to calculate the factorial.
- Prints the result directly inside the function.

**Code Snippet:**
```python
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")
    
factorial()
```
---
## 📘 Task 2 : Using the Math Module for Calculations

**Description**  
This script takes a number as input and uses Python's built-in math module to perform three operations:
- Find the square root.
- Calculate the natural logarithm.
- Find the sine (in radians).
**Functionality**
- Uses math.sqrt(), math.log(), and math.sin() functions.
- Includes a simple check to avoid math errors if the number is 0 or negative.
**Code snipper :**
  ```python
import math

def main():
    num = int(input("Enter a number: "))
    
    if num <= 0:
        print("Please enter a number greater than 0")
        return

    print("Log:", math.log(num))
    print("Sine:", math.sin(num))
    print("Square root:", math.sqrt(num))

main()
```
