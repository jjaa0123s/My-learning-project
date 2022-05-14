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
}





def money_coffee(command):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    client_money = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    if client_money > MENU[command]["cost"]:
        change_money = round(client_money - MENU[command]["cost"], 2)
        print(f"Here is ${change_money} in charge.")
        print(f"Here is your {command}. Enjoy!")
        return MENU[command]["cost"]
    elif client_money < MENU[command]["cost"]:
        print("“Sorry that's not enough money. Money refunded.")
        ingredients = MENU[command]["ingredients"]  # 要記得"ingredients" 是字串
        for value in ingredients:
            resources[value] = resources[value] + ingredients[value]
        return 0


def ingredient_coffee(command):
    ingredients = MENU[command]["ingredients"]  # 要記得"ingredients" 是字串
    for value in ingredients:
        assume_value = resources[value] - ingredients[value]
        if assume_value < 0:
            print(f"Sorry there is not enough {value}")
            return False
    for value in ingredients:
        resources[value] = resources[value] - ingredients[value]
    return True


def different_coffee(command):
    ingredient_part = ingredient_coffee(command)
    if ingredient_part:
        return money_coffee(command)


keep_asking = True
earned_money = 0

while keep_asking:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: ${earned_money}")
    elif command == "off":
        # exit()
        keep_asking = False
    elif command == "espresso":
        esp = different_coffee(command)
        earned_money = earned_money + esp
    elif command == "latte":
        lat = different_coffee(command)
        earned_money = earned_money + lat
    elif command == "cappuccino":
        cap = different_coffee(command)
        earned_money = earned_money + cap


# 如果咖啡夠 錢不夠 料也會減少
# 上述問題解決但又製造了材料會變多的問題








