
from Project_ATM_Database import customer_pin, customer_balance


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

def show_balance(cust_id):
    balance = customer_balance[cust_id]
    print(f"Your current balance is: {balance}")