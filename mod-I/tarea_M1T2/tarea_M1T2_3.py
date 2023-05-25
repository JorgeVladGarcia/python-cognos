'''
Cálculo del interés ganado por un depósito
• Pedir el capital (17.500)
• Pedir el interés anual a ganar (7,75 %)
• Pedir la cantidad de meses a calcular (8)
• Procesar y mostrar cuanto se ganará por interés
'''

capital = int(input("Insertar valor del capital: "))
interes = float(input("Insertar valor del interes anual: "))
tmp_mes = int(input("Insertar la cantidad de meses a calcular: "))

def int_dep():
    rslt_intrs = round(capital * ((interes/100)/12 * tmp_mes),2)
    rslt = capital + rslt_intrs
    print("El interés ganado por el deposito será:", rslt_intrs)
    print("El capital con reinversión puede ser:", rslt)

int_dep()