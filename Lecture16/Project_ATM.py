from ATM_Management import validate_pin


from Project_ATM_Database import customer_id
customer_name = input("Please enter your name\n")
if customer_name in customer_id.keys():
    customer_id_number = customer_id[customer_name]
    is_pin_valid = validate_pin(customer_id_number)
    if is_pin_valid:
        print('Valid pin')
    else:
        print("Your card has been blocked")
else:
    print("Invalid customer name")