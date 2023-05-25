'''
Lo mismo que el ejercicio 1, pero mostrar las palabras en orden
alfabético, eliminando el signo ¿ en las palabras que se presente
• Abrir el archivo “Reza-por-mi.txt”
• Quitar caracteres extras y contar las veces que se invoca cada palabra
• Mostrar en orden alfabético la cantidad de veces que se repite cada palabra
'''
import string 

# leer archivo
man_arch = open("Reza-por-mi.txt", encoding='utf8')
conta = dict()

for linea in man_arch:
    linea = linea.rstrip()
    linea.translate(linea.maketrans("", "", string.punctuation)) # instruccion importante para eliminar caracteres especiales
    linea = linea.lower()
    palabras = linea.split() # separar linease
    # iterar por palabras, metodo rtradicional
    for item in palabras:
        conta[item] = conta.get(item, 0) + 1

# almacenar valores del diccionario en lista
list = list(conta.keys())
# ordenar lista por orden alfabetic
list.sort()

for clave in list:
    print(clave, conta[clave])

#print(conta)
