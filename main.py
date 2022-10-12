

class Account :
    # accNo = 0
    # name = ''
    # deposit=0
    # type = ''
    
    def registration(self):
        self.name = input("Enter the user name : ")
        self.address = input("Ente the address : ")
        self.aadhar = int(input("Enter the 12 digit aadhar number : "))
        self.mobile = int(input("Entre your mobile number : "))
        print("\n\nCongrats! New Account Created")
        # print(f"\n\n Your Account Number is : { account_number} ")
    
    def display_account_info(self):
        print("Account Number : ",self.accNo)
        print("Account user Name : ", self.name)
        print("Balance : ",self.deposit)
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def list_of_beneficiaries():
        pass
    def list_of_card():
        pass
    def add_beneficiary():
        pass
    def update_account_info(self):
        print("Account Number : ",self.accNo)
        self.name = input("Enter correct user Name :")
        self.address = input("Enter correct Address :")
        self.aadhar = int(input("Enter correct aadhar number : "))
        self.mobile = int(input("Enter correct Mobile Number : "))
    def transfer_fund():
        pass
    def change_mpin_of_allotted_card():
        pass
    def register_new_card():
        pass

