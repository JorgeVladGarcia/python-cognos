'''
Obtener y mostrar los totales y promedio diario de los casos Covid de
los países y periodos indicados.
• Revisar y abrir el archivo “PBACH.txt”
• Procesar los países y períodos siguientes: Argentina (del 25-abr-2020 al 17-ago-2020),
Bolivia (del 18-jul-2020 al 5-dic-2020), Perú (del 23-sept-2020 al 8-ene-2021) y Chile (del
29-dic-2020 al 10-febr.-2021).
• Calcular para cada país el total y promedio diario de datos Covid de los periodos indicados
• Mostrar en pantalla los datos calculados.
'''
march = open("PBACH.txt")
lnp = []
lva = []
ctd = []
for n in range(4):
    lva.append(0)
for n in range(4):
    ctd.append(0)
for linea in march:
    linea = linea.rstrip()
    dato = linea.split(",")
    if dato[0] == "Fecha":
        for n in range(1,5):
            lnp.append(dato[n])
        continue
    if dato[0] >= "2020-09-23" and dato[0] <= "2021-01-08": #Perú
        lva[0] += int(dato[1])
        ctd[0] += 1
    if dato[0] >= "2020-07-18" and dato[0] <= "2020-12-05": #Bolivia
        lva[1] += int(dato[2])
        ctd[1] += 1
    if dato[0] >= "2020-04-25" and dato[0] <= "2020-08-17": #Argentina
        lva[2] += int(dato[3])
        ctd[2] += 1
    if dato[0] >= "2020-12-29" and dato[0] <= "2021-02-10": #Chile
        lva[3] += int(dato[4])
        ctd[3] += 1
for n in range(4):
    print("País:",lnp[n],"Total:",lva[n],"Promedio:",lva[n]/ctd[n])
march.close()
