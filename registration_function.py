SpecialSym =['$', '@', '#', '%']
import mysql.connector
# This is mysql connector to connect mysql server
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Ajeet@1234#",
    db="Banking_Project"
    )
# Cursor objects interact with the MySQL server using a MySQLConnection object
mycursor = mydb.cursor()

def remove(str):
    # This Method is for removing all space from string
    return str.replace(" ", "")

def welcome():
    print("\n")
    print("___________________________________________________________________________")
    print("************ \U0001f60A Welcome To CheckPaisa Bank \U0001f60A ************")
    print("___________________________________________________________________________")
    print("\n")
    print("Press 1 For Registration ")
    print("Press 2 For Log In  ")
    print("Press 3 For Exit  ")

def name():
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
    while True:
                try:
                    a='.'
                    a1='#'
                    a2='$'
                    a3='*'
                    a4='&'
                    a5='='
                    a6=','
                    a8='?'
                    a9='@'
                    p=input("Enter Your User Name : ")
                    if(a in p) or (a1 in p) or (a2 in p) or (a3 in p) or (a4 in p) or (a5 in p) or (a6 in p) or (a7 in p) or (a8 in p) or (a9 in p):
                        raise TypeError 
                    break
                except TypeError as m:
                    print("Special Character are not allowed like . ,@ # $ % * & = < > ? !")
    return p

def password():
    while True:        
                try:

                    z=input("Enter Your Password : ")
                    if (len(z)<6):
                        raise ValueError (" Password should contain at least 6 character ")
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
    s=input("Enter Your Address : ")
    return s

def mobile():
    while True:
            try:
                d=input("Enter Your Phone Number : ")
                if (len(d)!=10) or (d.isalpha()):
                    raise ValueError("Pls enter a valid 10 digit Number")
                break
            except ValueError as m:
                print(m)
    return d

def aadhar():
    while True:
        try:
            f=input("Enter Your 12 Digit Aadhar Number Without putting space  : ")
            if(len(f)!=12) or (f.isalpha()):
                raise ValueError ("Please Enter a valid 12 digit aadhar Number")
            break
        except ValueError as m:
            print(m)
    return f

def registration_confirmation(ut2,z,k,s,f,d):
    q="insert into account_details (name,password,balance,address,mobile,aadhar) values('{}','{}','{}','{}','{}','{}')".format(ut2,z,k,s,f,d)
    mycursor.execute(q)
    mydb.commit()
    ad="select account_number from account_details where name='{}' and password ='{}' ".format(ut2,z)
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

