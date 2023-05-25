'''
Listar los vecinos que habitan una ciudad ordenados por dirección y
otro listado por apellido-nombre.
• Abrir el archivo “Vecinos.txt”
• Leer, procesar y ordenar la información del archivo
• Preguntar que listado desea mostrar: por dirección o por apellido
• Mostrar el listado seleccionado
• Volver a preguntar que listado desea mostrar, hasta teclear “fin”
'''
march = open("Vecinos.txt", encoding='utf-8')
vecinos = dict()

for lineas in march:
    lineas = lineas.rstrip()
    campos = lineas.split("\t")
    if campos[0] == "Nombre":
        continue
    vecinos[campos[1],campos[0]] = campos[2]
    
while True:
    pregu = input("\nDar unicamente: apell, direc, fin...")
    if pregu == "apell":
        lista = list()
        for nombre,direccion in vecinos.items():
            lista.append((nombre,direccion))
        lista.sort()
        for dato, direc in lista:
            print(dato[0], dato[1], direc)
    elif pregu == "direc":
        lista = list()
        for nombre,direccion in vecinos.items():
            lista.append((direccion, nombre))
        lista.sort()
        for direc, dato in lista:
            print(direc, dato[0], dato[1])
    elif pregu == "fin":
        print("Terminamos")
        break
    else:
        print("Solo es valido apell, direc, fin...")
