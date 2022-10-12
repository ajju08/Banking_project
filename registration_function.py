SpecialSym =['$', '@', '#', '%']
from mysql_connector import mydb, mycursor

def remove(str):
    ''' 
    This Method is for removing all space from string. 
    '''
    return str.replace(" ", "")

def welcome():
    '''
    This is the method for task bar in we print Registration, Log In and Exit
    '''
    print("\n")
    print("___________________________________________________________________________")
    print("************ \U0001f60A Welcome To CheckPaisa Bank \U0001f60A ************")
    print("___________________________________________________________________________")
    print("\n")
    print("Press 1 For Registration ")
    print("Press 2 For Log In  ")
    print("Press 3 For Exit  ")

def name():
    ''''
    This is the method for taking Name as input from user after taking input.
    I use strip function to remove left space and right space .
    after that call remove function to remove all space from that string. 
    and by using isalpha function to check any other character other than alphabet is present or not 
    '''
    while True:
                try: 
                    ut1 = input("Enter Your Name Here : ")
                    ut2 = ut1.strip()
                    ut = remove(ut1)
                    if ut.isalpha() :
                        break
                    else:
                        raise TypeError 
                except TypeError:
                    print("Numeric or Special Character are not allowed like . , @ # < > ? / ; ")
    return ut2

def username():
    '''
    This is method for taking input for username 
    '''
    while True:
                try:
                    a='.'
                    a1='#'
                    a2='$'
                    a3='*'
                    a4='&'
                    a5='='
                    a6=','
                    a7='!'
                    a8='?'
                    a9='@'
                    a10=' '
                    p=input("Enter Your User Name : ")
                    if(a in p) or (a1 in p) or (a2 in p) or (a3 in p) or (a4 in p) or (a5 in p) or (a6 in p) or (a7 in p) or (a8 in p) or (a9 in p) or (a10 in p):
                        raise TypeError 
                    break
                except TypeError as m:
                    print("Special Character are not allowed like . ,@ # $ % * & = < > ? !")
    return p

def password():
    '''
    In this we check length of password , care about space , Upper case , lower case, special character and Numeric 
    '''
    while True:        
                try:

                    z=input("Enter Your Password : ")
                    if (len(z)<6):
                        raise ValueError (" Password should contain at least 6 character ")
                    if (' ' in z):
                        print("Please don't press space")
                        z=password()
                    if not any(char.isdigit() for char in z):
                        raise ValueError ("Password should atleast a number")
                    if not any(char.isupper() for char in z):
                        raise KeyError ()
                    if not any(char.islower() for char in z):
                        raise KeyError
                    if not any(char in SpecialSym for char in z ):
                        raise KeyError
                    break
                except ValueError:
                    print("Password should contain atleast 1 upper case, 1 Lower Case , 1 number, 1 Special Character  and Password Must Contain atleast 7 character")
                except KeyError:
                    print("Password should contain atleast 1 upper case, 1 Lower Case ,1 number, 1 Special Character  and Password Must Contain atleast 7 character")
    return z

def balance():
    '''
    In this if balance is negative it shows balance is less than zero care about taking input only take integer value
    '''

    while True:
                try:
                    try:
                        k=int(input("Enter the Amount of money you want to deposit : "))
                    except:
                        print("Please Enter the value ! \U0001F642 ")
                    if (k<=0) :
                        print('\n')
                        print("Amount less than Zero does not exist in the real world. Only you can think! \U0001F642 ")
                        print('\n') 
                    else:
                        break              
                except:
                    print("Please write correct value !")
    return k

def address():
    '''
    Address not contain Special Character like '!','@','#','$','%','^','*','=','_','?','<','>','?'
    '''
    s=input("Enter Your Address : ")
    a=['!','@','#','$','%','^','*','=','_','?','<','>','?']
    if any(char in a for char in s):
        print("Special Character are not allowed like '!','@','#','$','%','^','*','=','_','?','<','>','?'")
        s=address()
    
    return s

def mobile():
    '''
    mobile starting with 0 to 6 are not valid and length of number is exactly equal to 10
    '''
    try:
        d=int(input("Enter Your Phone Number : +91-"))
        if len(str(d))!=10 or int(str(d)[0]) in list(range(0,6)):
            print("Pls enter a valid 10 digit Number")
            d=mobile()
    except :
        print('Mobile number is not valid')
        d=mobile()

    return d

def aadhar():
    '''
    Aadhar Number exactly equal to 12 are valid and should not start with zero
    '''
    # try:
    #     f=int(input("Enter Your 12 Digit Aadhar Number Without putting space  : "))
    #     # if(len(str(f))!=12) or (str(f).isalpha()) or (int(str(f)[0])!=0):
    #     if(len(str(f))!=12)): #or (int(str(f)[0])==0):
    #         print("Please Enter a valid 12 digit aadhar Number and should not start with 0")
    #         f=aadhar()
    # except:
    #     print("Aadhar Number is not valid! ")
    #     f=aadhar()
    while True:
        try:
            f=int(input("Enter Your 12 Digit Aadhar Number Without putting space  : "))
            if(len(str(f))!=12) or (f.isalpha()):
                raise ValueError ("Please Enter a valid 12 digit aadhar Number")
            break
        except ValueError as m:
            print(m)
    return f

def registration_confirmation(name,password,balance,address,mobile,aadhar):
    '''
     =This function is taking the inputs entered at the time of registration & inserting the values into the database table.
     :param name: This is name of the user entered at the time of registration.
     :param password: This is password of the user entered at the time of registration
     :param balance: This is balance of the user entered at the time of registration
     :param address: This is address of the user entered at the time of registration
     :param mobile: This is mobile number of the user entered at the time of registration
     :param aadhar: This is aadhar number of the user entered at the time of registration
    '''
    q="insert into account_details (name,password,balance,address,mobile,aadhar) values('{}','{}','{}','{}','{}','{}')".format(name,password,balance,address,mobile,aadhar)
    mycursor.execute(q)
    mydb.commit()
    ad="select account_number from account_details where name='{}' and password ='{}' ".format(name,password)
    mycursor.execute(ad)
    a=mycursor.fetchone()[0]
    lb="insert into list_of_beneficiaries (account_number) values ({}) ".format(a)
    mycursor.execute(lb)
    mydb.commit()
    print("\n")
    print("*********** Registration Completed \U0001f60A Kindly Login ************")
    print("_______________________________________________________________________")
    print("\n")

def go_login():
    ''' 
    This function when called takes the user to login page.
    '''
    while True:
        try:
            try:
                u=int(input("Press 1 To Go Login Page ! : "))
            except:
                raise Exception
            if (u>=2) or (u<1) :
                print('\n')
                print("Key other than 1 is not valid ! \U0001F642 ")
                print('\n')
            elif(u==1):
                break
        except Exception:
            print("\n")
            print("_________________________________________________")
            print("Please Enter Right Key! \U0001F642 ")
            print("_________________________________________________")
            print("\n")

