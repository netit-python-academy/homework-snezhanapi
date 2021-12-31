from ATM_Management import validate_pin


from Project_ATM_Database import customer_id
customer_name = input("Please enter your name\n")
if customer_name in customer_id.keys():
    print(customer_id[customer_name])
    is_pin_valid = validate_pin()
    if
else:
    print("Invalid customer name")