'''
Pedir nombres, luego los apellidos y finalmente mostrar el nombre completo del usuario
''' 

nomb_prim = input("Primer nombre: ")
nomb_sgdo = input("Segundo nombre: ")
aplldo_pat = input("Apellido paterno: ")
aplldo_mat = input("Apellido materno: ")


def f_nomb_cmplto():
    nomb_cmplto = nomb_prim + " " + nomb_sgdo + " " +  aplldo_pat + " " + aplldo_mat
    print("El nombre completo es: ", nomb_cmplto)
 
f_nomb_cmplto()