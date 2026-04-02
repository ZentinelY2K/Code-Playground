import random as rm
for i in range(0,100):
    x = round(rm.uniform(0,50),2)
    print(x)
    if x >= 2.00 and x <= 3.00:
        print("NOP")
        continue
print(x,"hola")