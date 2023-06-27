import matplotlib.pyplot as plt

march = open("Material_de_Construccion.csv", encoding = 'utf-8')
band = True
piso = dict()
for linea in march:
    linea = linea.rstrip()
    if band:
        band = False
    else:
        ltemp = linea.split(';')
        if ltemp[0] == "Santa Cruz" and ltemp[2] == "Cotoca":
            piso[ltemp[3]] = int(ltemp[24])
n = cant = 1
fig, ax = plt.subplots()
# punto = ['r^']
punto = ['r^','b^','g^','rs','bs','gs']
for clave, valor in list(piso.items()):
    if clave != "COTOCA":
        cnum = str(n) + ". " + clave
        plt.plot(n, valor, punto[n-1], label=cnum)
        n += 1
        if cant == 6:
            break
        cant += 1
ax.set(xlabel='Localidades numéricas', ylabel='Cantidad de viviendas',
       title='Viviendas con piso de cemento del municipio de Cotoca')
ax.legend(title='Localidad de Cotoca')
plt.grid()
plt.show()