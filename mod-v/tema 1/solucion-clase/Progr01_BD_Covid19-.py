import sqlite3
import urllib.request

'''
OBJETIVO GENERAL:
Programa que crea la estructura de la Base de Datos SQLite en el navegador
DB Browser de acuerdo al modelo entidad-relación normalizado y realizado para
cargar la información Covid-19 de la OMS a nivel mundial desde su aparición
oficial hasta la fecha.

Para tal efecto, crea la estructura de datos respectiva, descarga la
información del sitio web de la OMS y la transfiere al navegador DB Browser
de acuerdo al modelo entidad-relación desarrollado para tal efecto.

Identifica y corrije el nombre extraño del territorio:
            "occupied Palestinian territory, including east Jerusalem"
quita las comillas inicial y final y la coma del medio
.
.
.
'''


conn = sqlite3.connect('Covid19.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Covid_datos;
DROP TABLE IF EXISTS Pais;
DROP INDEX IF EXISTS idx_pais;
DROP INDEX IF EXISTS idx_fecha;

CREATE TABLE Pais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pais_nomb   TEXT UNIQUE,
    pais_code   TEXT,
    region_who  TEXT
);

CREATE TABLE Covid_datos (
    pais_id  INTEGER,
    fecha    TEXT,
    new_cc   INTEGER,
    acum_cc  INTEGER,
    new_m    INTEGER,
    acum_m   INTEGER
);

CREATE INDEX idx_pais ON Pais(pais_nomb);
CREATE INDEX idx_fecha ON Covid_datos(fecha, abs(pais_id))
''')

fhand = urllib.request.urlopen("https://covid19.who.int/WHO-COVID-19-global-data.csv")

band = True
nn = 0
pais = ""
row = dict()
for lix in fhand:
    csvf = lix.decode().strip()
    if band:
        lcab = csvf.split(',')
        tam = len(lcab)
        band = False
    else:
        if csvf[14] == '"':
            '''     Identifica y corrije el nombre extraño del territorio:
            "occupied Palestinian territory, including east Jerusalem"
            quita las comillas inicial y final y la coma del medio    '''
            ncsvf = csvf[:14] + csvf[15:45] + csvf[46:71] + csvf[72:]
            csvf = ncsvf
        ltemp = csvf.split(',')
        for nume in range(tam):
            row[str(lcab[nume])] = str(ltemp[nume])
        fech = row['\ufeffDate_reported']   # Nombre de la primer columna
        if pais != row['Country']:
            pais = row['Country']           # Pais es la tercer columa
            cur.execute('''INSERT OR IGNORE INTO Pais (pais_nomb, pais_code, region_who)
                VALUES (?, ?, ?)''', (pais, row['Country_code'], row['WHO_region']))
            cur.execute('SELECT id FROM Pais WHERE pais_nomb = ? ', (pais, ))
            pais_id = cur.fetchone()[0]
        cur.execute('''INSERT OR IGNORE INTO Covid_datos (pais_id, fecha,
            new_cc, acum_cc, new_m, acum_m) VALUES ( ?, ?, ?, ?, ?, ? )''',
            (pais_id, fech, row['New_cases'], row['Cumulative_cases'],
            row['New_deaths'], row['Cumulative_deaths']))
        nn = nn + 1
        if nn == 100000:
            conn.commit()
            nn = 0
conn.commit()
print('Terminamos...')
cur.close()