# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:44 2022
Checkea si el nombre de usuario ya existe en la lista de usuarios de no ser
asi lo ingresa a la base de datos
@author: Riki
"""

import mysql.connector
def user_list(nombre):
    cnx = mysql.connector.connect(user='root',
                              password='Leo008008',
                              host='localhost',
                              database='cardio')
    curA = cnx.cursor(buffered=True)
    lista_usuarios="SELECT nombre_usuario FROM lista_usuarios"
    curA.execute(lista_usuarios)
    for nombre_usuario in curA:
        if nombre==nombre_usuario:
            curA.close()
            cnx.close()
            return nombre
    curA.close()
    cnx.close()
    
    nombre_usuario_tupple=(nombre,)
    cnx = mysql.connector.connect(user='root',
                              password='Leo008008',
                              host='localhost',
                              database='cardio')
    curB = cnx.cursor()
    agrega_nombre=("INSERT INTO lista_usuarios (nombre_usuario)"
                   "VALUES (%s)")
    curB.execute(agrega_nombre,nombre_usuario_tupple)
    user_id = curB.lastrowid
    cnx.commit()
    curB.close()
    cnx.close()
    return "ok"
