# =============================
# THEORY: IF STATEMENTS 
# =============================

## 1. BASIC IF-ELIF-ELSE STRUCTURE
# Use this to check multiple conditions in order.
num1 = 20
if num1 > 10:
    print("This is over 10")
elif num1 == 10:
    print("This is equals to 10")
else:
    print("This is under 10")

## 2. LOGICAL OPERATORS: AND
# 'and' means BOTH conditions must be true to execute the code.
num = int(input("Enter a number between 10 and 20: "))
if num>= 10 and num <= 20:
    print("Thank you")
else:
    print("Out of range")

## 3. LOGICAL OPERATORS: OR
# 'or' means AT LEAST ONE condition must be true.
num = int(input("Enter an EVEN number between 1 and 5: "))
if num == 2 or num == 4:
    print("Thank you")
else:
    print("Incorrect")

## 4. NESTED IF STATEMENTS
# You can put an 'if' inside another 'if' for more complex logic.
num = 30
if num >= 10:
    if num <= 20:
        print("This is between 10 and 20")
    else:
        print("This is over 20")
else:
    print("This is under 10")

## 5. STRING NORMALIZATION
# .lower() ensures that comparisons are not case-sensitive.
# Example: "YES", "Yes", and "yes" all become "yes".
text = str.lower(text) #Changes the text to lower case.

## 6. COMPARISON SUMMARY (AND vs OR)
# AND: num >= 10 and num <= 20 
# (Requires the number to be 10, 11, ..., 20)
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Out of range")    

# OR: num < 10 or num > 20 
# (Triggers if the number is outside the 10-20 range)
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 or num <= 20:
    print("Thank you")
else:
    print("Out of range")    

