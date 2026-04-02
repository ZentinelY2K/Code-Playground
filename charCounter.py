message = input("Please provide a sentence:\n")
character = input("Now just a single character please:\n")
counter = 0
def run_or_not():
   if len(character) == 1:
      return(True)
   else:
      return(False)
if run_or_not():
  for char in message:
      if char.lower() == character.lower():
        counter += 1
      else:
          continue
elif run_or_not() == False:
   print("Remember to just input a single character")
print(f"{character} appeared a total of: {counter} times in {message}")