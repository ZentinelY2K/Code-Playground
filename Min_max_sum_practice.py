summing = (0,1,2,3,4)
maxing = (0,1,2,3,4)
minimum = (0,1,2,3,4)
x = sum(summing)
y = min(minimum)
l = max(maxing)
def minimum_def ():
   if y == 1:
      return True
   else:
      return False
def summing_def():
   if x == 6:
       return True
   else:
      return False
def maximum_def():
    if l == 3:
      return True
    else:
      return False

one = minimum_def()
two = summing_def()
three = maximum_def()
if one:
   print("True MIN")
else:
   print("False MIN")
if two:
   print("True SUM")
else:
   print("False SUM")
if three:
   print("True MAX")
else:
   print("False MAX")
      
    
    