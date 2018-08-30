from socket import *

portaServidor = 12000

socketServidor = socket (AF_INET, SOCK_STREAM)

socketServidor.bind (('', portaServidor))

socketServidor.listen (1)

# Python 2
# print "O servidor esta pronto para receber"

# Python 3
print ("O servidor esta pronto para receber")

while 1 :

    socketConexao, endereco = socketServidor.accept ()

    frase = socketConexao.recv (1024)

    fraseMaiscula = frase.upper ()

    socketConexao.send (fraseMaiscula)

    socketConexao.close ()