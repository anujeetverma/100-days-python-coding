from data import MENU, resources
#TODO 1: create a function that will take input from the user Prompt user by asking prompts like off and report and
# “What would you like? (espresso/latte/cappuccino):
def take_choice():
    choice =''
    while choice not in ['espresso','latte','cappuccino','report','off']:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower().strip()
    return choice

#todo 2: collect the money from the user:
def take_money():
    print("please insert coins:")
    quarter = int(input("How many quarter: "))
    dimes = int(input("How many dimes: "))
    nickle = int(input("How many  nickle: "))
    pennies = int(input("How manu pennies: "))
    return quarter,dimes,nickle,pennies

#todo 3: maf that will check for constrain in the coins whether is sufficient or not return the money back if fails (check point)
def money_constrain(choice, quarter,dimes,nickle,pennies):
    cost = MENU[choice]['cost']
    money_paid = (quarter*0.25) + (dimes * 0.10) + (nickle * 0.5) + (pennies * 0.1)
    if money_paid < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print("Ok thank you!!! processing your order")
        return True

#todo returns the value of money left over
def return_money(choice, quarter,dimes,nickle,pennies):
    cost = MENU[choice]['cost']
    money_paid = (quarter * 0.25) + (dimes * 0.10) + (nickle * 0.5) + (pennies * 0.1)
    if money_constrain(choice, quarter,dimes,nickle,pennies):
        return_money = money_paid - cost
        return return_money


#todo 4:make a function that will check for the constrain of resources to make the coffee return whats limited (check point)
def resource_constrains(choice,resources):
    if resources['water'] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    elif resources['milk'] < MENU[choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif resources['coffee'] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffe")
        return False
    else:
        return True


#todo 5: a function that handels the resources and subtracts the resources
def coffee_machine(choice):

    if choice == "espresso":
        resources['water'] -= 50
        resources['coffee'] -= 18
        print(f"Here is your {choice} ☕️. Enjoy!")

    elif choice == "latte":
        resources['water'] -= 200
        resources['coffee'] -= 24
        resources['milk'] -= 150
        print(f"Here is your {choice} ☕️. Enjoy!")

    elif choice == "cappuccino":
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100
        print(f"Here is your {choice} ☕️. Enjoy!")

    elif choice == "report":
        for item in resources:
            print(f'{item} = {resources[item]}')

    elif choice == "off":
        print("Machine turned off for maintenance")


def special_maintenance(choice):
    if choice == "report":
        for item in resources:
            print(f'{item} = {resources[item]}')

    elif choice == "off":
        print("Machine turned for maintenance")


#todo 5: maf that will check for constrain in the coins whether is sufficient or not return the money back if fails (check point)
choice = ''
while choice != 'off':
    choice = take_choice()
    if choice in ['off','report']:
        special_maintenance(choice)
    else:


        if resource_constrains(choice, resources):
            quarter, dimes, nickle, pennies = take_money()
            if money_constrain(choice, quarter,dimes,nickle,pennies):
                coffee_machine(choice)
                print(f"Here is ${return_money(choice, quarter,dimes,nickle,pennies)} in change.")




