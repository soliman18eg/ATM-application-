from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
balance = 100
# name = str(input("enter name to register: [1-10 characters] "))
# pin = input("ENTER PIN:")

while True:
    try:
        name = str(input("enter name to register: [1-10 characters] "))
        if 1 <= len(name) <= 10:
            print(f"Thank you. The username {name} is valid")
            break

        else:
            print("invalid username  length between 1 and 10 characters. PL Try again")

    except:
        print("invalid username  length between 1 and 10 characters. PL Try again")
while True:
    try:
        pin = input("ENTER PIN:")
        if int(len(pin)) >=4:
            break

        else:
            print("invalid pin, Pin must be 4 digits or more !PL Try again")
    except:
        print("invalid pin, Pin must be 4 digits!PL Try again")

        print(name, "has been registred with starting balance of: $0")









        print("          === Automated Teller Machine ===          ")

        username = input("enter username: ")
        pin_number = int(input("ENTER PIN:"))
        if username == name and pin_number == pin:
            print(" login Successful !")
            break
        else:
            print("Invalid credentials")


while True:
    atm_menu(name)
    options = str(input("choose an option: "))
    if options == "1":
        print( account.show_balance(balance) )
        print('Your Balance is $', balance, '\n')
        restart = input('Would You you like to go back? ')
        if restart in ('n', 'NO', 'no', 'N'):
            print('Thank You')
            break
    if options == "2":
        balance = account.deposit(balance)
        print('Your amount $', balance, '\n')
        restart = input('Would You you like to go back? ')

        if restart in ('n', 'NO', 'no', 'N'):
            print('Thank You')
            break
    if options == "3":

        balance = account.withdraw(balance)

        print('Your amount $', balance, '\n')
        restart = input('Would You you like to go back? ')

        if restart in ('n', 'NO', 'no', 'N'):
            print('Thank You')
            break

    if options == "4":
        account.logout(name)
        print('Your amount $', balance, '\n')
        restart = input('Would You you like to go back? ')

        if restart in ('n', 'NO', 'no', 'N'):
            print('Thank You')
            break









