from datetime import date
import sqlite3

class casos_covid19:
    dict19 = dict()
    
# Extrae los datos Covid-19 cargados en el navegador BD Browser correspondientes
# al país y período solicitado. Entrega los datos extraidos en un diccionario.
    def extrae_CC(self, pais, fech_ini, fech_fin):
        if fech_fin < fech_ini:
            print("La fecha final es menor que la fecha inicial...")
        else:
            conn = sqlite3.connect('Covid19.sqlite')
            cur = conn.cursor()
            cur.execute('SELECT * FROM Pais WHERE pais_nomb = ? ', (pais, ))
            for fila in cur:
                idpais = fila[0]
                cur.execute('SELECT * FROM Covid_datos WHERE abs(pais_id) = ? AND fecha >= ? AND fecha <= ?',
                    (idpais, fech_ini, fech_fin, ))
                for fc19 in cur:
                    self.dict19[fc19[1]] = fc19[2]
            cur.close()
        return(self.dict19)

# Imprime el total de casos Covid19, el promedio diario, el día y su valor del
# menor y mayor de los casos presentados en el período indicado.
    def tot_prom_men_may(self, pais, fech_ini, fech_fin, ddatos):
        self.dict19 = ddatos
#        f_ini_ord = fech_ini.toordinal()
        tot = 0
        menor = mayor = None
        cant = len(self.dict19)
#        for n in range(cant):
        for clave, valor in list(self.dict19.items()):
#            ndia = date.fromordinal(f_ini_ord + n)
#            dato = self.dict19[str(ndia)]
            dato = int(valor)
            tot = tot + dato
            if menor == None or menor > dato:
                menor = dato
                dmen = str(clave)
#                dmen = ndia
            if mayor == None or mayor < dato:
                mayor = dato
                dmay = str(clave)
#                dmay = ndia
        print("El total de casos de", pais, "del", fech_ini, "al", fech_fin, "es:", tot)
        print("Promedio diario de casos:", tot/cant)
        print(dmen, "fue el día que se presentó el menor caso:", menor)
        print(dmay, "fue el día que se presentó el mayor caso:", mayor)
        return(tot)

# Imprime los días y valores que quedaron abajo y arriba del promedio diario
    def abajo_arriba(self, fech_ini, ddatos, tot):
        self.dict19 = ddatos
#        f_ini_ord = fech_ini.toordinal()
        cant = len(self.dict19)
        print("Día y valor abajo del promedio diario")
        for clave, valor in list(self.dict19.items()):
#        for n in range(cant):
#            ndia = date.fromordinal(f_ini_ord + n)
#            dato = self.dict19[str(ndia)]
            dato = int(valor)
            if dato < tot/cant:
                print(str(clave), dato)
#                print(ndia, dato)
        print("Día y valor arriba del promedio diario")
        for clave, valor in list(self.dict19.items()):
#        for n in range(cant):
#            ndia = date.fromordinal(f_ini_ord + n)
#            dato = self.dict19[str(ndia)]
            dato = int(valor)
            if dato > tot/cant:
                print(str(clave), dato)
#                print(ndia, dato)
        return()
