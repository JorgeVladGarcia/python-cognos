'''
1. Ejercicios en clase M1T4
	1. segundo ejercicios: mostrar casos comprobados covid de la semana
- elaborar una funcion que pida los datos del dia usando try except
- pedir datos de todos los dias de la semana
- en caso de falla el valor del dia sera 0 y enviara el mensaje de error
- mostrar el total de los nuevos casos de la semana
- mostrar el promedio diario de los nuevos casos
'''

def datos_dia(dia, val_ini): # servira para los 7 dias de la semana, y con el valor que empezamos el dia
    try:
        mensaje = "Dame dato del dia " + dia + ": "
        dato = input(mensaje)
        dfinal = int(dato) + val_ini # dato lo actualizo con el dato inicial
    except: # si existe error
        dfinal = val_ini + 0 #ponemos valor cero para el dia
        print("Error al dar el valor del dia, en este caso, sera ", dia)
    return dfinal

tot = datos_dia("lunes", 0)
tot = datos_dia("martes", tot)
tot = datos_dia("miercoles", tot)
tot = datos_dia("jueves", tot)
tot = datos_dia("viernes", tot)
tot = datos_dia("sabado", tot)
tot = datos_dia("domingo", tot)

print("El total de casos Covid de la semana es:", tot)
print("El promedio diario de casos Covid es:", tot/7)

'''
Modulo 1, Curso 4, Ejercicio en Clase 2
Nuevos Casos Comprobados (CC) Covid de la semana:
    Elaborar una función que pida los datos del día usando try – except
    Pedir los datos de todos los días de la semana
    En caso de falla el valor del día será 0 y enviará el mensaje de error
    Mostrar el total de los nuevos casos de la semana
    Mostrar el promedio diario de los nuevos casos

def pdato(dia, valor):
    try:
        mdia = "Dame el valor del día " + dia + " ... "
        nvalor = valor + int(input(mdia))
    except:
        nvalor = valor
        print("El valor del", dia, "no es correcto, quedará como 0")
    return nvalor

tot = pdato("lunes", 0)
tot = pdato("martes", tot)
tot = pdato("miercoles", tot)
tot = pdato("jueves", tot)
tot = pdato("viernes", tot)
tot = pdato("sabado", tot)
tot = pdato("domingo", tot)
print("El total de casos Covid de la semana es:", tot)
print("El promedio diario de la semana es:", tot/7)

'''