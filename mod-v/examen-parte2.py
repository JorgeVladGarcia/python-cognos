'''
➢ Elaborar un segundo programa Python que deberá tener 3 funciones y un programa principal. 

La primer
función permitirá extraer los datos Covid-19 cargados en el navegador BD Browser con el primer programa. La función debe recibir el país, la fecha inicial y la fecha final y deberá entregar un diccionario con las fechas y datos diarios Covid-19 presentados durante el período indicado.
'''
import sqlite3
from datetime import date   # revisar documentación de date

conn = sqlite3.connect('covid19_mundial.sqlite')
cur = conn.cursor()

# Extrae los datos Covid-19 cargados en el navegador BD Browser correspondientes
# al país y período solicitado. Entrega los datos extraidos en un diccionario.
def extrae_CC(pais, fech_ini, fech_fin):
    print("\nDatos", pais, "al periodo", fech_ini, "a", fech_fin)
    cur.execute('select * from country where country = ?', (pais,))
    # identificar llave primaria
    for linea in cur:
        idctry = linea[0]
        ctry = linea[2]
        cur.execute('select * from covid_info where country_id = ? and date_reported >= ? and date_reported <= ?', (idctry, fech_ini, fech_fin, ))
        # retornar todos los valores
        for valor in cur:
            print(ctry, valor[1:5])
            # para tarea: self.ltupl.append()
    return()
    # para tarea:return(self.ltupl)

# Imprime el total de casos Covid19, el promedio diario, el día y su valor del
# menor y mayor de los casos presentados en el período indicado.
def tot_prom_men_may(pais, fech_ini, fech_fin):
    # crear variables
    d_sublist = []
    sum = 0
    cnt = 0
    min = None 
    max = None  
    cur.execute('select * from country where country = ?', (pais,))
    #print("\nEn el periodo", fech_ini, "a", fech_fin, "en", pais)
    for linea in cur: 
        idctry = linea[0]
        ctry = linea[2]
        # hallar total de casos en el periodo 
        cur.execute('''select * from covid_info where country_id = ? and date_reported >= ? and date_reported <= ?''', (idctry, fech_ini, fech_fin)) 
        for valor in cur:
            d_sublist.append(valor)
    # hallar promedio             
    for i in d_sublist:
        cnt += 1
        sum += i[2]
        # hallar valor menor
        if min == None or i[2] < min:
            min = i[2]
            min_date = i[1]
        # hallar valor mayor 
        if max == None or i[2] > max:
            max = i[2]
            max_date = i[1]        
    print("\n- Total nuevos casos covid19:", sum)
    print("- Promedio diario al periodo:", round(sum/cnt, 2))
    print("- Día con menores casos reportados es:", min_date, "con", min, "registros")    
    print("- Día con más casos reportados es:", max_date, "con", max, "registros")
    return()

# Imprime los días y valores que quedaron abajo y arriba del promedio diario
def abajo_arriba(pais, fech_ini, fech_fin):
    # crear variables
    d_sublist = []
    sum = 0
    cnt = 0
    min = None 
    max = None 
    cur.execute('select * from country where country = ?', (pais,))
    #print("\nEn el periodo", fech_ini, "a", fech_fin, "en", pais)
    for linea in cur: 
        idctry = linea[0]
        ctry = linea[2]
        # hallar total de casos en el periodo 
        cur.execute('''select * from covid_info where country_id = ? and date_reported >= ? and date_reported <= ?''', (idctry, fech_ini, fech_fin)) 
        for valor in cur:
            d_sublist.append(valor)
    lista_val = []
    lista_fech = []
    # hallar promedio             
    for i in d_sublist:
        cnt += 1
        sum += i[2]
        # hallar valor menor
        if min == None or i[2] < min:
            min = i[2]
            min_date = i[1]
        # hallar valor mayor 
        if max == None or i[2] > max:
            max = i[2]
            max_date = i[1]        
        # hallar indices en lista con valores
        lista_val.append(i[2])
        # hallar valores de fechas
        lista_fech.append(i[1])
    avg = round(sum/cnt, 2)
    print("\nLos días y valores que están por encima del promedio son:")
    for n in range(len(lista_val)):
        if lista_val[n] > avg:
            print("-", lista_fech[n], "con", lista_val[n], "casos reportados")
    print("\nLos días y valores que están por debajo del promedio son:")
    for n in range(len(lista_val)):
        if lista_val[n] < avg:
            print("-", lista_fech[n], "con", lista_val[n], "casos reportados")
    return()

try:
    pais = input("Deme el pais: ")
    fecha_ini = input("Deme la fecha inicial: ")
    fecha_fin = input("Deme la fecha final: ")

    extrae_CC(pais, fecha_ini, fecha_fin)
    tot_prom_men_may(pais, fecha_ini, fecha_fin)
    abajo_arriba(pais, fecha_ini, fecha_fin)
except:
    print("Los valores son inválidos")