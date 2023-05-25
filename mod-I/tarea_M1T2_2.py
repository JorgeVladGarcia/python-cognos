'''
Cálculo simple de un número al azar entre 0 y 99
• Pedir 3 números enteros de 4 dígitos
• Multiplicar los 3 números
• Obtener y mostrar el número al azar, extrayendo los 2 dígitos menos significativos
del resultado
'''

# Insertar tres numeros que tengan solo cuatro digitos
print("Por favor insertar numeros de cuatro digitos")
num_uno = input("Inserte el primer número de 4 digitos: ")
while len(num_uno) != 4 or (not num_uno.isdigit()):
    print("El valor no es un numero de 4 digitos")
    num_uno = input("Inserte el primer número de 4 digitos: ")
num_uno = int(num_uno)

num_dos = input("Inserte el segundo número de 4 digitos: ")
while len(num_dos) != 4 or (not num_dos.isdigit()):
    print("El valor no es un numero de 4 digitos")
    num_dos = input("Inserte el primer número de 4 digitos: ")
num_dos = int(num_dos)

num_trs = input("Inserte el tercer número de 4 digitos: ")
while len(num_trs) != 4 or (not num_trs.isdigit()):
    print("El valor no es un numero de 4 digitos")
    num_trs = input("Inserte el primer número de 4 digitos: ")
num_trs = int(num_trs)

# Crear funcion 
def mult():
    # multiplicar los 3 numeros insertados
    total_mult = num_uno * num_dos * num_trs
    # convertir total de la mult a una lista
    total_list = [int(x) for x in str(total_mult)]
    print("El resultado de la multiplicacion es:", total_mult)
    # Extraer los 2 numeros mas pequenhos de la lista 
    total_list.remove(min(total_list))
    total_list.remove(min(total_list))
    # Convertir lista a integer
    s = [str(integer) for integer in total_list]
    a_string = "".join(s)
    res = int(a_string)
    print("El resultado menos los 2 digitos menos significativos es:", res)

mult()