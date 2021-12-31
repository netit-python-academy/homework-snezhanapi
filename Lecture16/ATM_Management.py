
from Project_ATM_Database import customer_pin


def validate_pin(cust_id):
    for i in range(0, 2):
        input_pin = input("Please enter your pin\n")
        if input_pin == customer_pin[cust_id]:
            x = True
            break
        else:
            x = False
    return x
