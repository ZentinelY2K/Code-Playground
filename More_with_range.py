import math as mt
import time  as tm
#Now lets continue with range but try to jump using a third argument
for test in range(0,11,2):
    print(f"{test}\n")#This should only print 5 numbers (plus 0) since 0-10 jumping by two is 2*5

#Working with lists and ranges
#Lets make a list that stores every perfect squares in existance
tm.sleep(1)
perfect_squares = [] #Empty list used to store values
for squares in range(0,11): #For loop that will run each number from 0-10
    multiplier = squares * squares #This multiplies each number by itself as the loop goes
    perfect_squares.append(multiplier) #The append funciton adds each multiplied number(result) to the perfect_square list
    print(f"{multiplier} is a perfect square") #print statement
print(perfect_squares) #At the end of the loop we print our list