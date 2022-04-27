# -*- coding: utf-8 -*-
"""
la funcion crea una tabla para el nuevo usuario.
Created on Tue Apr 12 11:37:31 2022

@author: Riki
"""
import mysql.connector
from user_list import user_list
def new_user():
    nombre=input("Ingrese un nombre de usuario:")
    buffer=user_list(nombre)
    while nombre==buffer:
        nombre=input("El nombre elegido esta ocupado, Ingrese otro nombre de usuario:")
        buffer=user_list(nombre)
    else:    
    #crea una tabla para el usuario nuevo con su nombre y comillas
    #ej jorge crea la tabla "'jorge'"
        cnx = mysql.connector.connect(user='root',
                                    password='Leo008008',
                                    host='localhost',
                                    database='cardio')
        curA = cnx.cursor(buffered=True)
        nombre_usuario=(nombre,)
        tarjeta1=input("hola %s que apodo queres ponerle a tu tarjeta?:"%nombre_usuario)
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
        tabla_nueva=TABLES['tabla_usuario']
        curA.execute(tabla_nueva,nombre_usuario)
        curA.close()
        cnx.close()
        #Busca el user id en user_list
        cnx = mysql.connector.connect(user='root',
                                    password='Leo008008',
                                    host='localhost',
                                    database='cardio')
        curD = cnx.cursor(buffered=True)
        useridsearch=("SELECT MAX(user_id) FROM lista_usuarios")
        curD.execute(useridsearch)
        user_id=max(curD.fetchone())
        curC = cnx.cursor(buffered=True)
        query=("INSERT INTO tarjetas_usuario (nombre_tarjeta,Dueño)"
               "VALUES (%(nombre_tarjeta)s,%(Dueño)s)")
        data_tarjeta={
            'nombre_tarjeta':tarjeta1,
            'Dueño':user_id,     
            }
        curC.execute(query,data_tarjeta)
        cnx.commit()
        curD.close()
        curC.close()
        cnx.close()
    
new_user()