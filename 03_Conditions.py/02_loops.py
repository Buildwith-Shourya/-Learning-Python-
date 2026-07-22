# # for loop------------------------
# #print number 0 - 20
# a = range(1,21,1)
# for i in a:
#     print(i)  

# #take input and print table of it 

# a = int(input(" give number to print :- "))  
# for i in range(a,a*10+1,a):
#     print(i) 


# # Using length fungtion

# name = "MITSUBISHI AC VERY POWERFULL"
# print(len(name)) 

# #using other method
# Z = " SAVE WATER SAVE ENVIROMENT"
# for i in range(len(Z)):
#     print(i)

# # One more method
# Q = " i am cool "
# print(len(Q))

# for i in range(len(Q)):
#     print(Q[i])

# #-----------------------------------------------------------------------
# # break statement
# #-----------------------------------------------------------------------

# for i in range(5,55):
#     if i == 26:
#         break
#     print(i)

# #--------------------------------------------
# #continue statement
# #--------------------------------------------

# for i in range(5,55):
#     if i == 25:   # continue -> skips the current iteration of a loop and move to the next iteration
#         continue  # without stopping the loop
#     print(i)


#work of else with break

for i in range(1,21):
    if i == 15:
        print("break statement is executed")
        break    
    print(i)

else:    
    print("break statement is not executed") 
# if break not running then else  run 
# if else not running then break run 
