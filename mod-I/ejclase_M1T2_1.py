'''
Convertir grados Celsius a Fahrenheit:
• Pedir los grados Celsius
• Procesar convirtiendo grados Celsius a Fahrenheit
grf = 32 + grc * 9 / 5
• Mostrar en pantalla los grados Fahrenheit
'''
temp_cels = float(input("Temperatura en celsius: "))
def cels_to_farnh():
    temp_farnh = 32 + temp_cels * 9/5
    print("Temperatura en farenheit es: ", temp_farnh)

cels_to_farnh()