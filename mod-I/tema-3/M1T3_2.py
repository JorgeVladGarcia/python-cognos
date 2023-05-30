'''
Nuevos casos Covid comprobados de lunes a miercoles:
• Pedir los datos de esos días usando try – except para cada día
• Mostrar el promedio diario de los nuevos casos
• Mostrar el total de casos de los 3 días
• Indicar cuál es el mejor día
• Indicar cuál es el peor día
'''


cs_cvd_lun = input("No. total casos lunes:")
try: 
    cc = int(cs_cvd_lun)
    if cc >= -10 and cc <= 49:
        temp_farnh = 32 + cc * 9/5
        print("El valor en Fahrenheit es:", temp_farnh)
    else: 
        print("El valor no esta dentro del rango.")
except:
    print("Ingresar valores entre -10 y 49 grados celsius")
