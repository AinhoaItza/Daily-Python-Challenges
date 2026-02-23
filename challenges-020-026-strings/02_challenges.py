# ============================================================
# CHALLENGES 020 - 026: STRINGS
# ============================================================

# ## 020 Correct
name = input("Enter your first name: ")
length = len(name)
print(length)
# another way that I thought about it
name = len(input("Enter your first name: "))
print(name) # It is shorter, more efficient, and avoids unnecessary variable type changes.


## 021 Correct
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
length = len(name)
print(name)
print(length)

## 022 Correct
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)

## 023 Correct
phrase = len(input("Please write the first line of a nursery rhyme: "[0:21]))
print("This has", phrase, "letter in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number"))
part = (phrase[start:end])
print(name)

## 024 Correct
word = input("Enter a word: ")
word = word.upper
print(word)

## 025 Correct
name = input("Enter your first name: ")
if len(name) < 5:
    surname = input("Enter your surname: ")
    name = name+surname
    print(name.lower())
else:
    print(name.lower())

## 026
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())    
#only challenge so far that I didn't know how to start

# another way that I thought about it
word = input("Please enter a word: ").lower() # Convertimos a minúsculas de una vez
first = word[0]
rest = word[1:] # No necesitas len(), el vacío indica "hasta el final"
if first in "aeiou": # Comprueba si la letra está dentro de las vocales
    newword = word + "way"
else:
    newword = rest + first + "ay"
print(newword)
