from Progr02_Clase import 


elpais = input("Introducir el pais:")
try:
    f_ini = input()
    f_ini_n = int(f_ini)
except:
    print("El dato debe ser numerico")
    exit()
try:
    f_inic = date(int(f_ini[0:4]), )
except:
    print("la fecha inicial esta mal proporcionada...")
    exit()    
