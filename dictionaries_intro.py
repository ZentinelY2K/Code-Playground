"""#simple pizza dictionary
restaurant_pizzas = {"Cheese": 1, "Pepperoni": 2, "Meat": 3}
x = restaurant_pizzas
print(x)
#add
restaurant_pizzas['Hawaian'] = 4
restaurant_pizzas["Specials"] = 5
print(x)"""
from random import randint
counter = 0
new = {}
for i in range(0,100):
    x = randint(1,100)
    new["Number"] = x
    counter +=1 
    print(f"ID: {new['Number']}",f" Status:{counter}")
 