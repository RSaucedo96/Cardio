# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:38:02 2022
Menu Inicial
@author: Riki
"""
from new_user import new_user
from delete_user import delete_user
from user_menu import user_menu
menu = {'1': "New User.", '2': "Delete User.", '3': "Find User", '4': "Exit"}
while True:
    opciones = menu.keys()
    opciones.sort()
    for entrada in opciones:
      print("entrada", menu[entrada])

    selection=input("Choose an option:")
    if selection =='1':
      new_user()
    elif selection == '2':
      delete_user
     elif selection == '3':
      eleccion_usuario=input("Ingrese su nombre de usuario:")
      user_menu(eleccion_usuario)
    elif selection == '4':
      break
    else:
      print ("Opcion desconocida") 