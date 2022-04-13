# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:44 2022
Checkea si el nombre de usuario ya existe en la lista de usuarios de no ser
asi lo ingresa a la base de datos
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

def user_list(nombre_usuario):
    buffer=str(nombre_usuario)
    user_list=[]
    if buffer in user_list:
        return(nombre_usuario)
    else:    
        user_list.append(buffer)
            