# ============================================================
# THEORY: DATA TYPES & ARITHMETIC OPERATORS
# ============================================================

## 1. ARITHMETIC OPERATORS
num1 = 45
num2 = 10

# Basic Operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division Types
division = num1 / num2        # Floating-point division (Result: 4.5)
floor_division = num1 // num2 # Floor division: truncates toward the lower integer (Result: 4)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Decimal Division:", division)
print("Floor Division (Integer):", floor_division)

## 2. SPECIAL CHARACTERS
# Use '\n' to create a line break within a string.
print("First Line\nSecond line")

## 3. INPUTS AND DATA TYPES
# String (Default): Stores text.
text_value = input("Enter a text value: ")
print("Text stored:", text_value)

# Integer (int): Stores whole numbers. Use int() to convert input.
num3 = int(input("Enter a whole number: "))
print("Integer stored:", num3)

# Floating Point (float): Stores decimal or fractional numbers.
num4 = float(input("Enter a decimal number: "))
print("Float stored:", num4)

