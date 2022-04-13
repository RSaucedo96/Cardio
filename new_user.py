# -*- coding: utf-8 -*-
"""
la funcion crea una tabla para el nuevo usuario.
Created on Tue Apr 12 11:37:31 2022

@author: Riki
"""
import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='root',
                                password='Leo008008',
                                host='localhost',
                                database='cardio')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Hay un error con el usuario o la contraseña.")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("No se encontro una base de datos con ese nombre.")
  else:
    print(err)
else:
  cnx.close()

from user_list.py import user_list
def new_user():
    nombre_usuario=input("Ingrese un nombre de usuario:")
    check=user_list(nombre_usuario)
    while nombre_usuario==check:
        nombre_usuario=input("Ese nombre ya esta tomado, por favor ingrese otro:")
        check=user_list(nombre_usuario)
    tarjeta1=input("hola", nombre_usuario,"que apodo queres ponerle a tu tarjeta?:")
    TABLES = {}
    TABLES[nombre_usuario] = (
    "CREATE TABLE `",nombre_usuario,"` ("
    "  `id_compra` int NOT NULL AUTO_INCREMENT,"
    "  `nombre_compra` varchar(20) NOT NULL,"
    "  `precio_total` int NOT NULL,"
    "  `cuotas_total` int NOT NULL,"
    "  `cuotas_pagadas` date NOT NULL,"
    "  `tarjeta_usada` int NOT NULL,"
    "  FOREIGN KEY(`tarjeta_usada`) REFERENCES tarjetas(id_tarjeta) ON DELETE SET NULL"
    "  PRIMARY KEY (`id_compra`)"
    ") ENGINE=InnoDB")
    
   


    
    
    