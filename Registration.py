from curses.ascii import isalpha, isdigit
SpecialSym =['$', '@', '#', '%']


def remove(string):
    return string.replace(" ", "")


while True:
    print("\n")
    print("**************************  Welcome To Bank  ******************************")
    print("\n")
    print("Press 1 to for Registration ")
    print("Press 2 to for Log In  ")

    try:
        ch=int(input("Enter Your Choice : "))
        if(isalpha(ch)) or (ch>=3) :
            raise Exception ("Oops!  That was not a valid number.  Try again...  :( ")




        elif(ch==1):
            while True:
                try: 
                    a='.'
                    a1='#'
                    a2='$'
                    a3='*'
                    a4='&'
                    a5='='
                    a6=','
                    a7='@'
                    a8='?'
                    a9='/'
                    a10=' '
                    ut1 = input("Enter Your Name Here : ")
                    ut2 = ut1.strip()
                    ut = remove(ut1)
                    if ut.isalpha() :
                        if ((a in ut) or (a1 in ut) or (a3 in ut) or (a4 in ut) or (a5 in ut) or (a6 in ut) or (a7 in ut) or (a8 in ut) or (a9 in ut) or (a10 in ut) or ())  :
                            raise TypeError 
                        break
                    else :
                        print("Name contains number are not allowed ")
                except TypeError:
                    print("Numeric or Special Character are not allowed like . , @ # < > ? / ; ")
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
                    print("Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
                except KeyError:
                    print("Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")


            k=int(input("Enter the Amount of money you want to deposit : "))

            s=input("Enter Your Address : ")

            while True:
                try:
                    d=input("Enter Your Phone Number : ")
                    if (len(d)!=10) or (d.isalpha()):
                        raise ValueError("Pls enter a valid 10 digit Number")
                    break
                except ValueError as m:
                    print(m)

            while True:
                try:
                    f=input("Enter Your 12 Digit Aadhar Number Without putting space  : ")
                    if(len(f)!=12) or (f.isalpha()):
                        raise ValueError ("Please Enter a valid 12 digit aadhar Number")
                    break
                except ValueError as m:
                    print(m)

            # q="insert into registration values('{}','{}','{}','{}','{}','{}','{}','{}')".format(ut2,p,z,a,s,d,f,k)
            # mycur.execute(q)
            # mycon.commit()
            print("\n")
            print("*********** Registration Completed \U0001f60A Kindly Login ************")
            print("_______________________________________________________________________")
            print("\n")
        break
    except Exception:
        print("\n")
        print("Oops! Something went wrong ")
        print("_________________________________________________")
        print("\n")
        break

