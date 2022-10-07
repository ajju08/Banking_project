def display_account_info():
    return "one"
def list_of_beneficiaries():
    return "two"
def list_of_card():
    return "three"
def add_beneficiary():
    return "four"
def update_account_info():
    return "five"
def transfer_fund():
    return "six"
def change_mpin_of_allotted_card():
    return "seven"
def register_new_card():
    return "eight"
def default():
    return "Sorry! Please Enter Valid keyword \U0001f612"

numberSpell = {
    1: display_account_info,
    2: list_of_beneficiaries,
    3: list_of_card,
    4: add_beneficiary,
    5: update_account_info,
    6: transfer_fund,
    7: change_mpin_of_allotted_card,
    8: register_new_card
    }

def spellFunction(number):
    return numberSpell.get(number, default)()

print(spellFunction(int(input("Enter a number : "))))
