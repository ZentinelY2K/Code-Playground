my_dictionary = {"phase1":"X"}
"""
Change x>y
"""
print(my_dictionary['phase1'])#print phase1: x before mutating
my_dictionary["phase1"] = "Y" #assign new value
print(my_dictionary['phase1']) #print new value
del my_dictionary['phase1']#delete value
print(my_dictionary) #print it empty
#But we dont want it empty so we add new value
my_dictionary['new value'] = 'Z' #add new value
print(my_dictionary['new value'])
coordinates = my_dictionary['new value']
print(f"the last coordinates to be printed should've been '{coordinates}'")
#This in case a pair-key value is non existent
error_handler = my_dictionary.get('This doesnt exist','Non Existent Return Error') #get function to manage errors
print(error_handler)