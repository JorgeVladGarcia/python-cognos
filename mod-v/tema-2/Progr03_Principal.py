'''
Progr03_Principal - Elaborar el programa principal que solicitará al usuario el departamento y el
municipio, que desea consultar. Asimismo, llamará a los 3 módulos de acuerdo a la necesidad.
'''

from Progr02_Clase import mat_const

munic = input("Introducir el municipio: ")
dept = input("Introducir el departamento: ")

xyz = mat_const()
idp = xyz.mod_i(dept, munic)
if len(idp) != 0:
    total = xyz.mod_ii(dept, idp)
    xyz.mod_iii(idp, total)
