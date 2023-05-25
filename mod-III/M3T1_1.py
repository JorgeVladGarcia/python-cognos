'''
Extraer y mostrar datos del archivo “correos.txt”
• Buscar en las líneas leídas aquellas que tienen un correo electrónico y una dirección
IP utilizando expresiones regulares
• Mostrar en pantalla el resultado de la búsqueda:
Correo: xxxxxxx, IP respectiva: yyyyyyyy
'''

import re
arch = open("correos.txt")

for linea in arch:
    linea = linea.rstrip()
    corr = re.findall(r'[a-zA-Z0-0]\S+@\S+[a-zA-Z]', linea)
    yy = re.findall('\[([0-9.]+)', linea)
    for mail in corr:
        mail = str(corr[0])
    for ip in yy:
        ip = str(yy[0])
        print("Correo:", mail, "IP respectiva:", ip)
