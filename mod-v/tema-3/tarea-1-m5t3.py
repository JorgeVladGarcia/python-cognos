'''
Utilizando la información del censo 2012 referente a los Materiales de
Construcción dibujar un gráfico con los datos de los tipos de techos de
las localidades del municipio de Porongo. Deben graficarse curvas de
calamina, teja, loza, paja y otro techo. La grafica debe ser producida en
forma automática por un programa Python, para esto se debe utilizar
los datos del archivo Material_de_construcción.csv, preparar los datos
seleccionados y finalmente graficar los datos utilizando el paquete
pygal en formato tipo Line.


{Calamina: 49, Teja: 748, Loza: , Paja:, Otro:}

GOOD ENOUGH DRAFT
'''

march = open("Material_de_Construccion.csv", encoding = "utf8")

calamina = []
teja = []
losa = []
paja = []
otro  = []

cnt = 1
# crear for para cargar todos los valores de scz cotoca en el diccionario piso
for linea in march:
    linea = linea.rstrip() # remover retorno de varro
    linea = linea.split(',')
    if linea[0] == "Santa Cruz" and linea[2] == "Porongo":
        if int(linea[14]) < 700: 
            calamina.append((cnt, int(linea[13])))
            teja.append((cnt, int(linea[14])))        
            losa.append((cnt, int(linea[15])))
            paja.append((cnt, int(linea[16])))
            otro.append((cnt, int(linea[17])))
            # agregar lista de localidades
            # localid.append()
            cnt += 1



import pygal 
xyplot = pygal.XY()
# utilizar opcion de linease no XY 
# linplot = pygal.Line() # para definir tipo de grafica line


xyplot.title = "Techos de viviendas de las localidades del municipio de Porongo"

# agregar linplot.x_labels = localid
xyplot.add("Calamina", calamina)
xyplot.add("Teja", teja)
xyplot.add("Losa", losa)
xyplot.add("Paja", paja)
xyplot.add("Otro", otro)

xyplot.render_to_file('draft3.svg')    