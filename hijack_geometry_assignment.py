choices = ['A','B','C','D','E','F','G','H','I']
import random as rm
import pyautogui as auto
import time as tm
first_string = ''
second_string = ''
third_string = ''
fourth_string = ''

final_1 = " "
list_of_used_codes = [] #avoid repetition
list_ = []
tm.sleep(5) #hurry up and select text box
for i in range(3024):
    choice1 = rm.choice(choices)
    first_string = choice1
    choices.remove(first_string)
    choice2 = rm.choice(choices)
    second_string = choice2
    choices.remove(second_string)
    choice3 = rm.choice(choices)
    third_string = choice3
    choices.remove(third_string)
    choice4 = rm.choice(choices)
    fourth_string = choice4
    choices.remove(fourth_string)

    list_.append(first_string)
    list_.append(second_string)
    list_.append(third_string)
    list_.append(fourth_string)
    
    code = ''.join(list_)
   
    auto.write(code, interval=0.05)

    auto.hotkey("ctrl", "a")   # select all text
    auto.press("backspace")   # or "delete"
    list_ = []
    choices = ['A','B','C','D','E','F','G','H','I']
    