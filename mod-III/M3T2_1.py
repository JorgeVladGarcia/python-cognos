'''
1. Mostrar solo el texto del archivo leído sin encabezado con
socket del archivo http://data.pr4e.org/romeo.txt
• Importar socket
• Abrir la pagina web y leer el archivo
• Mostrar en pantalla solo el contenido del archivo, no encabezado ni línea en blanco
'''
# importar libreria
import socket

# setear ambiente
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0
text = b""

while True:
    data = mysock.recv(200)
    if len(data) < 1:
        break
    count = count + len(data)
    text = text + data

mysock.close()

# bsucar el final de la cabecera
pos = text.find(b"\r\n\r\n")
# Ignorar la cabecera y guardar los datos del texto
to_print = text[pos+4:]
# Imprimir resultados 
print(to_print.decode())