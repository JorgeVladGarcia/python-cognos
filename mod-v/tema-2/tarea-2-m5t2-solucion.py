'''
Utilizando la información de los materiales de construcción del Censo 2012 dibujar
un gráfico con los datos de los techos de teja de las viviendas del total de cada
departamento. La grafica debe ser producida en forma automática por un
programa Python, el mismo que debe leer los datos del archivo Material de
Construcción.csv, extraer los datos de la columna techos de teja y el total de cada
departamento, preparar los datos para utilizarlos con pygal y conformar el gráfico
donde se tenga la lista de departamentos del país y la gráfica de puntos
'''

import pygal 

march = open("Material-Construccion-3.csv", encoding = "utf8")
list_dept = []

for linea in march:
    linea = linea.rstrip()
    linea = linea.split(',')
    # Identificar valores departamentos, donde dice "Total"
    if linea[1] == "Total":
        value = int(linea[4])
        # guardar valores en una lista 
        list_dept.append(value)

chart = pygal.Line(stroke = False)
chart.add('data', list_dept)
chart.render_to_file('tarea-2.svg')