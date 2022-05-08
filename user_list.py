# -*- coding: utf-8 -*-
import mysql.connector
import constants as cons


def user_list_add(name):

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
    return
