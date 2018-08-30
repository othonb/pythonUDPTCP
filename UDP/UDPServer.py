from socket import *

portaServidor = 12000

socketServidor = socket (AF_INET, SOCK_DGRAM)

socketServidor.bind (('', portaServidor))

print ("O servidor esta pronto para receber")

while 1 : 

    frase, enderecoCliente = socketServidor.recvfrom (2048)

    fraseModificada = frase.upper ()

    socketServidor.sendto (fraseModificada, enderecoCliente)

