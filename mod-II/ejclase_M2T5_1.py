'''
Mostrar en Excel la lista de datos Covid de los países indicados en el
archivo insertando 0 en las casillas donde no hay datos.
• Revisar y abrir el archivo “Paises_SA.txt”
• Leer los datos del archivo y rellenar los espacios en blanco con 0
• Convertir los datos en formato adecuado para Excel en el archivo PBACH.txt
• Migrar la información resultante al programa Excel
• Mostrar en Excel los datos completos
'''
march = open("Paises_SA.txt")
lp = list()
for linea in march:
    dato = linea.split("\t")
    if dato[0] == "Fecha":
        x = ""
        for n in range(5):
            x += dato[n]+","
        lp.append(x[:-1])
        continue
    if dato[1] == "": x = dato[0]+",0"
    else: x = dato[0]+","+dato[1]
    if dato[2] == "": x += ",0"
    else: x += ","+dato[2]
    if dato[3] == "": x += ",0"
    else: x += ","+dato[3]
    if dato[4] == "\n": x += ",0\n"
    else: x += ","+dato[4]
    lp.append(x)
print(lp)

fout = open("PBACH.txt", "w")
for dato in lp:
    fout.write(dato)
fout.close()
march.close()
