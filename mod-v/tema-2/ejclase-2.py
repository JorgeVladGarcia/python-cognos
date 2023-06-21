import pygal 

xyplot = pygal.XY()
xyplot.title = "Uso del piso de cemento en las viviendas del municipios de Cotoca"

march = open("Material_de_Construccion.csv", encoding = "utf8")

band = True #para primer renglon de las columnas
piso = dict() # crear diccionario 


# crear for para cargar todos los valores de scz cotoca en el diccionario piso
for linea in march:
    linea = linea.rstrip() # remover retorno de varro
    #print(linea)
    if band:
        band = False # para remover el primer renglon, se salta la primera linea
    else:
        ltemp = linea.split(',') # lista de valores de todas las columnas del primer renglon 
        if ltemp[0] == "Santa Cruz" and ltemp[2] == "Cotoca":
            piso[ltemp[3]] = int(ltemp[24]) # guardar el nombre de la localidad con la columna de los pisos de cemento , diccionario guarda info

print(piso)
# iniciar nuevo loop
n = 1 
for clave, valor in list(piso.items()): # enviar valores del diccionario a las variables clave y valor 
    if clave != "COTOCA":
        xyplot.add(clave, [(n, valor)])
    n += 1

xyplot.render_to_file('draft3.svg')    
