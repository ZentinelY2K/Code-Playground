
#separate
empleoyees = ['A101', 'B202', 'C303', 'S001', 'D404', 'S002'] #list
blacklisted_id = ['C303', 'Z999'] #list to check if excluded
for check in empleoyees: #check is a variable that will go through each of the empleoyees ID
    if check in blacklisted_id: #if the current empleoyee is inside the blacklist
        print(f"ID: {check} is BlackListed, access denied") #if so print it
        continue #skip rest of the code if true
    if check[0] == "S":
        print(f"ID: {check} Granted Level 5 (System Administrator) Clearance.")
    elif check[0] == "A" or check[0] == "B":
        print(f"ID: {check} Granted Level 3 (Standard User) Clearance.")
    else:
        print(f"ID: {check} Granted Level 1 (Visitor) Clearance.")

    