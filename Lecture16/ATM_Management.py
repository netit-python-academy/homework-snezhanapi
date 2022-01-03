from Project_ATM_Database import customer_pin, customer_balance

global action


def validate_pin(cust_id):
    for i in range(0, 3):
        input_pin = input("Please enter your pin\n")
        if int(input_pin) == customer_pin[cust_id]:
            x = True
            break
        else:
            print("Invalid pin\n")
            x = False
    return x


def enter_option():
    print("Options: Balance, Withdraw, Deposit")
    input_option = input("Please choose an option\n")
    if input_option.lower() in options.keys():
        action = options[input_option.lower()]
        print(action)
        return action
    else:
        print("Invalid option")
        exit


def show_balance(cust_id):
    balance = customer_balance[cust_id]
    print(f"Your current balance is: {balance}")


def validate_input_amount(input_amount):
    if input_amount.isdigit():
        return True
    else:
        print("Invalid input")
        return True


def withdraw(cust_id):
    balance = customer_balance[cust_id]
    withdraw_amount = input("Please enter amount to withdraw:\n")
    if validate_input_amount(withdraw_amount):
        if float(withdraw_amount) <= balance:
            final_balance = balance - float(withdraw_amount)
            print(f"Your current balance is: {final_balance}")
        else:
            print("Non-sufficient funds")


def deposit(cust_id):
    balance = customer_balance[cust_id]
    deposit_amount = input("Please enter amount to deposit:\n")
    if validate_input_amount(deposit_amount):
        final_balance = balance + float(deposit_amount)
        print(f"Your current balance is: {final_balance}")


options = {
    "balance": show_balance,
    "withdraw": withdraw,
    "deposit": deposit
}


def myMain(action):
    options[action]()
