file_name = 'Text.txt' 
wtd = input("Enter what to do (Add/Update/Delete): ")


'''with open('Text.txt', 'r') as file:
    Pass = file.read()'''
Pass=""
def clear_data(file_name):
    with open(file_name, 'w') as file:
        file.write("")


if wtd == "Add":
    
    if Pass == "":
      Pass = input("Enter Pass: ")
      with open('Text.txt', 'a') as file:
        file.write(Pass)
        print("Your Password is Created")
    else:
        print("Pass is already Created")
    
elif wtd == "Update":
    Old_pass = input("Enter Old Password: ")
    if  Old_pass==Pass   :
        clear_data("Text.txt")
        Pass = input("Enter New Password: ")
        with open('Text.txt', 'a') as file:
          file.write(Pass)
    else:
        print("Incorrect old password.")
elif wtd == "Delete":
    Old_pass = input("Enter Old Password: ")
    if Old_pass == Pass:
        clear_data("Text.txt")
        print("Password deleted.")
    else:
        print("Incorrect password.")
else:
    print("Invalid option.")



