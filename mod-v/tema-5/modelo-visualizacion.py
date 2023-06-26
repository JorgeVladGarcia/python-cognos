import sqlite3
def cargar_BD(arch_csv):
    cur.executescript('''
        drop table if exists ;        
        drop table if exists ;
        drop table if exists ;
        drop table if exists ;

        create table dpm (
            id integer primary key autoincrement
            dpto        text,
            provincia   text,
            municipio   text
        );

        create table mat_constr(
            dpm_id 

        );
        create index 
        '''
    )
    march = open(arch_csv, encoding="utf8")
    band = true 
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
            for num in range(tam):
                sbb.append(str(ltemp[num]))
            if munic != sbb[2]:
                
    return 