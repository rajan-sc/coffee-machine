MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}gm")
    print(f"Money: ${money}")


def coffee_selector(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]


def ingredients_avl_check(coffee_type):
    """Check the availability of ingredients """
    if resources["water"] >= MENU[coffee_type]["ingredients"]["water"]:
        if resources["milk"] >= MENU[coffee_type]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[coffee_type]["ingredients"]["coffee"]:
                return True
            else:
                print("Sorry not enough coffee.")
                return False
        else:
            print("Sorry not enough milk.")
            return False
    else:
        print("Sorry not enough water")
        return False


def coin_sorter(coffe_type):
    a = int(input("No. of quarters :")) * 0.25
    b = int(input("No. of nickles :")) * 0.25
    c = int(input("No. of dimes :")) * 0.25
    d = int(input("No. of pennies :")) * 0.25
    e = a + b + c + d
    change = e - MENU[coffe_type]["cost"]
    print(f"Here your {change}$ in change.")
    return e


at_end = True
while at_end:
    order = input("What type of coffee would you like (Latte, Espresso, Cappuccino) : ").lower()
    if order == "latte" or order == "cappuccino" or order == "espresso":
        if ingredients_avl_check(coffee_type=order):
            if coin_sorter(coffe_type=order) >= MENU[order]["cost"]:
                money += MENU[order]["cost"]
                coffee_selector(coffee_type=order)
                print(f"Here you go your {order}!")
            else:
                at_end = False
                print("Not enough money ")
        else:
            at_end = False
    elif order == "report":
        report()
    elif order == "off":
        at_end = False
