def show_balance(balance):
    print("current Balance", balance)

def deposit(balance):
    amount = input("Enter amount to deposit:")
    return balance + int(amount)

def withdraw(balance):
    amount = input("Enter amount to Withdraw:")

    # if int(amount) < balance():
    #     print("update balance" )
    # else:
    #     print("Else stament")
    return balance - int(amount)




    # amount = input("Enter amount to Withdraw:")
    # return balance - int(amount)



    # amount = input("Enter amount to Withdraw:")
    # if amount > balance:
    #     print("Please enter a lower amount!")
    #     continue
    # elif amount <= balance:
    #     break
    #     print(balance + amount)



        # else:
        #     print("cant withdrw this amount, Please enter a lower amount!")
        #





def logout(name):
    print("Goodbye", name)