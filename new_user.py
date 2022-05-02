# -*- coding: utf-8 -*-
"""
la funcion crea una tabla para el nuevo usuario.
Created on Tue Apr 12 11:37:31 2022

@author: Riki
"""
import mysql.connector
from user_list import user_list


def new_user():
    name = input("Ingrese un nombre de usuario:")
    buffer = user_list(name)
    while name == buffer:
        name = input("El nombre elegido esta ocupado, Ingrese otro nombre de usuario:")
        buffer = user_list(name)
    else:    
    #crea una tabla para el usuario nuevo con su nombre y comillas
    #ej jorge crea la tabla "'jorge'"
        cnx = mysql.connector.connect(user='root',
                                      password='Leo008008',
                                      host='localhost',
                                      database='cardio')
        cur_a = cnx.cursor(buffered=True)
        user_name = (name,)
        card = input("hola %s que apodo queres ponerle a tu tarjeta?:" %user_name)
        TABLES = {}
        TABLES['tabla_usuario'] = (
            "CREATE TABLE `%s` ("
            "  `id_compra` int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
            "  `nombre_compra` varchar(20) NOT NULL,"
            "  `precio_total` int NOT NULL,"
            "  `cuotas_total` int NOT NULL,"
            "  `cuotas_pagadas` date NOT NULL,"
            "  `tarjeta_usada` int,"
            "  FOREIGN KEY(`tarjeta_usada`) REFERENCES tarjetas(`id_tarjeta`) ON DELETE SET NULL"
            "); ENGINE=InnoDB")    
        tabla_nueva = TABLES['tabla_usuario']
        cur_a.execute(tabla_nueva,user_name)
        cur_a.close()
        cnx.close()
        #Busca el user id en user_list
        cnx = mysql.connector.connect(user='root',
                                    password='Leo008008',
                                    host='localhost',
                                    database='cardio')
        cur_d = cnx.cursor(buffered=True)
        user_id_search = ("SELECT MAX(user_id) FROM lista_usuarios")
        cur_d.execute(user_id_search)
        user_id = max(cur_d.fetchone())
        cur_c = cnx.cursor(buffered=True)
        query = ("INSERT INTO tarjetas_usuario (nombre_tarjeta,Dueño)"
                 "VALUES (%(nombre_tarjeta)s,%(Dueño)s)")
        card_data = {
                        'nombre_tarjeta': card,
                        'Dueño': user_id,
            }
        cur_c.execute(query, card_data)
        cnx.commit()
        cur_d.close()
        cur_c.close()
        cnx.close()
