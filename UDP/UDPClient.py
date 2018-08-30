from socket import *

nomeServidor = '127.0.0.1'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_DGRAM)

# Python 2
# frase = raw_input ('Informe uma frase com letras minusculas: ')

# Python 3
frase = input ('Informe uma frase com letras minusculas: ')

# Python 2
# socketCliente.sendto (frase, (nomeServidor, portaServidor))

# Python 3
socketCliente.sendto (frase.encode(), (nomeServidor, portaServidor))

fraseModificada, enderecoServidor = socketCliente.recvfrom (2048)

# Python 2
# print fraseModificada

# Python 3
print (fraseModificada.decode())

socketCliente.close ()