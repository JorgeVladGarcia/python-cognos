import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(10000)
    if len(data) < 1: break
#    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Busca el final de la cabecera (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Longuitud de la Cabecera', pos)
print(picture[:pos].decode())

# Ignorar la cabecera y guardar los datos de la imagen
#picture = picture[pos+4:]

#fhand = open("imagen.jpg", "wb")
#fhand.write(picture)
#fhand.close()

