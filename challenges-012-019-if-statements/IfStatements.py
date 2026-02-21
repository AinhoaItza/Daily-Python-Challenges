#Teoria
num1=20
if num1 > 10:
    print("This is over 10")
elif num1 == 10:
    print("This is equals to 10")
else:
    print("This is under 10")

num=int(input("Enter a number between 10 and 20: "))
if num>= 10 and num <= 20:
    print("Thank you")
else:
    print("Out of range")
#aqui se usa "and", means que si o si tienen que ser ciertas para imprimir el thank you

num=int(input("Enter an EVEN number between 1 and 5: "))
if num == 2 or num == 4:
    print("Thank you")
else:
    print("Incorrect")
#aqui se usa "or", means que al menos tiene que se un numero par (2 o 4) para que se cumpla
