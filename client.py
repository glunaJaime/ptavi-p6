#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket

# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = 'localhost'
METHOD = sys.argv[1]
DIR = sys.argv[2]
LOGIN = DIR.split('@')[0]
IP = DIR.split(':')[0], split('@')[1]
PORT = int(DIR.SPLIT(':')[1])


# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
