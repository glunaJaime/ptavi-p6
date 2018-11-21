#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
if len(sys.argv)!=3
sys.exit('Usage: python client.py method reciever@IP:SIPport')


# Dirección IP del servidor.
SERVER = 'localhost'
PORT = 6001


# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

SERVER = 'localhost'
METHOD = sys.argv[1]
DIR = sys.argv[2]
LOGIN = DIR.split('@')[0] 
IP = DIR.split(':')[0], split('@')[1]
PORT = int(DIR.SPLIT(':')[1])


#Enviamos:
LINE = METHOD + 'sip:' + RECEPTOR + '@' + IP + 'SIP/2.0\r\n\r\n'



# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP, PORT))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

#Envio el ACK en caso de recibir el TRYING, RING y OK
rec_invite = data.decode('utf-8').split('\r\n\r\n')[0:-1]
    
    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
