# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:38:02 2022
Menu Inicial
@author: Riki
"""
from new_user.py import new_user
menu = {}
menu['1']="Agregar Usuario." 
menu['2']="Borrar Usuario."
menu['3']="Encontrar Usuario"
menu['4']="Exit"
while True: 
  opciones=menu.keys()
  opciones.sort()
  for entrada in opciones: 
      print ("entrada", menu[entrada])

  selection=input("Elija una opcion:") 
  if selection =='1': 
      new_user 
  elif selection == '2': 
      delete_user
  elif selection == '3':
      user_list
  elif selection == '4': 
      break
  else: 
      print ("Opcion desconocida") 