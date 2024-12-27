balance = 10000
while True :
    option = int(input("enter 1 to credit the amount ,2 for debit,3 for balance_checking, 4 for atm pin generation,5 for exit :"))
    def credit() :
        if option ==1 :
            amount = int(input("enter the amount to credit :"))
            global balance
            balance+=amount
            print("amount credited successfully")
    credit()
    def debit() :
        if option == 2 :
            amount = int(input("enter the amount to debit : "))
            global balance
            balance-= amount
            print("amount debited successfully")
    debit()
    def balance_checking() :
        if option == 3 :
            global balance
            print(balance)
    balance_checking()
    def pin_generation() :
        if option == 4 :
            new_pin = int(input("enter the new pin to generate : "))
            print(f"your new pin is {new_pin} generated successfully")
    pin_generation()
    def exit() :
        if option == 5 :
            print("exit")
    break
    exit()