'''
Contar la cantidad de palabras del encabezado que contengan
letras, dos puntos (:) y comas (,) del archivo binario
http://data.pr4e.org/cover.jpg
• Importar socket
• Abrir la pagina web y leer el archivo
• Seleccionar y contar las palabras que contengan letras, (:) y (,)
• Mostrar en pantalla el texto completo del encabezado del archivo
• Mostrar las palabras contadas y la cantidad total de las mismas (deben ser 19).
'''
import socket
import time
import re 

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\r\n\r\n')
cont = 0
picture = b""

while True:
    data = mysock.recv(10000)
    if len(data) < 1: break
#    time.sleep(0.25)
    #count = count + len(data)
    #print(len(data), count)
    picture = picture + data

mysock.close()

# Busca el final de la cabecera (2 CRLF)
pos = picture.find(b"\r\n\r\n")
final = picture[:pos].decode()

print("Encabezado:")
print(final)

cont = 0
for i in final:
    if i == ":":
        cont+= 1

print("\nNum. de palabras contadas es:", cont)


#dos_puntos = re.findall()


#print(final)