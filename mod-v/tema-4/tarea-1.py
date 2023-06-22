import sqlite3

'''
OBJETIVO GENERAL:
Programa que extrae en forma selectiva datos de los casos diarios comprobados
de Covid y muertes de los datos de la OMS que se encuentran en el gestor
Database Browser for SQLite. Los datos requeridos son del pais y del rango
entre las fechas fech_ini y fech_fin.
'''


def extrae_1pais(pais,fech_i, fech_f):
    '''
    OBJETIVO:
        Extraer los datos covid de un pais del gestor Database Browser
        for SQLite de acuerdo con los parámetros de entrada.
    ENTRADAS:
        pais   = Nombre del pais requerido
        fech_i = Fecha inicial del rango a extraer
        fech_f = Fecha final del rango
    SALIDA:
        Imprime los datos del pais y rango requerido
    '''
    conn = sqlite3.connect('covid19_mundial.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM DCC WHERE Country = ?' , (pais,))             
    for fila in cur:
        DCC_id = fila[0]
        cur.execute('SELECT * FROM Tabla_casos WHERE abs(DCC_id) = ? AND Date_reported >= ? AND Date_reported <= ?', (DCC_id,fech_i,fech_f, ))
        for fc19 in cur:
            print ("Fecha:",fc19[1]," Pais:",pais," Casos nuevos:",fc19[2]," Casos muertes:",fc19[4])
    return

    
def extrae_dcovid(lpaises, fech_ini, fech_fin):
    '''
    OBJETIVO:
        Extraer los datos covid de los paises requeridos que están en el
        gestor Database Browser for SQLite de acuerdo con los parámetros
        de entrada.
    ENTRADAS:
        lpaises  = Lista de paises requerida
        fech_ini = Fecha inicial del rango a extraer
        fech_fin = Fecha final del rango
    SALIDA:
        Ninguna
    '''
    conn = sqlite3.connect('Covid_1.sqlite')
    cur = conn.cursor()
    for i in range (len(lpaises)):
        cur.execute('SELECT * FROM DCC WHERE Country = ?' , (lpaises[i],))             
        for fila in cur:
            DCC_id = fila[0]
            cur.execute('SELECT * FROM Tabla_casos WHERE abs(DCC_id) = ? and Date_reported >= ? and Date_reported <= ?',
                        (DCC_id,fech_ini,fech_fin, ))
            for fc19 in cur:
                print ("Fecha:",fc19[1]," Pais:",lpaises[i]," Casos nuevos:",fc19[2]," Casos muertes:",fc19[4])
            print("")
    return

'''
Programa principal
'''

conn = sqlite3.connect('covid19_mundial.sqlite')
cur = conn.cursor()

lista_p = ["Argentina", "Mexico", "Peru", "Chile", "Colombia"]
extrae_dcovid(lista_p, "2021-09-25", "2021-10-04")

cur.close()
print('Terminamos...')