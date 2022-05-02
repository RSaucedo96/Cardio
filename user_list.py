# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:44 2022
Checkea si el nombre de usuario ya existe en la lista de usuarios de no ser
asi lo ingresa a la base de datos
@author: Riki
"""

import mysql.connector


def user_list(name):
    cnx = mysql.connector.connect(user='root',
                                  password='Leo008008',
                                  host='localhost',
                                  database='cardio')
    cur_a = cnx.cursor(buffered=True)
    user_list = "SELECT nombre_usuario FROM lista_usuarios"
    cur_a.execute(user_list)
    for nombre_usuario in cur_a:
        if name == nombre_usuario:
            cur_a.close()
            cnx.close()
            return name
    cur_a.close()
    cnx.close()

    user_name_tupple = (name,)
    cnx = mysql.connector.connect(user='root',
                                  password='Leo008008',
                                  host='localhost',
                                  database='cardio')
    cur_b = cnx.cursor()
    add_name = ("INSERT INTO lista_usuarios (nombre_usuario)"
                "VALUES (%s)")
    cur_b.execute(add_name, user_name_tupple)
    user_id = cur_b.lastrowid
    cnx.commit()
    cur_b.close()
    cnx.close()
    return "ok"
