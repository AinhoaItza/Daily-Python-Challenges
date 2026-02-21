# #Teoria
# num1 = 20
# if num1 > 10:
#     print("This is over 10")
# elif num1 == 10:
#     print("This is equals to 10")
# else:
#     print("This is under 10")

# num = int(input("Enter a number between 10 and 20: "))
# if num>= 10 and num <= 20:
#     print("Thank you")
# else:
#     print("Out of range")
# #aqui se usa "and", means que tienen que ser ciertas para imprimir

# num = int(input("Enter an EVEN number between 1 and 5: "))
# if num == 2 or num == 4:
#     print("Thank you")
# else:
#     print("Incorrect")
# #aqui se usa "or", means que al menos tiene que se un numero par
# para que se cumpla

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