MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0,
}

latte_water_required = MENU["latte"]["ingredients"]["water"]
latte_milk_required = MENU["latte"]["ingredients"]["milk"]
latte_coffee_required = MENU["latte"]["ingredients"]["coffee"]
cappuccino_water_required =MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk_required = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee_required = MENU["cappuccino"]["ingredients"]["coffee"]
espresso_water_required =MENU["espresso"]["ingredients"]["water"]
espresso_milk_required = 0
espresso_coffee_required = MENU["espresso"]["ingredients"]["coffee"]

def checkEnough(water_left,coffee_left, milk_left):
    able = False
    not_enough = []
    if inp == "espresso":
        if water_left >= espresso_water_required and coffee_left >= espresso_coffee_required:
            able = True
        else:
            if water_left < espresso_water_required:
                not_enough.append("water")
            else:
                not_enough.append("coffee")
            able = False
    elif inp == "latte":
        if water_left >= latte_water_required and coffee_left >= latte_coffee_required and milk_left > latte_milk_required:
            able = True
        else:
            if water_left < latte_water_required:
                not_enough.append("water")
            elif milk_left < latte_milk_required:
                not_enough.append("milk")
            else:
                not_enough.append("coffee")
            able = False
    elif inp == "cappuccino":
        if water_left >= cappuccino_water_required and milk_left >= cappuccino_milk_required and coffee_left >= cappuccino_coffee_required:
            able = True
        else:
            if water_left < cappuccino_water_required:
                not_enough.append("water")
            elif milk_left < cappuccino_milk_required:
                not_enough.append("milk")
            else:
                not_enough.append("coffee")
            able = False
    return able, not_enough

def processCoins():
    money_inserted = 0
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))
    money_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return money_inserted

def assignCost():
    cost = 0
    if inp == "espresso":
        cost = MENU["espresso"]["cost"]
    elif inp == "latte":
        cost = MENU["latte"]["cost"]
    elif inp == "cappuccino":
        cost = MENU["cappuccino"]["cost"]
    return cost

def reduceResources(milk_left, coffee_left, water_left):
    if inp == "latte":
        milk_left -= latte_milk_required
        coffee_left -= latte_coffee_required
        water_left -= latte_water_required
    elif inp == "espresso":
        milk_left -= espresso_milk_required
        coffee_left -= espresso_coffee_required
        water_left -= espresso_water_required
    else:
        milk_left -= cappuccino_milk_required
        coffee_left -= cappuccino_coffee_required
        water_left -= cappuccino_water_required
    return milk_left, coffee_left, water_left
use = True
while use:
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    money_left = resources["money"]

    inp = input("What would you like? (espresso/latte/cappuccino): ")
    if inp == "off":
        break
    elif inp == "report":
        print(f"Water: {water_left}")
        print(f"Milk: {milk_left}")
        print(f"Coffee: {coffee_left}")
    else:
        able, not_enough = checkEnough(water_left, coffee_left, milk_left)
        if not able:
            print(f"Sorry there is not enough {not_enough}")
            break
        money_inserted = processCoins()
        cost = assignCost()
        if money_inserted >= cost:
            money_inserted += resources["money"]
            change = round(money_inserted - cost, 2)
            if change !=0 :
                print(f"Here is ${money_inserted - cost} in change.")
            print("Here is your coffee ☕. Enjoy!")
            milk_left, coffee_left, water_left = reduceResources(milk_left, coffee_left, water_left)
            resources["milk"] = milk_left
            resources["coffee"] = coffee_left
            resources["water"] = water_left
            resources["money"] += cost
        else:
            print("Sorry that's not enough money. Money refunded.")