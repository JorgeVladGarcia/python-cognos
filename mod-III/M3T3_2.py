'''
Contar las etiquetas de párrafo (p) del documento HTML de
Wikipedia del ejercicio de clase 1
• Importar las librerías necesarias
• Contar las etiquetas de párrafo (p)
• Mostrar la cantidad total de etiquetas encontradas, dato que debe coincidir con lo
que indica la opción de búsqueda en dicha página
'''

# Busqueda de enlaces a páginas web dentro de las entradas URL
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# La librería SSL permite acceder a los sitios web HTTPS
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cont = 0
url = "https://en.wikipedia.org/wiki/Main_Page"
# url = "https://docs.python.org/3/"
html = urllib.request.urlopen(url, context=ctx).read()
# links = re.findall(b'href="(http[s]?://.*?)"', html)
links = re.findall(b'<p>', html)
for link in links:
    cont += 1
#    print(link.decode())
print("Cantidad:", cont)