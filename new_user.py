# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:37:31 2022

@author: Riki
"""
import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='Leo008008', database='cardio')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Hay un error con el usuario o la contraseña.")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("No se encontro una base de datos con ese nombre.")
  else:
    print(err)
else:
  cnx.close()

def new_user(username):
    tarjeta1=input("hola", username,"que apodo queres ponerle a tu tarjeta?:")
    
    TABLES = {}
    TABLES[tarjeta1] = (
    "CREATE TABLE `",tarjeta1,"` ("
    "  `id_compra` int NOT NULL AUTO_INCREMENT,"
    "  `nombre_compra` varchar(20) NOT NULL,"
    "  `precio_total` int NOT NULL,"
    "  `cuotas_total` int NOT NULL,"
    "  `cuotas_pagadas` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")
   


    
    
    