'''
Elaborar un programa que muestre el comportamiento de la Conjetura de
Collatz
• Fue enunciada por el matemático alemán Lothar Collatz en 1937, a la fecha no resuelta.
• Dice que tomando cualquier número (n) entero no negativo que no sea cero, si es par se calcula n/2, si es impar 3n + 1.
• Al número resultante se le vuelve a ejecutar el mismo procedimiento y así sucesivamente.
• La hipótesis dice: independientemente del valor inicial (n), el valor siempre tiende a 1.
• Elaborar un programa que solicite el valor inicial (n), verificar con try – except que sea un número entero positivo, no 0 y repetir la solicitud hasta teclear el valor correcto (X)
• Aplicar la Conjetura de Collatz, con diferentes pasos hasta que el valor final sea 1.
• El programa debe mostrar los valores intermedios en una línea y en la siguiente indicar la cantidad de pasos necesarios que se tuvo que hacer para llegar al valor de 1 con el mensaje:

Para el número zz el total de pasos fue: xx.

• Resultados: El 15 tiene 17 pasos, el 6 tiene 8, el 11 tiene 14 , el 27 tiene 111 pasos.
'''

# tomar valores que sean mayores enteros, no negativos y distintos a cero
while True:
    value_init = input("Insertar el valor inicial: ")
    try:
        value_init = int(value_init)
        if value_init > 0:
            break                
        else:
            print("El valor debe ser un numero entero no negativo distinto a cero. Por favor insertar el valor una vez mas.")
    except ValueError:
        print("El valor debe ser un numero. Por favor insertar el valor una vez mas.")

# imprimir resultados de los valores intermedios
print("Los valores intermedios son:")

# crear variables
counter = 0
value_collatz = value_init

# crear loop
while value_collatz !=1:
    counter += 1
    print(value_collatz, end = ", ")
    if value_collatz % 2 == 0:
        value_collatz = value_collatz / 2
    else:
        value_collatz = 3 * value_collatz + 1
    
# imprimir resultados
print("\nPara el numero", value_init, "el total de pasos fue:", counter)
