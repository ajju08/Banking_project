from pprint import pprint
from registration_function import *
from mysql_connector import mydb, mycursor
SpecialSym =['$', '@', '#', '%']
    
def nameCheck(u):
    ''' 
    This function validates the name entered by user while logging in. 
    :param u: 'u' is the entered name.
    '''
    while True:
        try:
            a="select * from account_details where name='{}'".format(u)
            mycursor.execute(a)
            data=mycursor.fetchall()
            if data:
                break
            else:
                print("Invalid name ! ")
                break
        except:
            print("Invalid name ! ")
            break

def passwordCheck(p):
    ''' 
    This function validates the password entered by the user while logging in. In which, it allows only the correct password stored in the database. 
    :param p: 'p' is the entered password.
    '''
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

def go_back():
    ''' 
    This function takes the user exactly one step back and validates if the back key '1' is entered or not. 
    '''
    while True:
        try:
            try:
                u=int(input("Press 1 To Go Back! : "))
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

def task_bar():
    ''' 
    This function prints all the options provided to the user whenever called.
    '''
    print("\n")
    print("___________________________________________________________________________")
    print("************ \U0001f60A Welcome To CheckPaisa Bank \U0001f60A *************")
    print("___________________________________________________________________________")
    print("\n")
    print("Press 1 To display_account_info")
    print("Press 2 To list_of_beneficiaries ")
    print("Press 3 To list_of_card")
    print("Press 4 to add_beneficiary")
    print("Press 5 to update_account_info")
    print("Press 6 to transfer_fund")
    print("Press 7 to change_mpin_of_allotted_card")
    print("Press 8 to register_new_card")
    print("Press 9 for log out ")
    print("\n")

def account_info(u,p):
    ''' 
    This function is displaying all the account details of the user from the table "account_details" whenever called. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select * from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a1=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    print("____________________________________________")
    for x in a1:
        print("Your Account Number is      : " ,x[0])
        print("____________________________________________")
        print("Your Account Holder Name is : " ,x[1])
        print("____________________________________________")
        print("Your balance is             : " ,x[3])
        print("____________________________________________")
        print("Your Aadhar Number is       : " ,x[5])
        print("____________________________________________")
        print("Your Mobile Number is       : " ,x[6])
    print("____________________________________________")
    print("\n")

def list_of_beneficiaries(u,p):
    ''' 
    This function is displaying all the beneficiaries details of the user from the table "list_of_beneficiaries" whenever called. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a2=mycursor.fetchone()[0]
        print("Your Account Number is : ",a2)
        np1="select * from list_of_beneficiaries where account_number={} ".format(a2)
        mycursor.execute(np1)
        l2=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    if len(l2[0]) ==1:
        print("____________________________________________")
        print("You have't Beneficiaries! ")
        print("____________________________________________")
    else:
        for x in l2:
            i=1
            k=1
            try:
                while (i < len(x)):
                    
                    if x[i] is not None:
                        print("____________________________________________")
                        print("Beneficiaries%s : %s"%((k),x[i]))
                        print("Account Number%s : %s"%((k),x[i+1]))
                        print("____________________________________________")
                    i +=2
                    k +=1
            except :
                print("____________________________________________")
                print("You have't Beneficiaries! ")
                print("____________________________________________")
        print("\n")

def list_of_card(u,p):
    ''' 
    This function is displaying all the card details of the user from the table "card_details" whenever called. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a3=mycursor.fetchone()[0]
        print("Your Account Number is : ",a3)
        np3="select * from card_details where account_number={} ".format(a3)
        mycursor.execute(np3)
        l3=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    print("____________________________________________")
    for x in l3:
        if(x[7] =='active'):
            print("Your Credit Card Number : ",x[1])
        else:
            print("Currently No Any Credit Card Alloted! \U0001F642 ")
        print("____________________________________________")
        if(x[8]=='active'):
            print("Your debit Card  Number : ",x[4])
        else:
            print("Currently No Any Debit Card Alloted! \U0001F642 ")
    print("____________________________________________")
    print("\n")

def add_beneficiaries(u,p):
    ''' 
    This function is adding beneficiaries name related to that account in the table "list_of_beneficiaries" whenever called. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a4=mycursor.fetchone()[0]
        print("Your Account Number is: ",a4)
        np4="select * from list_of_beneficiaries where account_number={} ".format(a4)
        mycursor.execute(np4)
        l4=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    print("____________________________________________")
    for x in l4:
        if(x[1] == None):
            name = str(input("Enter the beneficiaries Name : "))
            if(remove(name).isalpha()):
                account = int(input("Enter the account number of beneficiaries : "))
                # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
                lb="UPDATE list_of_beneficiaries SET beneficiaries1='{}' , beneficiaries1_account={} where account_number = {}".format(name,account,a4)
                mycursor.execute(lb)
                mydb.commit()
                print("Your Beneficiaries Added Sucessfully! \U0001f60A ")
                break
            else:
                print("Please write Right Name! ")
        elif(x[3] == None):
            while True:
                name = str(input("Enter the beneficiaries Name : "))
                if(remove(name).isalpha()):
                    account = int(input("Enter the account number of beneficiaries : "))
                    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
                    lb="UPDATE list_of_beneficiaries SET beneficiaries2='{}' , beneficiaries2_account={} where account_number = {}".format(name,account,a4)
                    mycursor.execute(lb)
                    mydb.commit()
                    print("Your Beneficiaries Added Sucessfully! \U0001f60A ")
                    break
                else:
                    print("Please write Right Name! ")
        elif(x[5] == None):
            while True:
                name = str(input("Enter the beneficiaries Name : "))
                if(remove(name).isalpha()):
                    account = int(input("Enter the account number of beneficiaries : "))
                    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
                    lb="UPDATE list_of_beneficiaries SET beneficiaries3='{}' , beneficiaries3_account={} where account_number = {}".format(name,account,a4)
                    mycursor.execute(lb)
                    mydb.commit()
                    print("Your Beneficiaries Added Sucessfully! \U0001f60A ")
                    break
                else:
                    print("Please write Right Name! ")
        elif(x[7] == None):
            while True:
                name = str(input("Enter the beneficiaries Name : "))
                if(remove(name).isalpha()):
                    account = int(input("Enter the account number of beneficiaries : "))
                    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
                    lb="UPDATE list_of_beneficiaries SET beneficiaries4='{}' , beneficiaries4_account={} where account_number = {}".format(name,account,a4)
                    mycursor.execute(lb)
                    mydb.commit()
                    print("Your Beneficiaries Added Sucessfully! \U0001f60A ")
                    break
                else:
                    print("Please write Right Name! ")
        elif(x[9] == None):
            while True:
                name = str(input("Enter the beneficiaries Name : "))
                if(remove(name).isalpha()):
                    account = int(input("Enter the account number of beneficiaries : "))
                    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
                    lb="UPDATE list_of_beneficiaries SET beneficiaries5='{}' , beneficiaries5_account={} where account_number = {}".format(name,account,a4)
                    mycursor.execute(lb)
                    mydb.commit()
                    print("Your Beneficiaries Added Sucessfully! \U0001f60A ")
                    break
                else:
                    print("Please write Right Name! ")
        else:
            print("You already added 5 beneficiaries \U0001f60A ")
            break
    print("____________________________________________")
    print("\n")

def update_bar():
    '''
    This function prints all the options provided to the user whenever called.
    '''
    print("\n")
    print("___________________________________________________________________________")
    print("************** Update Your Account Information : **************************")
    print("___________________________________________________________________________")
    print("\n")
    print("Press 1 To Update Your Name ")
    print("Press 2 To Update Your Password  ")
    print("Press 3 To Update Your Aadhar Number ")
    print("Press 4 To Update Your MObile Number ")
    print("Press 5 To Update Your Address ")
    print("Press 6 To Go BACK ")

def update_account_info(u,p):
    ''' 
    This function is updating the account information of logged in user by taking inputs from the user and updating the database table 'account_details' simultaneously.
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    while True:
        update_bar()
        try:
            try:
                up1=int(input("Enter The Keyword : "))
            except:
                print("Please Enter Right Key! \U0001F642 ")
            if (up1>=7) or (up1<1) :
                print('\n')
                print("Key other than 1 to 6 are not valid ! \U0001F642 ")
                print('\n')                       
            elif(up1==1):
                nm1=name()
                np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np)
                a51=mycursor.fetchone()[0]
                print("Your Account Number is : ",a51)
                lb51="UPDATE account_details SET name='{}' where account_number = {}".format(nm1,a51)
                mycursor.execute(lb51)
                mydb.commit()
                print("Your Name is sucessfully updated! ")
            elif(up1==2):
                nm2=password()
                np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np)
                a52=mycursor.fetchone()[0]
                print("Your Account Number is : ",a52)
                lb52="UPDATE account_details SET password='{}' where account_number = {}".format(nm2,a52)
                mycursor.execute(lb52)
                mydb.commit()
                print("Your Password is sucessfully updated! ")
            elif(up1==3):
                nm3=aadhar()
                np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np)
                a53=mycursor.fetchone()[0]
                print("Your Account Number is : ",a53)
                lb53="UPDATE account_details SET aadhar={} where account_number = {}".format(nm3,a53)
                mycursor.execute(lb53)
                mydb.commit()
                print("Your Aadhar Number is sucessfully updated! ")
            elif(up1==4):
                nm4=mobile()
                np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np)
                a54=mycursor.fetchone()[0]
                print("Your Account Number is : ",a54)
                lb54="UPDATE account_details SET mobile={} where account_number = {}".format(nm4,a54)
                mycursor.execute(lb54)
                mydb.commit()
                print("Your Mobile Number is sucessfully updated! ")
            elif(up1==5):
                nm5=address()
                np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np)
                a55=mycursor.fetchone()[0]
                print("Your Account Number is : ",a55)
                lb55="UPDATE account_details SET address='{}' where account_number = {}".format(nm5,a55)
                mycursor.execute(lb55)
                mydb.commit()
                print("Your Address is sucessfully updated! ")
            elif(up1==6):
                break
        except TypeError:
            print("________________________________________________")
            print("     OOPs !!! That Was an Invalid Keyword :  ")
            print("________________________________________________")

def transfer_fund(u,p):
    ''' 
    This function already contains list of beneficiaries linked with the logged in user.
    Also, It allows user to enter the number associated to every beneficiary linked to user's account and make a fund transfer to user's beneficiary. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select account_number ,balance from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a6=mycursor.fetchall()
        print("Your Account Number is : ",a6)
        for x in a6:
            acc=x[0]
            bal=x[1]
            np6="select * from list_of_beneficiaries where account_number={} ".format(x[0])
            mycursor.execute(np6)
            l6=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    print("Your account balance is : ",bal)
    print("These are your beneficiaries : ")
    print("____________________________________________")
    for x in l6:
        print("Press 1, To tansfer amount to beneficiaries1 : ")
        print("Beneficiaries1 : ",x[1])
        print("Account Number : ",x[2])
        print("____________________________________________")
        print("Press 2, To tansfer amount to beneficiaries2 : ")
        print("Beneficiaries2 : ",x[3])
        print("Account Number : ",x[4])
        print("____________________________________________")
        print("Press 3, To tansfer amount to beneficiaries3 : ")
        print("Beneficiaries3 : ",x[5])
        print("Account Number : ",x[6])
        print("____________________________________________")
        print("Press 4, To tansfer amount to beneficiaries4 : ")
        print("Beneficiaries4 : ",x[7])
        print("Account Number : ",x[8])
        print("____________________________________________")
        print("Press 5, To tansfer amount to beneficiaries5 : ")
        print("Beneficiaries5 : ",x[9])
        print("Account Number : ",x[10])
        print("____________________________________________")
        print("\n")
    while True:
        while True:
            try:
                try:
                    amount = int(input("Enter transfereable amount : "))
                except:
                    print("Please Enter the value ! \U0001F642 ")
                if (amount<=0) :
                    print('\n')
                    print("Amount less than Zero is not exist in the real world only you can think! \U0001F642 ")
                    print('\n') 
                else:
                    break              
            except:
                print("Please write correct value !")
        if(amount<bal):
            key1= int(input("Enter beneficiaries key : "))
            # "update bank set Balance=GREATEST(0,Balance - '{}') where UserName='{}'".format(a1,u)
            en = "UPDATE account_details SET balance=(balance - {}) where account_number = {}".format(amount,acc)
            mycursor.execute(en)
            mydb.commit()
            for x in l6:
                if(key1==1):
                    b_acc = x[2]
                    bn = "UPDATE account_details SET balance = (balance + {}) where account_number={} ".format(amount,b_acc)
                    mycursor.execute(bn)
                    mydb.commit()

                elif(key1==2):
                    b_acc = x[4]
                    bn = "UPDATE account_details SET balance = (balance + {}) where account_number={} ".format(amount,b_acc)
                    mycursor.execute(bn)
                    mydb.commit()

                elif(key1==3):
                    b_acc = x[6]
                    bn = "UPDATE account_details SET balance = (balance + {}) where account_number={} ".format(amount,b_acc)
                    mycursor.execute(bn)
                    mydb.commit()

                elif(key1==4):
                    b_acc = x[8]
                    bn = "UPDATE account_details SET balance = (balance + {}) where account_number={} ".format(amount,b_acc)
                    mycursor.execute(bn)
                    mydb.commit()

                elif(key1==5):
                    b_acc = x[10]
                    bn = "UPDATE account_details SET balance = (balance + {}) where account_number={} ".format(amount,b_acc)
                    mycursor.execute(bn)
                    mydb.commit()
                np1="select balance from account_details where name='{}' and password ='{}' ".format(u,p)
                mycursor.execute(np1)
                updated_balance=mycursor.fetchone()[0]
                print("Your Updated Balance is : ",updated_balance)
            break 
        else:
            print("Sorry! You have insufficient balance \U0001F610 ")
            np1="select balance from account_details where name='{}' and password ='{}' ".format(u,p)
            mycursor.execute(np1)
            updated_balance=mycursor.fetchone()[0]
            print("Your Updated Balance is : ",updated_balance) 

def change_mpin_of_alloted_card(u,p):
    ''' 
    This function allows user to change the PIN of his/her card allotted to them. 
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    try:
        np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
        mycursor.execute(np)
        a7=mycursor.fetchone()[0]
        print(a7)
        np7="select * from card_details where account_number={} ".format(a7)
        mycursor.execute(np7)
        l7=mycursor.fetchall()
    except Exception:
        print("oops")
    print("\n")
    print("____________________________________________")
    for x in l7:
        print("Press 1 to change Credit Card Pin : ")
        print("Your Credit Card Number : ",x[1])
        print("Press 2 to change Debit Card Pin : ")
        print("Your Debit Card Number : ",x[4])
    key3 = int(input("Enter the Key : "))
    if(key3==1):
        new_pin_c = int(input("Enter New Pin of Credit Card : "))
        # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
        lb="UPDATE card_details SET credit_card_pin='{}' where account_number = {}".format(new_pin_c,a7)
        mycursor.execute(lb)
        mydb.commit()
        print("Your Credit Card Pin is successfully Updated! ")
    elif(key3==2):
        new_pin_d = int(input("Enter New Pin of Credit Card : "))
        # UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
        lb="UPDATE card_details SET debit_card_pin='{}' where account_number = {}".format(new_pin_d,a7)
        mycursor.execute(lb)
        mydb.commit()
        print("Your Debit Card Pin is successfully Updated! ")

    print("____________________________________________")
    print("\n")

def register_new_card(u,p):
    ''' 
    This function allows the user to activate the card allotted to his/her account in the bank.
    :param u: 'u' is the entered name.
    :param p: 'p' is the entered passsword.
    '''
    np="select account_number from account_details where name='{}' and password ='{}' ".format(u,p)
    mycursor.execute(np)
    a8=mycursor.fetchone()[0]
    print("Your Account Number is : ",a8)
    print("Press 1 for activate your credit card! ")
    print("Press 2 for activate your debit card! ")      
    while True:
        try:
            try:
                card_status_key = int(input("Enter key : "))
            except:
                print("Please Enter Right Key! \U0001F642 ")
            if (card_status_key > 2) or (card_status_key < 1) :
                print('\n')
                print("Key other than 1 and 2 are not valid ! \U0001F642 ")
                print('\n')
            elif(card_status_key == 1):
                cd = "UPDATE card_details SET credit_card_status= '{}' where account_number = {}".format('active',a8)
                mycursor.execute(cd)
                mydb.commit()
                cdn = "SELECT credit_card_no from card_details where account_number = {}".format(a8)
                mycursor.execute(cdn)
                print("Your Credit Card Number is : ",mycursor.fetchone()[0])
                print("Your Credit Card Activated successfully! ")
                break
            elif(card_status_key == 2):
                cd = "UPDATE card_details SET debit_card_status= '{}' where account_number = {}".format('active',a8)
                mycursor.execute(cd)
                mydb.commit()
                cdn = "SELECT debit_card_no from card_details where account_number = {}".format(a8)
                mycursor.execute(cdn)
                print("Your Debit Card Number is : ",mycursor.fetchone()[0])
                print("Your Debit Card Activated successfully! ")
                break
        except:
            print("Enter the Correct Key! ")


