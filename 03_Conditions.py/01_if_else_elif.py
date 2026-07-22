#Simple if statement 

age = int(input(" Enter your age :- "))

if age >=18:
    print("you are eligible for driving") 


# Simple else statement with if 

Age = int(input(" Enter your age :- "))
if Age >= 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")    

#  Mixed statement with elif 

percentage = int(input(" how many percentage you got :-"))

if percentage >= 75:
    print(" you are eligible to give JEE advance ")


elif percentage >= 60:
    print(" you are eligible for NDA exam ")  


else:
    print(" you are eligible for private collages") 


# Example 
Money = int(input("Enter how much money you have: "))

if Money >= 300:
    print("You can eat pizza")

elif Money >= 100:
    print("You can eat noodles")

elif Money >= 50:
    print("You can eat burger")

elif Money >= 20:
    print("You can eat ice cream")

else:
    print("You eat Ghar ka khana")     

