programming_languages = {"1":"Python",
                         "2":"Java",
                         "3":"Rust",
                         "4":"C",
                         "5":"C#",
                         "6":"C++",
                         "7":"CSS",
                         "8":"HTML",
}
for number, program in programming_languages.items(): #Always remember to use '.items()' 
    print(f"{program} is good to code and it's number in the dictionary is {number}")


"""
Second exercise
"""
print("")
colors_opposite = {
    "Blue":"Red",
    "Black":"White",
    "Pink":"purple",
}
counter = 0
#ALl OF THIS CAN BE SIMPLIFIED AS WE'LL SEE
"""for color, opposite in colors_opposite.items(): 
    #first one is always key, after comma is value
    print(f"{color} is the opposite of {opposite}")
for color,null in colors_opposite.items():
    print(f"Only the color:\n {color}")
for null, opposite in colors_opposite.items():
    print(f"Only the opposite:\n {opposite}")"""
for colors_only in colors_opposite.keys():
    counter +=1
    print(f"{counter} {colors_only} because instead of 'items' which takes\n all key-value pairs we use 'keys' for keys only")