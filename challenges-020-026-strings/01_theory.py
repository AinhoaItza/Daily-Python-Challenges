# =============================
# THEORY: IF STATEMENTS 
# =============================

# num = input("Enter a number: ")
# num = int(num)
# # we can convert it to a number after it has been created using this line
# total = num + 10
# print(total)

# # An alternative approach (The one I have being using until now)
# # Define it as a number when the variable is being created.
# num = int(input("Enter a number: "))
# total = num + 10
# print(total)

# # Another way would be convert it to string
# name = input("Enter a name: ")
# num = int(input("Enter a number: "))
# num = str(num)
# ID = name + num
# print(ID)

# Multiple-Line Strings
# For multiple-line strings we can either use the line break (\n) 
# or enclose the entire thing in triple quotes. This will preserve the formatting of the text
address = """123 Long Lane
Oldtown
AB1 23CD"""
print(address)

# Example Code

len(word) # Finds the lengh of the variable called word.
word.upper() # Changes the string into upper case.
print(word.capitalize()) # Display variable so only the firts word has a capital 
# letter at the beginning.
word.lower() # Changes the string into lower case.
name = firstname+surname # Joins the first name and surname together without a 
# space between them (concatenation).
word.title() # Changes a phare so that every word has a capital letter at the beginning
# with the rest of the letters in lower case.
text = " This is some text. "
print(text.strip(" ")) # Removes extra characters (in this case spaces) from the start 
# and end of a string.
print("Hello world"[7:10]) # Each letter is assigned an index number to identify its 
# position in the phase, including the space.
# Python starts counting from 0, not 1. Therefore, in this example, it would display the
# value of 7,8 and 9, which is "orl".

