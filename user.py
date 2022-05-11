import mysql.connector
import constants as cons


class User:
    all_users = []

    def __init__(self, user_name: str):
        self.user_name = user_name
        User.all_users.append(self)

    def new_user(self):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_a = cnx.cursor(buffered=True)
        user_list_from_database = "SELECT nombre_usuario FROM lista_usuarios"
        cur_a.execute(user_list_from_database)
        while self.user_name in cur_a
            self.user_name = input("That username is not available, please choose a different one:")
        cur_a.close()
        self.user_list_add()
        self.create_user_table()
        self.new_card()
        cnx.close()
        return

    def user_list_add(self):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_b = cnx.cursor()
        user_name_tuple = (self.user_name,)
        add_name = ("INSERT INTO lista_usuarios (nombre_usuario)"
                    "VALUES (%s)")
        cur_b.execute(add_name, user_name_tuple)
        user_id = cur_b.lastrowid
        cnx.commit()
        cur_b.close()
        cnx.close()
        return

    def create_user_table(self):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_a = cnx.cursor(buffered=True)
        user_name_tuple = (self.user_name,)
        new_table_query= """CREATE TABLE %s (
                        id_compra int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        nombre_compra varchar(20) NOT NULL,
                        precio_total int NOT NULL,
                        cuotas_total int NOT NULL,
                        cuotas_pagadas date NOT NULL,
                        tarjeta_usada int,
                        FOREIGN KEY(tarjeta_usada) REFERENCES tarjetas(id_tarjeta) ON DELETE SET NULL) """
        cur_a.execute(new_table_query, user_name_tuple)
        cnx.commit()
        cur_a.close()
        cnx.close()

    def new_card(self):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_d = cnx.cursor(buffered=True)
        user_id_search = ("SELECT MAX(user_id) FROM lista_usuarios")
        cur_d.execute(user_id_search)
        user_id = max(cur_d.fetchone())
        cur_c = cnx.cursor(buffered=True)
        card = input("How do you wanna name your card?:" % self.user_name)
        insert_card_query = ("INSERT INTO tarjetas_usuario (nombre_tarjeta,Dueño)"
                             "VALUES (%(nombre_tarjeta)s,%(Dueño)s)")
        card_data = {
            'nombre_tarjeta': card,
            'Dueño': user_id,
        }
        cur_c.execute(insert_card_query, card_data)
        cnx.commit()
        cur_d.close()
        cur_c.close()
        cnx.close()

