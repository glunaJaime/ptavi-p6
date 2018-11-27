#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


if len(sys.argv) != 4:
    sys.exit('Usage: python server.py IP PORT audio_file')
else:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    if sys.argv[3] == "cancion.mp3":
        AUDIO_FILE: sys.argv[3]
    else:
        sys.exit("the third argument must be <cancion.mp3>")


class EchoHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        #self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            #print("El cliente nos manda " + line.decode('utf-8'))

            method = line.decode('utf-8').split(' ')[0]
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            if method == 'INVITE':
                print("El cliente nos manda " + line.decode('utf-8'))
                message = b"SIP/2.0 100 Trying SIP/2.0 180 Ring SIP/2.0 200 Ok"
                self.wfile.write(message)
            elif method == 'ACK':
                #print("llega")
                # aEjecutar es un string
                # con lo que se ha de ejecutar en la shell:
                aEjecutar = ('./mp32rtp -i 127.0.0.1 -p 23032 <' + sys.argv[3])
                print("Vamos a Ejecutar: ", aEjecutar)
                #message = b"SIP/2.0 200 OK \r\n\r\n"
                os.system(aEjecutar)
                print("Cancion Enviada")
            elif method == 'BYE':
                message = b"SIP/2.0 200 Ok \r\n\r\n"
                self.wfile.write(message)
            else: 
                sys.exit("METHOD not allowed")
                sel.wfile.write(b'SIP/2.0 400 Bad Request \r\n\r\n')

			
if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    try:
        serv = socketserver.UDPServer((IP, PORT), EchoHandler)
        print("Listening.........")
        serv.serve_forever()
    except KeyboardInterrupt:
        print("finalizado")
