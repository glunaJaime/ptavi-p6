#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
if len(sys.argv)!=3:
	sys.exit('Usage: python client.py method reciever@IP:SIPport')


# Dirección IP del servidor.
SERVER = 'localhost'
PORT = 6001

try:
	# Contenido que vamos a enviar
	LINE = '¡Hola mundo!'

	METHOD = sys.argv[1]
	DIR = sys.argv[2]
	LOGIN = DIR.split('@')[0] 
	IP = DIR.split(':')[0].split('@')[1]
	PORT = int(DIR.split(':')[1])
except:
	sys.exit('Usage: python client.py method reciever@IP:SIPport')

	#Enviamos:
LINE = METHOD + ' sip:' + DIR + '@' + IP + 'SIP/2.0\r\n\r\n'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
	my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	my_socket.connect((IP, PORT))

	print("Enviando: " + LINE)
	my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
	data = my_socket.recv(1024)

#Envio el ACK en caso de recibir el TRYING, RING y OK
message = data.decode('utf-8')
if message == ['SIP/2.0 100 Trying', 'SIP/2.0 180 Ring','SIP/2.0 200 Ok']:
	ms_ack = 'ACK' + DIR + '@' + IP + 'SIP/2.0\r\n\r\n'
	print("Enviamos: " + ms_ack)
	my_socket.send(bytes(ms_ack, 'utf-8') + b'\r\n\r\n')
if message == b"SIP/2.0 200 OK \r\n\r\n":
	print("ACK recibido")
	
print("Terminando socket...")

print("Fin.")
