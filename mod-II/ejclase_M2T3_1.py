'''
Contar cuantas veces se repite cada palabra, sin incluir caracteres
extras, de un texto
• Abrir el archivo “Reza-por-mi.txt”
• Quitar los caracteres extras ligados a cada palabra
• Contar cada una de las palabras
• Mostrar la cantidad de veces que se repite cada palabra utilizada
'''
# importar modulo
import string 

# leer archivo
man_arch = open("Reza-por-mi.txt")
conta = dict()

for linea in man_arch:
    linea = linea.rstrip()
    linea.translate(linea.maketrans("", "", string.punctuation)) # instruccion importante para eliminar caracteres especiales
    linea = linea.lower()
    palabras = linea.split() # separar lineas
    # iterar por palabras, metodo rtradicional
    for item in palabras:
        conta[item] = conta.get(item, 0) + 1
print(conta)