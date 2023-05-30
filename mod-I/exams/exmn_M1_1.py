'''
1. Procesar mediante funciones los Casos Comprobados (CC) Covid de los
departamentos de Bolivia en un día generando los casos en forma aleatoria
entre 50 y 600. (X)
• No utilizar listas ni otras herramientas que no se hayan presentado en el curso
• Todos los procesos necesarios a programar deben estar definidos por funciones (def) (X)
• Importar el módulo random (X)
• Generar en forma aleatoria el dato de los CC Covid por departamento (X)
• Mostrar cada departamento y su dato de CC Covid (X)
• Mostrar el total de casos del país presentados ese día (X)
• Mostrar el promedio de casos de los departamentos (X)
• Mostrar el mejor departamento y su dato del día (X)
• Mostrar el peor departamento y su dato del día (X)
• Mostrar cada departamento y su dato que están por encima del promedio (X)
• Mostrar cada departamento y su dato que están por debajo del promedio (X)
'''
# importar modulos
import random 

# crear funcion
def cc_func(lista):
	# definir variables de la funcion
	mjor = None
	peor = None
	tot = 0
	indice = 0
	vdepto = [0] * len(lista)
    # crear bucle para iterar en la lista
	for depto in lista:
		drand = random.randint(50,600)
		print("Para el departamento de", depto, "el valor aleatorio es", drand)
		tot = tot + drand
		if mjor == None or drand < mjor:
			mjor = drand
			dpto_mjor = depto
		if peor == None or drand > peor: 
			peor = drand 
			dpto_peor = depto
		vdepto[indice] = drand
		indice += 1
    # crear variable promedio
	avg = round(tot/len(lista), 2)
    # imprimir los resultados
	print("\nEl total de casos presentados del país es:", tot)
	print("El promedio de casos de los departamentos es:", avg)
	print("El mejor departamento es", dpto_mjor, "con", mjor, "casos.")
	print("El peor departamento es", dpto_peor, "con", peor, "casos.")
	print("\nLos departamentos que están por encima del promedio son:")
	for n in range(len(lista)):
		if vdepto[n] > avg: print("-", lista[n], "con:", vdepto[n])
	print("\nLos departamentos que están por abajo del promedio son:")
	for n in range(len(lista)):
		if vdepto[n] < avg: print("-", lista[n], "con:", vdepto[n])


# crear lista de variables
bol = ['La Paz', 'Oruro', 'Potosí', 'Cochabamba', 'Chuquisaca', 'Tarija', 'Pando', 'Beni', 'Santa Cruz']

# llamar funcion 
cc_func(bol)