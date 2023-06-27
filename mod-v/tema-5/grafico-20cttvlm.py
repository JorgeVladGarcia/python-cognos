import matplotlib.pyplot as plt
import numpy as np
import sqlite3

'''
OBJETIVO GENERAL:
Aplicación que utiliza los datos del archivo materiales de construcción del
Censo 2012, que permite escoger un municipio cualquiera y visualiza en forma
gráfica las cantidades de los tipos de techos de calamina, teja y losa que
tienen las viviendas de las localidades de ese municipio. La gráfica se ejecuta
con el paquete matplotlib, en el eje X están las localidades y en el eje Y las
cantidades de viviendas, además ajusta el tamaño de este eje a la cantidad
máxima de viviendas presentada. La aplicación está hecha en Python con
funciones y un programa principal, a este último se le proveé el nombre
del municipio que se desea consultar.
'''

def cargar_BD(arch_csv):
    '''
    OBJETIVO:
        Extraer los datos del archivo csv que contiene la información y de
        acuerdo al modelado de datos los graba en la base de datos SQLite a
        através del gestor Database Browser.
    ENTRADAS:
        arch_csv = Nombre del archivo csv donde están los datos
    SALIDA:
        Ninguna. Graba los datos normalizados en el Database Browser SQLite
    '''
    cur.executescript('''
        DROP TABLE IF EXISTS mat_constr;
        DROP TABLE IF EXISTS dpm;
        DROP INDEX IF EXISTS idx_munic;
        DROP INDEX IF EXISTS idx_local;
        
        CREATE TABLE dpm (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dpto       TEXT,
            provincia  TEXT,
            municipio  TEXT
    );
        CREATE TABLE mat_constr (
            dpm_id     INTEGER,
            localidad  TEXT,
            total_pared INTEGER,
            ladr_cem   INTEGER,
            adobe      INTEGER,
            tabique    INTEGER,
            piedra     INTEGER,
            madera_par INTEGER,
            caña       INTEGER,
            otro_pared INTEGER,
            total_techo INTEGER,
            calamina   INTEGER,
            teja       INTEGER,
            losa       INTEGER,
            paja       INTEGER,
            otro_techo INTEGER,
            total_piso INTEGER,
            tierra     INTEGER,
            madera_pis INTEGER,
            machimbre  INTEGER,
            parquet    INTEGER,
            ceramica   INTEGER,
            cemento    INTEGER,
            mosaico    INTEGER,
            ladrillo   INTEGER,
            otro_piso  INTEGER
    );
        CREATE INDEX idx_munic ON dpm(municipio);
        CREATE INDEX idx_local ON mat_constr(localidad);
    ''')
    march = open(arch_csv, encoding = "utf8")
    band = True
    nn = 0
    munic = ""
    for linea in march:
        linea = linea.rstrip()
        if band:
            lcab = linea.split(';')
            tam = len(lcab)
            band = False
        else:
            ltemp = linea.split(';')
            sbb = list()
            for nume in range(tam):
                sbb.append(str(ltemp[nume]))
            if munic != sbb[2]:
                munic = sbb[2]
                cur.execute('INSERT INTO dpm(dpto, provincia, municipio) VALUES (?, ?, ?)',
                    (sbb[0], sbb[1], munic))
                cur.execute('SELECT id FROM dpm WHERE municipio = ?', (munic, ))
                dpm_id = cur.fetchone()[0]
            cur.execute('''INSERT INTO mat_constr(dpm_id, localidad, total_pared,
                ladr_cem, adobe, tabique, piedra, madera_par, caña, otro_pared,
                total_techo, calamina, teja, losa, paja, otro_techo, total_piso,
                tierra, madera_pis, machimbre, parquet, ceramica, cemento, mosaico,
                ladrillo, otro_piso)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (dpm_id, sbb[3], sbb[4], sbb[5], sbb[6], sbb[7], sbb[8], sbb[9],
                sbb[10], sbb[11], sbb[12], sbb[13], sbb[14], sbb[15], sbb[16],
                sbb[17], sbb[18], sbb[19], sbb[20], sbb[21], sbb[22], sbb[23],
                sbb[24], sbb[25], sbb[26], sbb[27]))
            nn += 1
            if nn == 5000:
                conn.commit()
                nn = 0
    conn.commit()
    march.close()
    return

def extraer_datselec(nmuni):
    '''
    OBJETIVO:
        Extrae los datos del municipio requerido del Database Browser for
        SQLite y entrega un diccionario con los datos extraidos.
    ENTRADA
        Ninguna
    SALIDA:
        dic_extr = Diccionario con los datos extraidos de la BD
        localid  = Lista de los nombres de las localidades
    '''
    dic_extr = dict()
    nn = 0
    localid = []
    ttecho = ["calamina", "teja", "losa"]
    for n in range(3):
        dic_extr[ttecho[n]] = []
    cur.execute('SELECT * FROM dpm WHERE municipio = ? ', (nmuni, ))
    for fila in cur:
        idmuni = fila[0]
        cur.execute('SELECT "calamina", "teja", "losa", "localidad" FROM mat_constr WHERE abs(dpm_id) = ?',
            (idmuni, ))
        for tt in cur:
            if tt[3] != nmuni.upper():
                for x in range(3):
                    dic_extr[ttecho[x]].append(tt[x])
                localid.append(tt[3])
    max1 = max(dic_extr[ttecho[0]])
    max2 = max(dic_extr[ttecho[1]])
    if max1 >= max2: maxi = max1
    else: maxi = max2
    return(dic_extr, localid, maxi)

def graf_datos(dic_dag, dlocalid, nmuni, maxim):
    '''
    OBJETIVO:
        Graficar los datos que recibe con el paquete Matplotlib, en el eje X
        se tienen las localidades del municipio y en el eje Y las cantiades de
        cada tipo de techo extraido.
    ENTRADAS:
        dic_dag  = Diccioinario con los datos extraidos de la BD
        dlocalid = Lista de los nombres de las localidades del municipio
        nmuni    = Nombre del municipio requerido por el usuario
    SALIDA:
        Ninguna    (elabora y presenta la gráfica resultante)
    '''
    x = np.arange(len(dlocalid)) # etiqueta de las localizaciones
    ancho = 0.2                  # ancho de las barras
    multiplica = 0
    fig, ax = plt.subplots(layout='constrained')
    for tipotech, listcviv in dic_dag.items():
        desplaz = ancho * multiplica
        rects = ax.bar(x + desplaz, listcviv, ancho, label=tipotech)
        ax.bar_label(rects, padding=2, size=5)
        multiplica += 1.0
    # Añade texto a las etiquetas, titulo, ejes y otros
    ax.set_ylabel('Cant. de viviendas')
    titulo = 'Tipos de techo de las viviendas del municipio de ' + nmuni
    ax.set_title(titulo)
    ax.set_xticks(x + ancho, dlocalid, rotation=90, size=5)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, maxim+10)
    plt.show()
    return

'''
Programa principal
'''
ndmun = input("Dame el nombre del municipio? ")
conn = sqlite3.connect('MC_Bolivia.sqlite')
cur = conn.cursor()
# cargar_BD("Material_de_Construccion.csv")
dic_dreq, list_dl, dmax = extraer_datselec(ndmun)
cur.close()
graf_datos(dic_dreq, list_dl, ndmun, dmax)