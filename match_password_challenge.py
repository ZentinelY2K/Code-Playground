import os
file = 'password_of_user.txt'
choice = input("Do you wish to create a new password?")
if choice == 'No':
    input_of_user = input("Please provide current password:\n")
    if os.path.exists(file) == False:
       open_file = open(file,"w")
       open_file.write(input_of_user)
       print("Succesfully created password!")
    else:
       read_file = open(file,'r')
       read_file = read_file.read()
       if read_file == input_of_user:
            print("Access granted!")
       else:
            print("Access Denied")
elif choice == "Yes":
    input_of_user = input("Please create a new password:\n")
    open_file = open(file,"w")
    open_file.write(input_of_user)
    print("Succesfully created password!")