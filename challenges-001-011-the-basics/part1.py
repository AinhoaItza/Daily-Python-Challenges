#Teoria
num1=45
num2=10
answer=num1+num2
answer2=num1-num2
answer3=num1*num2
answer4=num1/num2 #numero decimal
answer5=num1//num2 #trunca hacia abajo al entero más cercano, sin redondear como tal
print("the answer is: ", answer)
print("The answer nº 2 is: ", answer2)
print("The answer nº 3 is: ", answer3)
print("The answer nº 4 is: ", answer4)
print("The answer nº 5 is: ", answer5)

print("First Line\nSecond line") #el comando "\n" separa 

textValue=input("Enter a text value: ") #input es para que el usuario introduzca un valor str
print("El valor introducido es: ", textValue)
num3=int(input("Enter a number: ")) #int(input(..)) es para que el usuario introduzca un valor numerico
print("El valor numerico introducido es: ", num3)
num4=float(input("Enter a number: ")) #float(input(...)) es para que el usuario introduzca un valor flotante o fraccionario
print("El valor flotante introducido es: ", num4)

##Challenges

#001 CORRECT
firstname=input("Enter your first name: ")
print("Hello, ", firstname)

#002 CORRECT
surname=input("Enter your surname: ")
print("Hello, ", firstname, surname)

#003 CORRECT
print("What do you call a bear with no teeth?\nA gummy bear!")

#004 CORRECT
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
answer=num1+num2
print("The total is: ", answer)

#005 CORRECT
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the thrid number: "))
sum=num1+num2
multiply=sum*num3
#answer = (num1+num2)*num3 #MEJOR MANERA de hacerlo pero bien
print("The answer is: ", multiply)

#006 CORRECT
num1=int(input("How many slices of pizza did you have at the beggining: "))
num2=int(input("How many slices have you eaten so far: "))
answer=num1-num2
print("You can still enjoy ", answer, " pizza slices. Lucky one!")

#007 CORRECT
name=input("Could you tell me your name, please?: ")
age=int(input("Could you tell me your age, please?: "))
futureage=age+1
print(name, "next birthday you will be ", futureage)

#008 CORRECT
bill=float(input("Could you please tell me the total price of the bill?:")) #en el resultado ejemplo usa int pero es mejor obv pq un bill tiene decimales casi siempre, asi que good job
diners=int(input("How many diners are seated at the table?:"))
answer=bill/diners
print("Each of the diners may pay", answer,"€ for the bill")

#009 CORRECT
days=int(input("Tell me how many days are in a week:"))
hours=24*days
minutes=hours*60
seconds=minutes*60
print(days, "days contain", hours, "hours,", minutes, "minutes and", seconds, "seconds in total.")

#010 CORRECT
weightkilo=float(input("Enter a weight in kilograms: "))
pounds=weightkilo*2.204
print("The kilograms you enter are equal to ",pounds,"pounds")

#011 WRONG
bignumber = int(input("Please enter a number over 100: "))
smallnumber = int(input("Now enter a number under 10: "))
answer = bignumber / smallnumber #WRONG
#answer = bignumber // smallnumber pq lo que hace es dividir y redonde hacia abajo. es decir, en vez de 10.3 seria 10. 
#Si queremos saber cuántas veces cabe completamente un número pequeño en uno grande (sin importar lo que sobre), usa este.
print("The small number", smallnumber, "goes into the large number", bignumber, ",", answer, "times.")
