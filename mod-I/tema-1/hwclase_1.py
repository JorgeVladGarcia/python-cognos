'''
1. ¿Dónde está el programa mientras se ejecuta?
    En la memoria ram y procesador. 
2. Explique las características de un compilador comercial
    Los compiladores comerciales permiten generar código de máquina inmediatamente, envía el código fuente a un ensamblador y el ensamblador genera un programa (por ejemplo archivos .exe). 
3. Explique las características de un intéprete moderno
    Los interpretes ejecutan instrucciones. Los intérpretres evalúan y ejecutan programas, si es que detectan errores, detienen la ejecución del programa. Ayuda a transmitir las instrucciones del código a la máquina.
4. Detalle un ejemplo de un error de semántica
    Por ejemplo en la formación de oraciones, un error de semántica causaría que una oración sea incorrecta y no tenga sentido porque incumple ciertas normas y reglas. En lugar de decir, "Yo como una manzana", una oración con errores de semántica podría decir "Mi comer un manzana". 
    
5. Elborar un programa que haga:
    - Valor inicial de una variable = 10
    - Proporciona 5 por teclado
    - Añadir ese valor a la variable
    - Mostrar en pantalla el valor final

'''

valor_init = 10
print("El valor inicial es:", valor_init)
valor = int(input("Añade el valor de cinco: "))
print("El valor final es:", valor_init+valor)