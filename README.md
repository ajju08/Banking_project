# Banking_Application_Project using MySql and Python
## About

In this project we have created a Virtual Bank Application **(CheckPaisa Bank)** using Python and MySQL. Data entered by the user are stored in MYSQL database in tabular form. The Best Part of this code is that it is 100 % user friendly because of excess use of exceptional handling.

This project is designed for The Account Holder to see their record, Transfer fund, add beneficiaries,activate credit & debit card,change card pin . Only authorized Users can have the accessibility to the program. User after Logging in have the support to display all records, and modify it accordingly. If someone is not having Login Id, password he/she could make a new id. Further it can also check overall record of a local customer or full detail of a single a/c as per transactions, create a new record for new customer, Update an old customer record. Python is used as Front End and MySQL is used as Back End.

## Requirement

1.Python Latest Version(3.8.10)

2.Visual Studio Code

3.MySql(8.0.30)

4.Python MySql connector : Most Important

## Module Used In Python Code

 mysql.connector
 
## About MySql Code
 
 1.Database used here is Banking_Project
   - create database Banking_Project;
 2.Tables : account_details,list_of_beneficiaries,card_details
 
   - **Table: account_details**
   - **column name:** (account_number,name,password,balance,address,aadhar,mobile)
   - Here account_number is auto incremented.
 
   - **Table : card_details**
   - **column name:**(account_name,credit_card_no,credit_card_pin,credit_card_cvv,debit_card_no,debit_card_pin,debit_card_cvv,credit_card_status,debit_card_status)
 
   - **Table : list_of_beneficiaries**
   - **column name:** (account_number,beneficiaries1,beneficiaries1_account,beneficiaries2,beneficiaries2_account,beneficiaries3,beneficiaries3_account,beneficiaries4,beneficiaries4_account,beneficiaries5,beneficiaries5_account)

## More About Files:

- **SourceCode.py**
  - In this all code are written in one file only you run this file to  see all result

- **home.py**
  - This is home menu to run this banking application project here we call all registration_function and login_function

- **registration_function**
  - This is registration file in which all registion function are defined seperatly and if wanna to change something in one function it will not affect to  other function.

- **login_function**
  - This is the login file in which all login function are defined seperatly and if wanna to change something in one function it will not affect to other function.

- **mysql_connector**
  - In this file we put the mysql login credential like as host,user,password and database name create a cursor to execute the mysql related code


## Run home.py file to run all program.



