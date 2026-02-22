# #Teoria
num1 = 20
if num1 > 10:
    print("This is over 10")
elif num1 == 10:
    print("This is equals to 10")
else:
    print("This is under 10")

num = int(input("Enter a number between 10 and 20: "))
if num>= 10 and num <= 20:
    print("Thank you")
else:
    print("Out of range")
#aqui se usa "and", means que tienen que ser ciertas para imprimir

num = int(input("Enter an EVEN number between 1 and 5: "))
if num == 2 or num == 4:
    print("Thank you")
else:
    print("Incorrect")
#aqui se usa "or", means que al menos tiene que se un numero par
#para que se cumpla

num = 30
if num >= 10:
    if num <= 20:
        print("This is between 10 and 20")
    else:
        print("This is over 20")
else:
    print("This is under 10")

text = str.lower(text) #Changes the text to lower case.

num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Out of range")    
# This use and. Both conditions mut be met

num = int(input("Enter a number between 10 and 20: "))
if num >= 10 or num <= 20:
    print("Thank you")
else:
    print("Out of range")    
# This use or. Just one conditions mut be met


##Challenges

#012 CORRECT
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num2, "and" , num1)
else:
    print(num1, "and" , num2)

#013 Correct
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

#014 Correct
num = int(input("Enter a number between 10 and 20 (inclusive): "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

#015 Correct
colour = input("Please enter your favourite colour: ").lower()
if colour == "red":
    print("I like red too")
else:
    print("I dont like", colour,", I prefer red")
#My code is better because .lower() handles all capitalization variants (like "rEd"), 
#making it more robust and much cleaner.

#An alternative approach (Nichola's answer)
colour = input("Please enter your favourite colour: ").lower()
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print("I dont like that colour, I prefer red")

#Use .casefold() for "aggressive" matching; it’s more reliable than .lower() for international characters.

#016 Correct
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

#Chaining .lower() directly to the input() function is better practice than reassigning
#variables, as it reduces redundancy and potential errors.

#017 Correct
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

#018 Correct
number = int(input("Please write a number: "))
if number < 10:
    print("Too low")
elif number >= 10 and number <= 20:
    print("Correct")
else:
    print("Too high")

#019
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