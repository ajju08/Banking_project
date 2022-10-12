from mysql_connector import mydb, mycursor
from registration_function import *
from login_function import *
from curses.ascii import isalpha, isdigit
SpecialSym =['$', '@', '#', '%']

def registration():
    while True:
        welcome()
        try:
            try:
                ch=int(input("Enter the Key : "))
            except:
                print("Please Enter Right Key! \U0001F642 ")
            if (ch>=4) or (ch<1) :
                print('\n')
                print("Key other than 1,2 of 3 are not valid ! \U0001F642 ")
                print('\n')

            elif(ch==1):
                a1=name()
                a2=password()
                a3=balance()
                a4=address()
                a5=mobile()
                a6=aadhar()
                registration_confirmation(a1,a2,a3,a4,a5,a6)
                go_login()
                
            elif(ch==2):
                while True:
                    u=input("Enter Your Username : ")
                    try:
                        try:     
                            a="select * from account_details where name='{}'".format(u)
                            mycursor.execute(a)
                            data=mycursor.fetchall()
                        except :
                            raise Exception
                        if data:
                            break
                        else:
                            print("Invalid Username ! ")
                    except Exception:
                        print("Oops! Something went wrong  ! ")
                    
                while True:
                    p=input("Enter Your password : ")
                    try:
                        try:
                            a="select * from account_details where password='{}'".format(p)
                            mycursor.execute(a)
                            data=mycursor.fetchall()
                        except:
                            raise Exception
                        if data:
                            break
                        else:
                            print("Invalid password ! ")
                    except Exception:
                        print("Oops! Something went wrong  ! ")

                if data:
                    while True:
                        task_bar()
                        try:
                            try:
                                ch1=int(input("Enter the Key : "))

                            except:
                                raise Exception

                            if (ch1>=10) or (ch1<1) :
                                print('\n')
                                print("Key other than 1 to 10 are not valid ! \U0001F642 ")
                                print('\n') 

                            elif(ch1==1):
                                account_info(u,p) 
                                go_back()

                            elif(ch1==2):
                                list_of_beneficiaries(u,p)
                                go_back()

                            elif(ch1==3):
                                list_of_card(u,p)
                                go_back()

                            elif(ch1==4):
                                add_beneficiaries(u,p)
                                go_back()

                            elif(ch1==5):
                                update_account_info(u,p)
                                go_back() 

                            elif(ch1==6):
                                transfer_fund(u,p)
                                go_back() 

                            elif(ch1==7):
                                change_mpin_of_alloted_card(u,p)
                                go_back() 

                            elif(ch1==8):
                                register_new_card(u,p)
                                go_back() 

                            elif(ch1==9):
                                break

                        except Exception:
                            print("\n")
                            print("_________________________________________________")
                            print("Please Enter Right Key! \U0001F642 ")
                            print("_________________________________________________")
                            print("\n")

            elif(ch==3):
                print("_________________________________________________")
                print("Thank You For Visiting! \U0001f60A ")
                print("_________________________________________________")
                break  
                
        except Exception:
            print("\n")
            print("_________________________________________________")
            print("Oops! Something went wrong \U0001F610 ")
            print("_________________________________________________")
            print("\n")
registration()
# address()
# password()
# aadhar()
