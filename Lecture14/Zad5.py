shopping_cart = []

def add_to_list(item):
    shopping_cart.append(item)

def show_list():
    print('My Shopping List:')
    for item in shopping_cart:
        print(item)

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
    else:
        print("This item doesn't exist in your shopping cart")

def clear_item():
    shopping_cart.clear()

while True:
    user_input = input("Please enter an action \n")
    if user_input.lower() == "add":
        item_input = input("Please add an item \n")
        add_to_list(item_input)
    elif user_input.lower() == "show":
        show_list()
    elif user_input.lower() == "delete":
        item_input = input("Please remove an item \n")
        remove_item(item_input)
    elif user_input.lower() == "clear":
        clear_item()
    elif user_input.lower() == "quit":
        break
