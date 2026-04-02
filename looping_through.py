import time as tm
#for x in range-type of practice
#Self - inflected task: Make a list or tuple with colors and print each one along with a message for it
colors = ["red","yellow","purple","orange","green"]
for color in colors:
    print(f"Hey! {color.title()} you're shining!")
    print(f"Until Next time, {color}\n") #Second message runs after first and takes the same previous color
        
print("end of the loop\n") #This is not inside the block of code, therefore it'll be treated as nothing more than a
#print statement, but since it is after the loop, it will wait until the loop ends to be printed.

#you learned that for 'x' in range or for 'x' in 'y' is a LOOP,meaning it'll run each statement
#until something stops it, it reaches the end, or it runs out of parameters like a list
#So you just need to print an f-string one for a message for each 'x' inside a list, since
#lets remember once it finds that value, it skips to the other one.
#This way the loop 'for x in range y' will assign each value of y to the variable 'x'
#and therefore run each statement underneath until x is completely empty
#In this case, x will be each color, and we print a message for it ONCE because
#the loop will go back to top each time it ends, and it'll only stop until x = nothing, aka until green's turn
tm.sleep(3)#Hold for next example
pizzas = ["Pepperoni","Mexican","Meat","Extra Cheese"]
for pizza in pizzas:
    print(f"I like {pizza}!")
    
print(f"I like all these pizzas! {pizzas}") #If it were to be the variable assigned (aka pizza) it will just print the last 
#processed value, which is 'extra cheese'
tm.sleep(3)

animals = ["Cat","Dog","Turtle"]
for animal in animals:
    print(f"This {animal} would make a great pet!")

print(f"Any of these animals {animals} would make a great pet!")
