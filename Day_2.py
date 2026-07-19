# String slicing

name = "shouryajeet singh" 
# If i want to print only shouryajeet then i'll do slicing
print(name[0:11:1]) 


#Implicit-> in this python automatically turns a data type to another datatype

a = 12
b = 2
print(a/b) 

#Explicit -> in this we use buildin fungtions for data type conversion

a = 95123
a = str(a)
print(type(a))  

#Operator -> 
#1 arithmatic Operator -> 7 arithmatic operator

a = 10
b = 20
print(a+b)  # -> addition
print(a-b)  # -> substraction
print(a*b)  # -> multiplication
print(a/b)  # -> division
print(a//b) # -> Florr division
print(a%b)  # -> Modulus
print(a**b) # -> Exponential

#2 Compound Assignment operator -> these are the shortcut of operator 

# EG :-
a = 10
a+=12
print(a)  


#3 Comparision Operator 
 
a = 12
b = 12 
print(a==b) 
print(a!=b)

c = 50
d = 100

print(c<d)
print(c>d)  

print(45<=45) 
print(45>=50) 

# Logical Operator 

#1. and -> return true if all are true condition 

print(23==23 and 45==45 and 10<50) 

#2. or -> return true if atleast one condition is true 

print(23==50 or 50<100  or 200>10000) 

#3. not -> it converts a true value into false 

print( not 200==200) 



# ---  Conditional Statement 
#-----
#-------

money = int(input("provide money :- ")) 

if money == 10:
    print(" i will eat choco bar")

elif money == 20:
    print(" i will eat mango dolly")  

elif money == 30:
    print(" i will eat chochlate cone")    

else:
    print(" i will eat burger")    



  




