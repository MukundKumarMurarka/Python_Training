# code for user defined exception
class AccountBalance(Exception):
    pass
def maintainBalance():
    available_balance = 10000
    withdraw_balance= int(input(" enter the balance you want to withdraw "))
    try:
        restamount =  available_balance - withdraw_balance
        if restamount <= 2000:
            raise AccountBalance(" print isufficient balance ")
        print(restamount)
    except AccountBalance as acpt:
        print(acpt)
maintainBalance()