# ===========================
# Practice Questions - Day 2
# Topic: Conditional Statements
# ===========================

# Q1. Accept two numbers and print the greatest between them.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is:", num1)
elif num2 > num1:
    print("Greatest number is:", num2)
else:
    print("Both numbers are equal")


# --------------------------------------------

# Q2. Accept gender and print greeting message.

gender = input("\nEnter your gender (M/F): ").upper()

if gender == "M":
    print("Good Morning Sir")
elif gender == "F":
    print("Good Morning Ma'am")
else:
    print("Invalid Gender")


# --------------------------------------------

# Q3. Check whether a number is even or odd.

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# --------------------------------------------

# Q4. Check whether the user is a valid voter.

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Hello {name}, you are not eligible to vote.")


# --------------------------------------------

# Q5. Check whether a year is a leap year.

year = int(input("\nEnter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")