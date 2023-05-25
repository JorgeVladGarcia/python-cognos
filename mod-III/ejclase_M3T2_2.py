'''
Contar la cantidad de palabras idénticas que tiene el archivo
http://data.pr4e.org/romeo.txt
• Importar la librería urllib
• Abrir la página web que contiene el archivo romeo.txt
• Leer el contenido del archivo
• Contar las palabras idénticas que se vayan encontrando
• Mostrar en pantalla la palabra y su cantidad de aparicione
'''


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

cont = 0
acum = 0
while True:
    data = mysock.recv(200)
    if len(data) < 1:
        break
    print(data.decode())
    cont += 1
    acum += len(data)
    print("Veces:", cont, "Datos Acumulados:", acum)

mysock.close()
