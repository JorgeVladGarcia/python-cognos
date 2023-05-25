temp_cels = float(input("Insertar temperatura en Celsius: "))
def cels_to_farnh():
    temp_farnh = 32 + temp_cels * 9/5
    print("La temperatura en Farenheit es: ", temp_farnh)

cels_to_farnh()