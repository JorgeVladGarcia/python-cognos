'''
Progr02_Clase - Elaborar un programa tipo clase que tendrá 3 módulos.

▪ El primer módulo permitirá extraer los datos de las tejas de los materiales de construcción del censo
2012 cargados en la base de datos SQLite (BD Browser). El módulo debe recibir el departamento y el
municipio y deberá entregar una lista de tuplas (localidad y cantidad de viviendas con teja).

▪ El segundo módulo deberá calcular y mostrar en pantalla 
    - el total de viviendas con teja del municipio y departamento, 
    - el promedio de viviendas de las localidades, 
    - la localidad 
    - y la cantidad tanto menor como mayor de viviendas del municipio y departamento indicado. 

El módulo debe recibir el departamento, municipio y la lista de tuplas (localidad y cantidad de viviendas con teja).

▪ El tercer módulo deberá calcular y mostrar en pantalla las listas de localidades y cantidad de viviendas
con teja que quedan tanto abajo como arriba del promedio de viviendas. El módulo debe recibir la lista
de tuplas de localidad y cantidad de viviendas con teja. No entregará nada.
'''

import sqlite3

class mat_const:
    dict_mat_const = dict()

    def mod_i(self, dept, munic):
        conn = sqlite3.connect('SB_Bolivia.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM dpm WHERE municipio = ?', (munic,))
        for linea in cur:
            idpm = linea[0]
            muni = linea[3]
            cur.execute('SELECT * FROM mat_constr WHERE dpm_id = ?', (idpm,))
            for value in cur:
                self.dict_mat_const[value[1]] = value[2]
        cur.close()
        return(self.dict_mat_const)

    def mod_ii(self, dept, ddatos):
        self.dict_mat_const = ddatos
        tot = 0
        menor = mayor = None
        cant = len(self.dict_mat_const)
        for clave, valor in list(self.dict_mat_const.items()):
            dato = int(valor)
            tot = tot + dato
            if menor == None or menor > dato:
                menor = dato
                mun_men = str(clave)
            if mayor == None or mayor < dato:
                mayor = dato 
                mun_may = str(clave)
        print("\ntotal hogares con techo de teja en" , dept, "es", tot)
        print("promedio hogares con techo de teja:", round(tot/cant, 2))
        print(mun_men, "es el municipio con menos hogares con techo de teja:", menor)
        print(mun_may, "es el muniicpio con más hogares con techo de teja:", mayor)
        return(tot)
    
    def mod_iii(self, ddatos, tot):
        self.dict_mat_const = ddatos
        cant = len(self.dict_mat_const)
        print("\nMunicipio y num viviends debajo del promedio")
        for clave, valor in list(self.dict_mat_const.items()):
            dato = int(valor)
            if dato < tot/cant:
                print(str(clave), dato)
        print("\nMunicipio y valor arriba del promedio")
        for clave, valor in list(self.dict_mat_const.items()):
            dato = int(valor)
            if dato > tot/cant:
                print(str(clave), dato)
        return()