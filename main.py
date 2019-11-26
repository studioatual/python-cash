import getpass
import os

# Initialize Machine
def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    getHeader()
    getLogin()

# Header to Cash Machine
def getHeader():
    print("****************************************************************")
    print("*********************** WR - Cash Machine **********************")
    print("****************************************************************")
    print("\n")

# Inputs to Login Client
def getLogin():
    account = input("Type your Account: (press Enter)\n")
    if account == 'x':
        return exit()

    if not account in accounts:
        print('Account is invalid!')
        print("\n")
        input("Press any key to try again\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        return init()

    password = getpass.getpass("Type your Password: (press Enter)\n")

    if not password == accounts[account]['password']:
        print('Password is invalid!')
        print("\n")
        input("Press any key to try again\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        return init()

    os.system('cls' if os.name == 'nt' else 'clear')
    init_panel(account)

# Init Panel
def init_panel(account):
    # Show Welcome to Client    
    def show_welcome():
        print("****************************************************************")
        print('Welcome ', accounts[account]['name'])
        show_options()

    # Show Options
    def show_options():    
        print("****************************************************************")
        print('1 Balance | 2 Cash Out | 3 Cash Deposit | 4 Statement | 5 Logout')
        print("****************************************************************")
        print("\n")
        option = input("Choice the option number above: (press Enter)\n")

        if option == '1':
            return show_balance()
        elif option == '2':
            return cash_out()
        elif option == '3':
            return chash_in()
        elif option == '4':
            return mov_in_out()
        elif option == '5':
            return init()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            show_options()

    # Show Balance
    def show_balance():
        print("\n")
        print("****************************************************************")
        print('Your Total Account is: ', accounts[account]['total'])
        print("****************************************************************")
        print("\n")
        input("Press any key to go back\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_options()

    # Cash Out
    def cash_out():
        quantity = input("How much you want? (press Enter)\n")
        quantity = quantity.replace(',', '.')
        if float(quantity) <= accounts[account]['total']:
            accounts[account]['total'] = float(accounts[account]['total']) - float(quantity)
            print("\n")
            print("****************************************************************")
            print('You Receive the amount: ', quantity)
            print('Your Total Account is now: ', accounts[account]['total'])
            print("****************************************************************")
            print("\n")
            input("Press any key to go back\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            show_options()
        else:
            print("The amount is larger than your total account.")
            input("Press any key to try again\n")
            cash_out()

    # Deposit
    def chash_in():
        quantity = input("How much you deposited? (press Enter)\n")
        quantity = quantity.replace(',', '.')
        accounts[account]['total'] = float(accounts[account]['total']) + float(quantity)
        print("\n")
        print("****************************************************************")
        print('You Deposited the amount: ', quantity)
        print('Your Total Account is now: ', accounts[account]['total'])
        print("****************************************************************")
        print("\n")
        input("Press any key to go back\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_options()

    # Moviments
    def mov_in_out():

        input("Press any key to go back\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_options()

    show_welcome()
    show_options()


# Initial Default Variables
accounts = {}
accounts['147-0'] = {'name': 'José Francisco', 'password': '123', 'total': 1280.50}
accounts['258-0'] = {'name': 'Pedro da Silva', 'password': '123', 'total': 4532.00}
accounts['369-0'] = {'name': 'Joana da Conceição', 'password': '123', 'total': 8243.85}
accounts['789-0'] = {'name': 'Maria Vitória', 'password': '123', 'total': 1584.32}

init()