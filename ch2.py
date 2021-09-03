# Python Basics Chapter 2:
# ========================

# 1. String Concatenation

# Collecton of characters inside single quotes or double quotes.

# # first = "Anshul"
# # last = "Garg"

# full = first + last
# full = first + " " + last
# full = first + "\t" + last
# print(full)
# print(type(full))

# print("Anshul" + " " + "Garg")

# print(first + 2) -> Error
# print(first + "2")
# print(first + str(2))

# print(first * 3)

# 2. User Input

# name = input("Type Your Name : ")

# print(name)
# print("Hello " + name)

# age = input("Your Age : ")

# print(age)
# print("Your Age Is : " + age)
# print(type(age))

# Type Casting

# age = "21"

# Type Conversion

# print(type(age))

# age = int(age)

# print(type(age))

# age = float(age)

# print(type(age))

# age = str(age)

# print(type(age))

# 3. Int() and Float() Functions

# num1 = int(input("First Number : "))
# num2 = int(input("Second Number : "))

# num1 = float(input("First Number : "))
# num2 = float(input("Second Number : "))

# total = num1 + num2
# print("Total Is : " + str(total))

# num1 = str(4)

# num2 = float("44")
# num3 = int("33")

# print(int("1.5")) -> Error

# print(num2 + num3)
# print(num1 + num2 + num3) Error because num1 str

# num = eval(input("Any Number : "))
# print(type(num))

# 4. More About Variables

# name, age = "Anshul", 22
# print("Hello " + name + "\nYour age is " + str(age))

# x = y = z = 1
# print(x + y + z)

# 5. Two Or More Input In One Line

# name, age = input("Enter your name and age separated by space : ").split()
# name, age = input("Enter your name and age separated by comma : ").split(",")
# print("Hello " + name + "\nYour age is " + age) # ugly syntax

# 6. String Formatting

# name = "Anshul"
# age = 22

# {} -> placeholder

# print("Hello {} \nYour age is {}".format(name, age))
# print("Hello {} \nYour age is {}".format(name, age + 2))

# print(f"Hello {name} \nYour age is {age}")
# print(f"Hello {name} \nYour age is {age + 2}")

# 7. Exercise - 1

# Ask user to input 3 numbers and you have to print average of three  
# numbers using string formatting.
# Bonus: Try to take all three comma separated inputs in one line.

# 8. Exercise - 1 Solution

# num1, num2, num3 = input("Three numbers separated by comma : ").split(",")

# average = (int(num1) + int(num2) + int(num3)) / 3
# print(f"Average : {average}")

# 9. String Indexing

# language = "Python"

# positions or index number

# P = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

# print(language)
# print(language[2])
# print(language[4])

# print(language[6])

# print(language[-1])
# print(language[-7]) -> Error

# 10. String Slicing

# lang = "Python"

# Syntax - [start argument : stop argument]

# print(lang[0 : 2])
# print(lang[2 : 6])

# print(lang[0 : -4])
# print(lang[-4 : 6])

# print(lang[-4 : ])
# print(lang[-6 : -4])

# print(lang[-4 : -6])

# print(lang[ : ])
# print(lang[2 : ])
# print(lang[ : 2])

# print(lang[ : 6])
# print(lang[7 : ])

# 11. Step Argument

# Syntax - [start argument : stop argument + 1 : step]

# print("Anshul"[0 : 4])

# print("Anshul"[0 : 6 : 2])
# print("Anshul"[0 : : 2])
# print("Anshul"[0 : : 3])
# print("Anshul"[ : : 3])

# print("Anshul"[5 : : -1])
# print("Anshul"[-1 : : -1])
# print("Anshul"[: : -1])

# 12. Exercise - 2

# Ask user name and print back user name in reverse order.
# Note: Try to make your program in 2 lines using string formatting. 

# 13. Exercise - 2 Solution

# name = input("Your name : ")
# print(f"Your name in reverse order : {name[::-1]}")

# 14. String Methods Part - 1

# name = "AnShUl gArG"

# 1. len() method

# print(f"Length of name : {len(name)}")

# 2. lower() method

# print(f"Name (lower) : {name.lower()}")

# 3. upper() method

# print(f"Name (upper) : {name.upper()}")

# 4. title() method

# print(f "Name (title) : {name.title()}")

# 5. count() method

# print(f"Count : {name.count('A')}")
 
# 15. Exercise - 3

# Take two comma separated inputs from user
# 1. user's name
# 2. a single character

# Output: 2 print lines
# 1. user's name length
# 2. count the character that user inputed 
# Bonus: case insensitive count

# 16. Exercise - 3 Solution

# name, char = input("Your name and a character separated by comma : ").split(",")

# print(f"Length of your name : {len(name.strip())}")
# print(f"Count of character : {name.strip().lower().count(char.strip().lower())}")

# 17. Solve Problem With Spaces Using Strip Method

# name = "    Ansh    ul      "
# dots = "................"

# print(name + dots)
 
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip() + dots)

# print(name.replace(" ", "") + dots)

# 18. Find And Replace Method

string = "she is beautiful and she is good dancer"

# print(string.replace(" ", "_"))
# print(string.replace("is", "was"))
# print(string.replace("is", "was", 1))
# print(string.replace("is", "was", 2))
# print(string.replace("is", "was", 3))

# print(string.find("is"))
# print(string.find("is", 5)) # static

# is_pos1 = string.find("is")
# print(string.find("is", is_pos1 + 1)) # dynamic

# 19. Center Method

# name = "anshul"
# Expected Output: **anshul**

# print(name.center(6, "*"))
# print(name.center(7, "*"))
# print(name.center(8, "*"))
# print(name.center(9, "*"))
# print(name.center(10, "*"))

# name = input("Your name : ")

# print(f"Welcome {name.center(len(name) + 4, '*')}")

# 20. Strings Are Immutable

# string = "python"

# print(string[0])
# print(string[0] = "c")

# print(string.replace("p", "c"))
# print(string)

# 21. Assignment Operators

# name = "Ansh"

# name = name + "ul"
# name += "ul"

# print(name)

# age = 22

# age = age + 2
# age += 2

# print(age)
