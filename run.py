# -*- coding: utf-8 -*-
from user import User
from item import Item


def main():
    menu = {'1': "New User.", '2': "Delete User.", '3': "Find User", '4': "Exit"}
    users = {}
    while True:
        opciones = menu.keys()
        for entrada in opciones:
            print(f"{menu[entrada]}")

        selection = input("Choose an option:")
        if selection == '1':
            name = input("Welcome, What username will you use?:")
            users[name] = User(name)
            users[name].new_user()
        elif selection == '2':
            # delete_user
            pass
        elif selection == '3':
            user_select = input("Ingrese su nombre de usuario:")
            users[user_select].validate_user()
            user_menu(user_select)
        elif selection == '4':
            break
        else:
            print("Error, unknown option selected")


def user_menu(user_select):
    items = {}
    Item.instantiate_from_db(user_select)
    menu = {'1': "Add Item.", '2': "Update Item.", '3': "Check Balance", '4': "Exit"}
    while True:
        opciones = menu.keys()
        for entrada in opciones:
            print("entrada", menu[entrada])

        selection = input("Choose an option:")
        if selection == '1':
            item_name = str(input("what is the name of the item?:"))
            item_cost = float(input("how much it costs?"))
            item_total_payments = int(input("How many payments?:"))
            item_payments_done = int(input("How many of those payments did you complete? if the answer is none input 0:"))
            items[item_name] = Item(item_name, item_cost, item_total_payments, item_payments_done)
            items[item_name].update_item_to_db()

        elif selection == '2':
            pass
            # update item
        elif selection == '3':
            pass
            # check balance
        elif selection == '4':
            break
        else:
            print("Error, unknown option selected")


main()
