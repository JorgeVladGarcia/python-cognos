'''
1. Indicar el número de caracteres a leer, mostrar el texto recibido con
socket y mostrar la cantidad de caracteres recibidos del archivo
http://data.pr4e.org/romeo.txt
• Importar el módulo socket
• Teclear el número de caracteres a leer
• Pasar por try-except el dato tecleado por el usuario
• Mostrar el texto recibido de acuerdo con el número de caracteres tecleados
• Mostrar la cantidad de caracteres recibidos
'''
import socket

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
try:
    crec = int(input("Dame la cant. de caracteres a recibir: "))
    data = misock.recv(crec)
    #print(data.decode())
    #print(type(data))
    print("Cant. de caracteres recibidos:", len(data))
    misock.close()
except:
    print("Dame solo numeros enteros ya?...")
