# -*- coding: utf-8 -*-
"""
la funcion crea una tabla para el nuevo usuario.
Created on Tue Apr 12 11:37:31 2022

@author: Riki
"""
import mysql.connector
import user_list
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
        nombre_usuario=(buffer,)
        tarjeta1=(input("hola %s que apodo queres ponerle a tu tarjeta?:"%nombre_usuario),)
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
        curB = cnx.cursor(buffered=True)
        useridsearch=("SELECT user_id FROM lista_usuarios" 
                      "WHERE nombre_usuario=`%s`;")
        curB.execute(useridsearch,nombre_usuario)
        useridinsert=curB
        curB.close()
        cnx.close()
        #ingresa el user_id y su tarjeta en la tabla de tarjetas
        cnx = mysql.connector.connect(user='root',
                                    password='Leo008008',
                                    host='localhost',
                                    database='cardio')
        curC = cnx.cursor(buffered=True)
        query=("INSERT INTO tarjetas (nombre_tarjeta,Dueño)"
               "VALUES ('%s',%d);")
        curC.execute(query,(tarjeta1,useridinsert))
        curC.close()
        cnx.close()
    
new_user()