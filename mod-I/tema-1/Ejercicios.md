# Tema 1: Introducción a Python
## Ejercicios en clase 1
1. Mostrar un mensaje en pantalla
2. Captar un mensaje de entrada 
3. Pedir un mensaje e imprimirlo 5 veces
4. Mostrar 5 veces el mensaje de entrada
```
nombre = input("Dame tu nombre... ")
for i in range(5):
    print ("Tu nombre es:", nombre)
```
Los resultados serían: 
```
Dame tu nombre... Jorge
Tu nombre es: Jorge
Tu nombre es: Jorge
Tu nombre es: Jorge
Tu nombre es: Jorge
Tu nombre es: Jorge
```
## Tarea Tema 1 
Elaborar un programa que haga:
    - Valor inicial de una variable = 10
    - Proporciona 5 por teclado
    - Añadir ese valor a la variable
    - Mostrar en pantalla el valor final
```
valor_init = 10
print("El valor inicial es:", valor_init)
valor = int(input("Añade el valor de cinco: "))
print("El valor final es:", valor_init+valor)
```
