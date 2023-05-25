'''
Generar los valores de una curva senoidal:
• Estudiar en https://www.python.org/doc/ buscar Library Reference luego Numeric
and Mathematical Modules finalmente math
• Importar el módulo math
• Generar los valores de la curva del seno cada 10 grados de los 360 grados
• Mostrar el valor del seno cada 10 grados (de 0 a 360 grados), mostrar por línea:
Para xxx grados, el valor del seno es yyy
'''
import math 

var1 = 0
while var1 < 360:
    var1 = var1 + 10
    grnd_rdn = math.radians(var1)
    sine = round(math.sin(grnd_rdn), 2)
    print("Para", var1, "grados, el valor del seno es", sine)