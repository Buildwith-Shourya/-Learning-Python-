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