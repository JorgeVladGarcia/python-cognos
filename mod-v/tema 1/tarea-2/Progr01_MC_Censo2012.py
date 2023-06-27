'''
Progr01_MC_Censo2012 – Elaborar un programa para transferir la información de los materiales de
construcción del censo 2012 del país al navegador de Base de Datos SQLite de acuerdo al modelo
entidad-relación realizado.
'''


import sqlite3

# abrir conexcion
conn = sqlite3.connect('SB_Bolivia.sqlite')
# definir cursor 
cur = conn.cursor()

# ejecutar script
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
    techo_teja INTEGER
);

CREATE INDEX idx_munic ON dpm(municipio);
CREATE INDEX idx_local ON mat_constr(localidad);
''')

# abrir archivo CSV 
march = open("Material-Construccion-csv.csv", encoding = "utf8")

# abrir bandera
band = True
# nn sirve para hacer los commits 
# guardar registros por cada mil registros 
nn = 0
munic = ""
for linea in march:
    linea = linea.rstrip()
    if band:
        # guardar informacion del listado
        lcab = linea.split(',')
        tam = len(lcab)
        # cambiar bandera a falso para guardar primera fila en enxavezados
        # guarda datos del cabezal
        band = False
    else:
        ltemp = linea.split(',')
        # lista comienza en 0 y se ejecuta, la volvemos a inicializar y continua llenandose
        sbb = list()
        for nume in range(tam):
            sbb.append(str(ltemp[nume]))
        # utilizamos info del municipio porque es info distinta
        # queremos que municipio sea PK
        # iterar sobre informacion del munic
        # tiene que aparecer un solo municipio como id
        # si munic es distinto a 2 actualizaco mi municipio 
        if munic != sbb[2]:
            munic = sbb[2]
            # inserto datos a tabla
            cur.execute('INSERT INTO dpm(dpto, provincia, municipio) VALUES (?, ?, ?)',
                (sbb[0], sbb[1], munic))
            # seleccionando info de muniicpio
            cur.execute('SELECT id FROM dpm WHERE municipio = ?', (munic, ))
            # iteracion termina y volvemos a comenzar
            # fetchone identifica la llave foranea 
            dpm_id = cur.fetchone()[0]
        # ahora se empieza a insertar todos los hombres 
        cur.execute('''INSERT INTO mat_constr(dpm_id, localidad, techo_teja)
            VALUES (?,?,?)''',
            (dpm_id, sbb[3], sbb[4]))
        # hacemos que commit se haga de mil en mil
        nn += 1
        # si nn llega a mil ejecuta el commit y lo pone en 0
        if nn == 1000:
            conn.commit()
            nn = 0
# commit graba la info en la DB            
conn.commit()
print('Terminamos...')
cur.close()
march.close()