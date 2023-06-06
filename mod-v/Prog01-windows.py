'''
➢ Elaborar un primer programa Python que descargue la información del sitio web de la OMS al navegador
BD Browser de SQLite de acuerdo al modelo entidad-relación realizado.
https://covid19.who.int/WHO-COVID-19-global-data.csv
'''

import urllib.request
import sqlite3

# abrir documento
outf = open("Covid19-mundial.csv", "w")
fhand = urllib.request.urlopen("https://covid19.who.int/WHO-COVID-19-global-data.csv")

#exportar csv 
for i in fhand:
    i = i.strip().decode()
    i = i.replace('"occupied Palestinian territory, including east Jerusalem"', 'occupied Palestinian territory including east Jerusalem')
    outf.write(str(i.encode("utf-8")) + '\n')
outf.close()

# abrir conexion
conn = sqlite3.connect('covid19_mundial.sqlite')
cur = conn.cursor()

# ejecutar script
cur.executescript('''
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS covid_info;
DROP INDEX IF EXISTS idx_country;
DROP INDEX IF EXISTS idx_date;

CREATE TABLE country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code       TEXT,
    country            TEXT,
    who_region         TEXT
);

CREATE TABLE covid_info (
    country_id          INTEGER,
    date_reported       TEXT,
    new_cases           INTEGER,
    cumulative_cases    INTEGER,
    new_deaths          INTEGER,
    cumulative_deaths   INTEGER
);

CREATE INDEX idx_country ON country(country);
CREATE INDEX idx_date ON covid_info(date_reported);
'''
)
# on sql above, add abs(country_id)

# abrir archivo CSV 
march = open("WHO-COVID-19-global-data.csv", encoding = "utf-8-sig")

# abrir bandera
band = True
# nn sirve para hacer los commits 
# guardar registros por cada mil registros 
nn = 0
country = ""
for linea in march:
    linea = linea.rstrip()
    if band:
        # guardar informacion del listado
        lcab = linea.split(',')
        tam = len(lcab)
        # cambiar bandera a falso para guardar primera fila en enxavezados
        # guarda datos del cabezal
        #print(lcab)
        band = False
    else:
        ltemp = linea.split(',')
        # lista comienza en 0 y se ejecuta, la volvemos a inicializar y continua llenandose
        sbb = list()
        for nume in range(tam):
            sbb.append(str(ltemp[nume]))
        if country != sbb[2]:
            country = sbb[2]
            cur.execute('INSERT INTO country(country_code, country, who_region) VALUES (?, ?, ?)', (sbb[1], country, sbb[3]))
            # seleccionando info del pais
            cur.execute('select id from country where country = ?', (country, ))
            # identificar la llave foranea
            country_id = cur.fetchone()[0]
        # insertar informacion del covid
        cur.execute('''INSERT INTO covid_info(country_id, date_reported, new_cases, cumulative_cases, new_deaths, cumulative_deaths) VALUES (?, ?, ?, ?, ?, ?)''', (country_id, sbb[0], sbb[4], sbb[5], sbb[6], sbb[7]))
        nn += 1
        if nn == 1000:
            conn.commit()
            nn = 0

conn.commit()
print('Done')            
cur.close()
march.close()