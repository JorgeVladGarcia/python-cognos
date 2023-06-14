'''
Crear mediante un programa el árbol XML de la información Covid-19 de la
OMS correspondiente a parte del mes de febrero 2022 del país y verificar
que la estructura del árbol XML creado es correcta.
• Los datos Covid-19 de la OMS están en el archivo Covid19-Bol.txt
• Crear mediante un programa de Python el árbol XML respectivo, Covid19-Bol.xml
• La etiqueta principal del programa debe ser: OMS_Bolivia y para el resto de las
etiquetas utilizar los encabezados de la primer línea.
• Verificar con el navegador de la máquina que el archivo XML creado es correcto
• Crear otro programa para listar los datos originales de cada día.
'''

# Importar librerias
import re
import xml.etree.ElementTree as ET

# Abrir archivos
f = open("Covid19-Bol.txt")
save = open("Covid19-Bol.xml", "w")

# crear variables vacías
data = []
i = -1

# Limpiar datos (borrar primera lista de la sublista)
for line in f:
	line = line.rstrip()
	line = line.split("\t")
	data.append(line)
	clean = data[1:]

# Guardar datos
save.write('<?xml version="1.0" encoding="UTF-8"?>\n')
save.write('<OMS_Bolivia>\n')
for element in clean:
	i += 1
	save.write('<fecha'+ ' fecha = '+ '"' +str(clean[i][0])+ '"'+ '>\n')
	save.write('<cod_pais>'+ clean[i][1] + '</cod_pais>\n')
	save.write('<pais>' + clean[i][2] + '</pais>\n')
	save.write('<region_WHO>' + clean[i][3] + '</region_WHO>\n')
	save.write('<casos_compr>' + clean[i][4] + '</casos_compr>\n')
	save.write('<cc_acumul>' + clean[i][5] + '</cc_acumul>\n')
	save.write('<muertes>' + clean[i][6] + '</muertes>\n')
	save.write('<m_acumul>'+ clean[i][7] + '</m_acumul>\n')
	save.write('</fecha>\n')	
save.write('</OMS_Bolivia>')

# Cerrar archivos
f.close()
save.close()


'''
CREAR PROGRAMA PARA LISTAR LOS DATOS DE CADA DÍA
'''
# abrir archivos
datos = open("Covid19-Bol.xml")

# crear arbik xml 
arbol = ET.parse(datos)
rama = arbol.findall("fecha")

# imprimir resultados
for item in rama:
    print("\nFecha:", item.get("fecha"))
    print("Casos comprobados", item.find("casos_compr").text)
    print("Casos acumulados:", item.find("cc_acumul").text)
    print("Num. muertes:", item.find("muertes").text)
    print("Num. muertes acumuladas:", item.find("m_acumul").text)

# cerrar archivos
datos.close()    
