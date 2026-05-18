import time as tm
import random as rm
digits = ['1','2','3','4','5','6','7','8','9','0']
store_digits = []

for i in range(0,100000000000000000000000000000000000):
    first_choice = rm.choice(digits)
    store_digits.append(first_choice)
    
    second_choice = rm.choice(digits)
    store_digits.append(second_choice)
    
    third_choice = rm.choice(digits)
    store_digits.append(third_choice)
    
    fourth_choice = rm.choice(digits)
    store_digits.append(fourth_choice)
    
    fifth_choice = rm.choice(digits)
    store_digits.append(fifth_choice)
    
    
    choice = ''.join(store_digits)
    
    if choice == '22435':
       
        print(i,choice)
        break

    else:
        pass

    store_digits = []