
# Importação da biblioteca de socket
from socket import *

nomeServidor = '127.0.0.1'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_STREAM)

socketCliente.connect ((nomeServidor, portaServidor))

# Python 2
# frase = raw_input ('Informe uma frase em letras minusculas: ')

# Python 3
frase = input ('Informe uma frase em letras minusculas: ')

socketCliente.send (frase.encode())

fraseModificada = socketCliente.recv (1024)

# Python 2
# print "Do Servidor: ", fraseModificada

# Python 3
print ("Do Servidor: ", fraseModificada.decode())

socketCliente.close ()