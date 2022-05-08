# -*- coding: utf-8 -*-
import mysql.connector
from user_list import user_list_add
import constants as cons


def new_user():
    cnx = mysql.connector.connect(user=cons.DBUSER,
                                  password=cons.DBPW,
                                  host=cons.DBHOST,
                                  database=cons.DBNAME)
    cur_a = cnx.cursor(buffered=True)
    name = input("Write your username:")
    user_list_from_database = "SELECT nombre_usuario FROM lista_usuarios"
    cur_a.execute(user_list_from_database)
    while name in cur_a:
        name = input("That username is not available, please choose a different one:")
    user_list_add(name)
    cur_a.close()
    cnx.close()
    # Creates a table for the new user called like the user
    # example creates a table called "'jorge'" for user jorge
    cnx = mysql.connector.connect(user=cons.DBUSER,
                                  password=cons.DBPW,
                                  host=cons.DBHOST,
                                  database=cons.DBNAME)
    cur_a = cnx.cursor(buffered=True)
    user_name = (name,)
    card = input("Hello %s, how do you wanna name your card?:" % user_name)
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
    cur_a.execute(tabla_nueva, user_name)
    cur_a.close()
    cnx.close()
    # search for user id in the database user list
    cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
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
