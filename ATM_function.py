Bal = 0
def ch_balance():
    global Bal
    print("The balance amount is:",Bal)
def depo(a):
    global Bal
    Bal += a
    print("The amount deposited is :",a)
    ch_balance()
def withdraw(a):
    global Bal
    if a > Bal:
        print("Not sufficient amount to withdraw")
    else:
        Bal -= a
        print("The amount withdrawn :",a)
        ch_balance()
def show():
    global Bal
    while True:
        print("ATM FUNCTIONS")
        print("1. BALANCE")
        print("2. DEPOSIT")
        print("3.WITHDRAW")
        print("4.EXIT")
        ch = input("select from 1 to 4: ")
        if ch == '1':
            ch_balance()
        elif ch == '2':
            a = int(input("Enter amont to deposit:"))
            depo(a)
        elif ch == '3':
            a = int(input("Enter withdraw amount:"))
            withdraw(a)
        elif ch == '4':
            print("Thanks and see you again")
            break
        else:
            print("Invalid inputs!")
show()
        