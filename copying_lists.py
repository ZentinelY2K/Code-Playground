original = [0,1,2,3,4,5]
copy = original[0:6] #same as below
copy = original[:]
print(copy)
print(original)
favN_original = int(input("Give me a number (original):\n"))
favN_copy = int(input("Give me a number (copy):\n"))
original.append(favN_original)
copy.append(favN_copy)
print(f"original: {original}",f"copy:{copy}")
