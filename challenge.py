input1 = input("Provide a string:\n")
input2 = input("Provide another string:\n")
comparison1 = " "
comparison2 = " "
def attempt1():
  for char in input1:
    if char in input2:
        comparison1 += char
    else:
       return(False)
def attempt2():
  for char in input2:
    if char in input1:
        comparison2 += char
    else:
        return(False)
print("If any characters are the same, they will be outputed, else, they will not")
def final_output():
   if attempt1 == "False":
      print("They do not coincide at all")
   else:
      print(comparison1,comparison2)
def main():
   attempt1()
   attempt2()
   final_output()
main()      