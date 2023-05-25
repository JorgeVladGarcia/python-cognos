'''
Descargar los datos crudos Covid-19 de la Organización Mundial de la Salud
(OMS) con el URL siguiente y procesar de acuerdo a lo indicado
https://covid19.who.int/WHO-COVID-19-global-data.csv
• Descargar y guardar los datos en el archivo Covid19-Mundial.txt
• Elaborar un programa Python para convertir esos datos en formato JSON
• Mostrar en pantalla los datos del mes de abril-2022 del país Brasil
• Obtener el total y promedio de Casos covid y de fallecimientos de los datos mostrados
'''

import urllib.request

outf = open("M3T3-T2-Datos-Crudos.txt", "w")
fhand = urllib.request.urlopen("https://covid19.who.int/WHO-COVID-19-global-data.csv")

for i in fhand:
    outf.write(str(i) + '\n')
outf.close()

#nn = 0
#
#for line in fhand:
#    linea = line.strip().decode()
#    datos = linea.split(",")
#    print(datos)
#    nn += 1
#    if nn == 5: break
#
#for i in fhand:
#    outf.write(str(i) + "\n")
outf.close()

'''    
for line in fhand:
    print(line.decode().strip())
'''