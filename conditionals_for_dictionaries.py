#We can use conditionals to work with a dictionary
#Lets try checking for errors in a program (for example) and then remove it out
program_status = {
    "working1":"True",
    "working2": "True",
    "working3":"False",
    "working4": "True",
    "working5": "True"
}
counter = 0
error_dict = {"Error":"working3"}
for working_y_n in program_status.keys():
    counter +=1
    if error_dict["Error"] in working_y_n:
        print(f"{error_dict['Error']} matches {working_y_n} so it was skipped")
        counter -=1
        continue
    else:
        print(f"{working_y_n} is fine")
print(counter)
        