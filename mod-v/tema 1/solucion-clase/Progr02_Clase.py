import sqlite3

class casos_covid19:
    ltupl = list()
    
    '''
    OBJETIVO:
    Extraer los datos de los casos comprobados diarios Covid-19, cargados en la
    base de datos SQLite (navegador BD Browser), del país y período solicitado.
    
    ENTRADAS:
        - Pais, territorio o región a buscar
        - Fecha inicial del período
        - Fecha final del período
        No afecta ninguna de las entradas
    
    SALIDA:
        - Entrega los datos extraidos de la base de datos en una lista de tuplas.
          Cada tupla tiene la fecha y el dato de casos diario Covid19
    '''
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
                    self.ltupl.append((fc19[1], fc19[2]))
            cur.close()
        return(self.ltupl)
    
    '''
    OBJETIVO:
    Calcular, obtener e imprimir el total de casos Covid19, el promedio diario
    del período, el día y su valor de la menor y la mayor cantidad de casos
    presentados en el período.
    
    ENTRADAS:
        - Pais, territorio o región a buscar
        - Lista de tuplas de los datos
        No afecta ninguna de las entradas
    
    SALIDA:
        - Entrega el total de los casos Covid19 del período.
    '''
    def tot_prom_men_may(self, pais, ltdatos):
        self.ltupl = ltdatos
        tot = 0
        menor = mayor = None
        cant = len(self.ltupl)
        for nn in range(cant):
            fecha, dato = self.ltupl[nn]
            tot = tot + dato
            if menor == None or menor > dato:
                menor = dato
                dmen = fecha
            if mayor == None or mayor < dato:
                mayor = dato
                dmay = fecha
        fech_ini, dato = self.ltupl[0]
        fech_fin, dato = self.ltupl[-1]
        print("El total de casos de", pais, "del", fech_ini, "al", fech_fin, "es:", tot)
        print("Promedio diario de casos:", tot/cant)
        print(dmen, "fue el día que se presentó el menor caso:", menor)
        print(dmay, "fue el día que se presentó el mayor caso:", mayor)
        return(tot)
    
    '''
    OBJETIVO:
    Calcular, obtener e imprimir las listas de cuales fueron los días y sus
    valores que quedan tanto abajo como arriba del promedio diario. 
    
    ENTRADAS:
        - Lista de tuplas de los datos
        - Total de casos Covid-19 del período
        No afecta ninguna de las entradas
    
    SALIDA:
        No entrega nada.
    '''
    def abajo_arriba(self, ltdatos, tot):
        self.ltupl = ltdatos
        cant = len(self.ltupl)
        print("Día y valor abajo del promedio diario")
        for nn in range(cant):
            fecha, dato = self.ltupl[nn]
            if dato < tot/cant:
                print(fecha, dato)
        print("Día y valor arriba del promedio diario")
        for nn in range(cant):
            fecha, dato = self.ltupl[nn]
            if dato > tot/cant:
                print(fecha, dato)
        return()
