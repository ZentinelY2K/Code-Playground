#Brute-froce password guesser, for educational pruposes, i DO NOT support any type of malicious intent
from random import * #import the random library
from string import * #import the string library
username = "C00lDude123" #create username variable
password = "123539" #create password variable, for better results make it simple and no dictionary words like the one provided
expand = digits  #create expand variable to combine digits and letters
attempt = 0 #attempt counter, create variable to be increased inside the loop
found = False #set a variable to determine if password has been cracked
print("Waiting...")
while not found: #loop
    brute_force_guesser = ''.join(choice(expand) for _ in range(len(password)))  #all methods in a variable
    attempt += 1 #attempt counter increases by a factor of one
    
    if brute_force_guesser == password: #check for congruence
        print(f"Password has been found, your username: {username} your password {brute_force_guesser}") #print statement + password
        print(f"And took {attempt} number of attempts") # attempt counter output/result
        found = True #set found to True
    if found == True:
        print("Password was cracked with 100% success!") #check for found being True with print statement


        
