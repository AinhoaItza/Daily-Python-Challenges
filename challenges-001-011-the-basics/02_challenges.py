# ============================================================
# CHALLENGES 001 - 011: THE BASICS
# ============================================================

## 001 - Hello Name - CORRECT
firstname=input("Enter your first name: ")
print("Hello, ", firstname)

## 002 - Full Name - CORRECT
surname=input("Enter your surname: ")
print("Hello, ", firstname, surname)

## 003 - Joke Output - CORRECT
print("What do you call a bear with no teeth?\nA gummy bear!")

## 004 - Addition - CORRECT
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
answer=num1+num2
print("The total is: ", answer)

## 005 - Sum and Multiply - CORRECT
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the thrid number: "))
sum=num1+num2
multiply=sum*num3
#answer = (num1+num2)*num3 #MEJOR MANERA de hacerlo pero bien
print("The answer is: ", multiply)

## 006 - Pizza Slices - CORRECT
num1=int(input("How many slices of pizza did you have at the beggining: "))
num2=int(input("How many slices have you eaten so far: "))
answer=num1-num2
print("You can still enjoy ", answer, " pizza slices. Lucky one!")

## 007 - Next Birthday - CORRECT
name=input("Could you tell me your name, please?: ")
age=int(input("Could you tell me your age, please?: "))
futureage=age+1
print(name, "next birthday you will be ", futureage)

## 008 - Bill Splitter - CORRECT
# Using float for the bill is better practice as prices usually have decimals
bill=float(input("Could you please tell me the total price of the bill?:")) 
diners=int(input("How many diners are seated at the table?:"))
answer=bill/diners
print("Each of the diners may pay", answer,"€ for the bill")

## 009 - Time Converter - CORRECT
days=int(input("Tell me how many days are in a week:"))
hours=24*days
minutes=hours*60
seconds=minutes*60
print(days, "days contain", hours, "hours,", minutes, "minutes and", seconds, "seconds in total.")

## 010 - Weight Converter - CORRECT
weightkilo=float(input("Enter a weight in kilograms: "))
pounds=weightkilo*2.204
print("The kilograms you enter are equal to ",pounds,"pounds")

## 011 - Integer Division - WRONG
bignumber = int(input("Please enter a number over 100: "))
smallnumber = int(input("Now enter a number under 10: "))
# Use floor division (//) to see how many times the small number fits into the large one
answer = bignumber / smallnumber #WRONG 
print("The small number", smallnumber, "goes into the large number", bignumber, ",", answer, "times.")
