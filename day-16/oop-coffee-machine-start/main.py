from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from data import MENU, resources


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"Enter  {options}: ")
    if choice == "off":
        is_on =False
    elif choice  == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)







# print(items.cost)
# choice = input(f"Enter  {menu.get_items()}: ")
# menu.find_drink(choice)
#
# item = MenuItem(choice,30, 30, 30, 2.5)
#
# cost = item.cost
# print(cost)


# order.find_drink(item.name)
# machine.report()
#
# if money_machine.make_payment(cost):
#     if coffee_machine.is_resource_sufficient(item):
#         coffee_machine.make_coffee(item)
