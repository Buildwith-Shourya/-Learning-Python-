# def greet():
#     print("Hello, welcome to Python!")

# greet()   # ← this is calling the function


# def addition(a,b):  # parameters 
#     print(a + b)


# addition(10,20)    # arguments
# addition(50,50) 


def palindrome_checker(a):
    copy = a 
    rev = 0 

    while a > 0:
        rev = rev * 10 + a%10 
        a = a //10 

    if copy == rev:
        print(f"{copy} is a palindrome number")
    else:
        print(f"{copy} is not a palindrome")

palindrome_checker(121)
palindrome_checker(456)
palindrome_checker(324)
