#1 Accept an integer and Print hello world n times

n = int(input(" Enter your number :- "))
for i in range(n):
        print("Hello World")

#2 Print natural number up to n
n = int(input(" Enter your number :- "))
for i in range(1,n+1,1):
    print(i)


#3 Reverse for loop. Print n to 1
n = int(input(" Enter your number :- "))
for i in range(n,0,-1):
    print(i)


#4 Take a number as input and print its table
n = int(input(" Enter a number to print table :- "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#5 Sum up to n terms
n = int(input(" Enter a number :- "))

sum = 0

for i in range(1,n+1):
    sum = sum + i
print(f"your sum is {sum}")    

#6 Factorial of a number
n = int(input(" Enter a number :- "))

fact = 1

for i in range(1,n+1):
    fact = fact * i
print(f" your factorial is {fact}")


#7 Print the sum of all even & odd numbers in a range 
# separately
n = int(input("tell your number "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i

    else:
        odd = odd + i    

print(f"your even and odd sum are {even} , {odd}")        

    

#8 Print all the factors of a number
n = int(input("ENter that number you what to do factor"))
for i in range(1,n+1):
    if n%i == 0:
        print(i)








