# ============================================================
# CHALLENGES 012 - 019: IF STATEMENTS
# ============================================================


## 012 - Number Comparison - CORRECT
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num2, "and" , num1)
else:
    print(num1, "and" , num2)

## 013 - Under 20 Validation - Correct
num1 = int(input("Please enter a number under 20: "))
if num1 < 20:
    print("Thank you")
else:
    print("Too high")

#An alternative approach (Nichola's answer)
num1 = int(input("Please enter a number under 20: "))
if num1 >= 20:
    print("Too high")
else:
    print("Thank you") 

## 014 - Range Check (10-20) - Correct
num = int(input("Enter a number between 10 and 20 (inclusive): "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

## 015 - Favourite Colour - Correct
colour = input("Please enter your favourite colour: ").lower()
if colour == "red":
    print("I like red too")
else:
    print("I dont like", colour,", I prefer red")
# My approach is more robust as .lower() handles all capitalization variants (e.g., "rEd").
# Use .casefold() for even more aggressive matching with international characters.

#An alternative approach (Nichola's answer)
colour = input("Please enter your favourite colour: ").lower()
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print("I dont like that colour, I prefer red")


## 016 - Weather Advisor - Correct
# Chaining .lower() directly to input() is cleaner and avoids reassigning variables.
weather = input("Could you tell me if is raining in your location right now?: ").lower()
if weather == "yes":
    windy = input("Could you tell me if is windy in you location right now: ").lower()
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

#An alternative approach (Nichola's answer)
raining = input("Is it raining?: ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy?: ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")



## 017 - Age Permissions - Correct
age = int(input("How old are you?: "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
elif age < 16:
    print("You can go Trick-or-Treating")

#An alternative approach (Nichola's answer)
age = int(input("How old are you?: "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")

#Both versions are logically equivalent, but Nichola's else is more efficient as it acts as 
#a catch-all without needing an extra comparison."

## 018 - Number Range Categorization - Correct
number = int(input("Please write a number: "))
if number < 10:
    print("Too low")
elif number >= 10 and number <= 20:
    print("Correct")
else:
    print("Too high")

## 019 - Choice Selection - Correct
num1 = 1
num2 = 2
num3 = 3
answer = int(input("Please enter 1, 2 or 3: "))
if answer == num1:
    print("Thank you")
elif answer == num2:
    print("Well done")
elif answer == num3:
    print("Correct")
else:
    print("Error message")

#An alternative approach (Nichola's answer)
answer = input("Please enter 1, 2 or 3: ")
if answer == "1":
    print("Thank you")
elif answer == "2":
    print("Well done")
elif answer == "3":
    print("Correct")
else:
    print("Error message")

#Nichola's approach is more robust because it avoids a "ValueError" if the user enters a letter, 
#though my version is better for mathematical scalability.