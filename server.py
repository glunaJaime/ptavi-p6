#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


if len(sys.argv)!=4:
	sys.exit('Usage: python server.py IP PORT audio_file')
else:
	IP = sys.argv[1]
	PORT = int(sys.argv[2])
	if sys.argv[3] == "cancion.mp3":
		AUDIO_FILE: sys.argv[3]
	else:
		sys.exit("the third argument must be <cancion.mp3>")	

print("Listening ...")


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
	METHODS = ['INVITE', 'ACK', 'BYE']

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
			text = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

			method = text.decode('utf-8').split(' ')[0]

			if method !== METHODS:
				sys.exit("METHOD not allowed")
			elif method == 'INVITE':
				message = b"SIP/2.0 100 \r\n\r\n Trying SIP/2.0 180 Ring \r\n\r\n SIP/2.0 200 Ok"
				self.wfile.write(message)
			elif method == 'ACK':


            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
