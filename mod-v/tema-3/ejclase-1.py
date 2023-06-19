# working graph

"""
Aplicación para graficar los datos del Producto Interno Bruto (PIB) de paises seleccionados.
Los datos de todos los paises se encuentran en un archivo CSV.
La gráfica se creará con el paquete pygal y será del tipo XY.
"""

import pygal

def lectura_datos_totales(dat_csv, camp_clav, separador, quote):
    """
    Objetivo:
      Leer los datos totales que vienen en el archivo, acomodarlos y entregarlos en un diccionario
      
    Entradas:
      dat_csv   - Nombre del archivo CSV donde están los datos PIB
      camp_clav - Nombre del campo clave para usarlo con los renglones
      separator - Caracter que sirve como separador de los campos
      quote     - Caracter opcional para marcar las cadenas de texto

    Salida:
      Regresa un diccionario de diccionarios donde el diccionario externo mapea el valor en el campo clave al correspondiente renglón del archivo. Los diccionarios internos mapean a los nombres de los campos a los valores de campo para cada renglón. {"Aruba": {1990: 123.45, 1991: 876.29, ...}, "AFE": {1990: 345.89....}...}
    """
    dicddics = dict()
    band = True

    # leer csv 
    march = open(dat_csv, encoding="utf8")
    for linea in march:
        # eliminar retorno de carro 
        linea = linea.rstrip()
        # leer la primera linea
        if band:
            # almacenar información en la cabecera 
            lcab = linea.split(separador)
            # almacenar longitud del csv 
            tam = len(lcab)
            # saltar a segunda linea, ignorar cabecera 
            band = False
        else:
            # crear diccionario interno
            dicint = dict()
            # almacenar info csv menos cabecera 
            ldat = linea.split(separador)
            # loop para agarrar datos del csv  y guardarlos en dic interno
            for n in range(34, tam-1):
                dicint[lcab[n]] = ldat[n]
            # unir diccionario interno y externo
            dicddics[ldat[camp_clav]] = dicint
    #print(dicddics)
    return dicddics


def recupera_un_elemento(dcomplem, dun_pais):
    """
    Objetivo:
      Recuperar un elemento del diccionario de diccionarios (datos del PIB) y acomodarlo en el modo requerido para ser  graficado luego
      
    Entradas:
      dcomplem  - Diccionario de datos complementarios, rango de fechas a ser graficadas, nombre del pais y otros
      dun_pais - Diccionario de los datos PIB de un pais

    Salida: 
      Regresa una lista de tuplas de la forma (año, PIB) del pais indicado, para los años que se encuentran en el rango seleccionado (del min_year al max_year inclusive) que se indican en el diccionario de datos complementarios. El año es entero y el PIB un número de punto flotante
    """
    # crear lista 
    ltu_pais = list()
    # leer min year de diccionario complemento 
    amin = dcomplem["min_year"]
    # leer mmx yer de diccionario complement
    amax = dcomplem["max_year"]

    # 
    for clave, valor in list(dun_pais.items()):
        anio = int(clave)
        pib = valor.replace(",", ".")
        if anio >= amin and anio <= amax:
            if valor == "":
                ltu_pais.append((anio, 0))
            else:
                ltu_pais.append((anio, float(pib)))
    #print(ltu_pais)
    return ltu_pais


def recupera_elem_selec(datos_pib, dcomplem, list_paises):
    """
    Objetivo:
      Recuperar todos los datos del PIB de la lista de paises requeridos y entregarlos en un diccionario con el formato  adecuado para ser graficados posteriormente
      
    Entradas:
      datos_pib   - Diccionario de los datos totales del PIB que entrega la función lectura_datos_totales()
      dcomplem    - Diccionario de datos complementarios, rango de fechas a ser graficadas, nombre del pais y parámetros para leer el archivo total
      list_paises - Lista de los nombres de paises requeridos a ser graficados

    Salida:
      Regresa un diccionario donde la clave es el pais de la lista de paises requeridos y el valor es la lista de pares de valores de la gráfica XY (X = año, Y = PIB) de dicho pais.

      Los paises requeridos que no aparecen en el archivo CSV original, estarán en el diccionario de  graficación pero con una lista vacia para la gráfica XY. {"Bolivia": [(1990, 987.98), (1991, 987.23), .....]}
    """
    # crear diccionario vacío 
    dic_graf = dict()
    for ctry in list_paises:
        dunpais = datos_pib[ctry]
        dic_graf[ctry] = recupera_un_elemento(dcomplem, dunpais)
    #print(dic_graf)
    return dic_graf


def crea_grafica_xy(dic_graf, list_paises , arch_graf):
    """
    Objetivo:
      Crea una imagen SVG con el paquete pygal de una gráfica tipo XY correspondiente a datos del PIB de los paises requeridos en la lista list_paises. La imagen será almacenada en el archivo indicado en  arch_graf.
      
    Entradas:
      dic_graf    - Diccionario con los datos del PIB de los paises requeridos en la lista respectiva
      list_paises - Lista de los nombres de paises requeridos a ser graficados
      arch_graf   - Nombre del archivo donde quedará almacenada la imagen SVG creada por el paquete pygal

    Salida:
      No regresa nada.
    """
    xyplot = pygal.XY(heigh=400)

    title = ""
    for i in lpaises:
        title += i + " "
    xyplot.title = "PIB: " + str(title)
    #print(dic_graf)

    for ctry, pibyear in list(dic_graf.items()):
      xyplot.add(ctry, pibyear)
      xyplot.render_to_file(arch_graf)
    return

"""
variables para programa final
""" 

# diccionario complementario 
dic_complem = {
    "arch_pib": "Datos_PIB.csv",    # Nombre del archivo CSV con datos PIB
    "separator": ";",               # Caracter separator de datos
    "quote": '"',                   # Caracter indicador de cadena
    "min_year": 1990,               # Año más viejo 
    "max_year": 2021,               # Año más nuevo
    "nombre_pais": "Bolivia",       # Nombre del pais
    "codigo_pais": "BOL"            # Código del pais
}

# lista de paises 
lpaises = ["Bolivia", "Paraguay", "Ecuador", "Chile", "Perú", "Colombia"]

# llamar funciones 
datos_tot = lectura_datos_totales('Datos_PIB.csv', 0, ';', '"')
datos_selec = recupera_elem_selec(datos_tot, dic_complem, lpaises)
crea_grafica_xy(datos_selec, lpaises, "graf_xy_pib.svg")