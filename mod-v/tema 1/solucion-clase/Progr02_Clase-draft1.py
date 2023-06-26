from pais_periodo_clase import casos_covid19
from datetime import date

# Programa principal, pide datos y llama a las 3 funciones
elpais = input("Introducir el país: ")
# Solicita la Fecha Inicial
try:
    f_ini = input("Introducir la fecha inicial (formato: aaaammdd): ")
    f_ini_n = int(f_ini)
except:
    print("El dato debe ser numérico...")
    exit()
try:
    a_ini = int(f_ini[0:4])
    if a_ini < 2020 or a_ini > 2023:
        print("El año inicial tiene que estár entre 2020 y 2023...")
        exit()
    else:
        f_inic = date(a_ini, int(f_ini[4:6]), int(f_ini[6:]))
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
    a_fin = int(f_fin[0:4])
    if a_fin < 2020 or a_fin > 2023:
        print("El año final tiene que estár entre 2020 y 2023...")
        exit()
    f_final  = date(a_fin, int(f_fin[4:6]), int(f_fin[6:]))
except:
    print("La fecha final está mal proporcionada...")
    exit()
# Con el país y período recibido, ejecuta la parte principal
xyz = casos_covid19()
idp = xyz.extrae_CC(elpais, f_inic, f_final)
if len(idp) != 0:
    total = xyz.tot_prom_men_may(elpais, f_inic, f_final, idp)
    xyz.abajo_arriba(f_inic, idp, total)
