'''
1. Convertir grados Celsius a Fahrenheit:
• Pedir los grados Celsius usando try – except y aceptar solo de -10 a 49
grados Celsius
• Procesar convirtiendo grados Celsius a Fahrenheit
• Mostrar en pantalla los grados Fahrenheit o el mensaje de error.
'''

temp_cels = input("Insertar temperatura en Celsius: ")
try: 
    cc = float(temp_cels)
    if cc >= -10 and cc <= 49:
        temp_farnh = 32 + cc * 9/5
        print("El valor en Fahrenheit es:", temp_farnh)
    else: 
        print("El valor no esta dentro del rango.")
except:
    print("Ingresar valores entre -10 y 49 grados celsius")
