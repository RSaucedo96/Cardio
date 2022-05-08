# -*- coding: utf-8 -*-
import mysql.connector
import constants as cons


def user_list(name):
    cnx = mysql.connector.connect(user=cons.DBUSER,
                                  password=cons.DBPW,
                                  host=cons.DBHOST,
                                  database=cons.DBNAME)
    cur_a = cnx.cursor(buffered=True)
    user_list_from_database = "SELECT nombre_usuario FROM lista_usuarios"
    cur_a.execute(user_list_from_database)
    for nombre_usuario in cur_a:
        if name == nombre_usuario:
            cur_a.close()
            cnx.close()
            return name
    cur_a.close()
    cnx.close()

    user_name_tuple = (name,)
    cnx = mysql.connector.connect(user=cons.DBUSER,
                                  password=cons.DBPW,
                                  host=cons.DBHOST,
                                  database=cons.DBNAME)
    cur_b = cnx.cursor()
    add_name = ("INSERT INTO lista_usuarios (nombre_usuario)"
                "VALUES (%s)")
    cur_b.execute(add_name, user_name_tuple)
    user_id = cur_b.lastrowid
    cnx.commit()
    cur_b.close()
    cnx.close()
    return "ok"
