
def remove(string):
    return string.replace(" ", "")
def registration():
    user_name = str(input("Enter user name : "))
    
    if remove(user_name).isalpha():
        print(f"User name : {user_name}")
    else:
        print("Enter correct user name \U0001f612")
        registration()
    Address = str(input("Enter Address : "))
    aadhar = int(input("Enter Aadhar number : "))
    mobile = int(input("Enter Mobile number : "))

registration()

# Take user name
# Address
# Aadhar 
# Mobile no
# print(remove("AJeet Kumar").isalpha())