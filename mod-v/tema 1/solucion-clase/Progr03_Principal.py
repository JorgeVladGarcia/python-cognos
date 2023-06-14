from Progr02_Clase import casos_covid19
from datetime import date

'''
OBJETIVO PRINCIPAL:
Solicitar al usuario el país y el período (fecha inicial y fecha final) que
desea consultar, utilizando el mecanismo de try y except para verificar que
las fechas inicial y final son proporcionadas en forma numérica y de acuerdo
al calendario. Los datos de las fechas deben estar comprendidas en el período
válido del Covid-19 (de Ene-2020 a la fecha actual).

Con el país y los datos del período correctos va llamando a cada uno de los
tres módulos para calcular y mostrar en pantalla:
    - El total de casos Covid-19 presentados durante ese período
    - El promedio diario de casos en ese período
    - Los días en que se presentaron el menor y la mayor cantidad de casos
    - Las listas de los días y cantidad de casos Covid-19 que quedaron abajo
      y arriba del promedio diario durante ese período
'''

elpais = input("Introducir el país: ")
# Solicita la Fecha Inicial
try:
    f_ini = input("Introducir la fecha inicial (formato: aaaammdd): ")
    f_ini_n = int(f_ini)
except:
    print("El dato debe ser numérico...")
    exit()
try:
    f_inic = date(int(f_ini[0:4]), int(f_ini[4:6]), int(f_ini[6:]))
except:
    print("La fecha inicial está mal proporcionada...")
    exit()
# Solicita la Fecha Final
try:
    f_fin = input("Introducir la fecha final (formato: aaaammdd): ")
    f_fin_n = int(f_fin)
except:
    print("El dato debe ser numérico...")
    exit()
try:
    f_final  = date(int(f_fin[0:4]), int(f_fin[4:6]), int(f_fin[6:]))
except:
    print("La fecha final está mal proporcionada...")
    exit()
# Con el país y período correcto, llama a los módulos de acuerdo a la necesidad
xyz = casos_covid19()
idp = xyz.extrae_CC(elpais, f_inic, f_final)
if len(idp) != 0:
    total = xyz.tot_prom_men_may(elpais, idp)
    xyz.abajo_arriba(idp, total)
else:
    print("ERROR, No existe el país o el período no es válido para Covid")
