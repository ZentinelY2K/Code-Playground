import time as tm
#For x in range() pracitce from Book
for tenths in range(4):
    print(tenths)
print("This will print numbers: 0,1,2,3\n")
#As you may see, when printed out you'll see 4 numbers, but from 0-3, not 1-4, this, because Python
#always begins from zero, so you'll have to add a number each time to achieve one, for example
#If you want to print the numbers from 0-100, you'd need to do it 0-101 to get 100 printed out
tm.sleep(3)
for hundreds in range (0,101):
    print(hundreds)
print("This will print 0-100\n")
tm.sleep(3)
#Now, we'll be using different functions, the first one turns the results of range into a list
from_range_to_list = list(range(1,6))#Numbers from 1-5 stored inside a list
print(from_range_to_list)
#now we can manipulate the numbers
tm.sleep(1)
del from_range_to_list[1]#Delete number 2
from_range_to_list.insert(1, 1)#Replace number 2 with 1
from_range_to_list.reverse()#Reverse everything backwards
print(from_range_to_list)
#end