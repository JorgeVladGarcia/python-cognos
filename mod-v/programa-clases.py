def tot_prom_men_may(self, pais, ltdatos):
    self.ltupl = ltdatos
    tot = 0
    menor = mayor = None
    cant = len(self.ltupl)
    for nn in range(cant):
        fecha,dato = self.ltupl[nn]
        tota = tot + dato
         if menor == None or menor > dato:
           mejor = dato
           dmen = fecha 
    # leer el primer registro de ltupl y obnter la fecha inicial
    fech_ini, dato = self.ltupl[0]
    # leer el último registro
    fech_ini, dato = self.ltupl[-1]
    print("El total de casos de")
    print("Promedio diario de casos")
    print(dmen, )
    print(dmay,)
    return(tot)


# esquelot de abajo arriba, dias arriba del promedio y dias abajo del promedio

# crear metodo
def abaj_arriba(self, ltdatos,tot):
    self.ltupl = ltdatos 
    cant = len(self.ltupl)
    print("Dia y valor bajo del promedio diario")
    for nn in rang(cant):
       fecha, dato = self.ltupl[nn]
       if dato < tot/cant: 
          print(fecha,dato)
    print("Dia y valor arriba del promedio diario")
    for nn in rang(cant):
       fecha, dato = self.ltupl[nn]
       if dato > tot/cant: 
          print(fecha,dato)
    return()          
          