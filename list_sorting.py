import time as tm
#List sorting
list_testing = ["b","x","f","a"] #We set up our list
list_testing.sort()#This permanently puts the list in alphabetical order
print(list_testing)
tm.sleep(1)# this just for aesthetics
list_testing.sort(reverse = True)#This permanently reverses the list
print(list_testing)
tm.sleep(1)
#This does it for one line, but not for the other one (not permanently) + You gotta do sorted first
sorted(list_testing)
print(list_testing)
tm.sleep(1)
print(f"""{list_testing} This line cannot go back to its original state, because we used
           'sort' which permanently changes the list for bad or for good""")
tm.sleep(1)
list_testing.reverse() #This doesnt change anything alphabetically, it just does it by changing from 0-x to x-0 (reverse)
print(list_testing)