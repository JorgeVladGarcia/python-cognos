'''
Sistema de servicios 
Realizar otro programa utilizando las claves lógicas respectivas para mostrar los datos de un municipio y
de un tipo de servicio. Para esto se debe pedir por pantalla el nombre del municipio y el tipo de servicio.
'''
import sqlite3

conn = sqlite3.connect("SB_Bolivia.sqlite")
cur = conn.cursor()
munic = input("Dame el municipio: ")
tserv = input("Dame el tipo de servicio (A D E): ")
# ejecutar query con info del munnicipio
cur.execute('SELECT * FROM dpm WHERE municipio = ?', (munic,))
if tserv == "A":
    for linea in cur:
        # identificar llave primaria
        iddpm = linea[0]
        # municipio es el tercer valor 
        muni = linea[3]
        cur.execute('SELECT localidad, total_agua, red FROM serv_basicos WHERE dpm_id = ?',
            (iddpm,))
        for valor in cur:
            print(muni, valor[0], valor[1], valor[2])
elif tserv == "D":
    for linea in cur:
        iddpm = linea[0]
        muni = linea[3]
        cur.execute('SELECT localidad, tot_desagu, alcantaril FROM serv_basicos WHERE dpm_id = ?',
            (iddpm,))
        for valor in cur:
            print(muni, valor[0], valor[1], valor[2])
elif tserv == "E":
    for linea in cur:
        iddpm = linea[0]
        muni = linea[3]
        cur.execute('SELECT localidad, tot_electr, red_electr FROM serv_basicos WHERE dpm_id = ?',
            (iddpm,))
        for valor in cur:
            print(muni, valor[0], valor[1], valor[2], round(valor[2]*100/valor[1], 2))
else:
    print("Mal la inicial del servicio....")
print("Terminamos")
cur.close()
