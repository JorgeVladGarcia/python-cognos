'''
Realizar el Ejercicio de clase 2 pero solo para lunes, martes y miércoles,
utilizar la sentencia "if" cuando corresponda y mostrar:
• El peor día y su valor
• El mejor día y su valo
'''

# pedir valores de casos covid
lunes = int(input("No. de casos lunes: "))
martes = int(input("No. de casos martes: "))
miercoles = int(input("No. de casos miércoles: "))

# guardar valores en lista
cvd_cs = [lunes, martes, miercoles]

# crear diccionario de datos
data = {'lunes': lunes
    , 'martes': martes
    , 'miércoles': miercoles}

# crear funcion para encontrar valor menor (mejor dia)
def find_smallest_element(cvd_cs):
    smallest_element = cvd_cs[0]
    for current_element in cvd_cs:
        if smallest_element > current_element:
            smallest_element = current_element
    return smallest_element

# crear funcion para enconrar valor mayor (peor dia)
def find_largest_element(cvd_cs):
    largest_element = cvd_cs[0]
    for current_element in cvd_cs:
        if largest_element < current_element:
            largest_element = current_element
    return largest_element

# Hallar total de casos covid
sum_cvd_cs = sum(cvd_cs)

# Hallar promedio diario de casos covid, con 2 decimales 
avg_daily = round(sum_cvd_cs / 7, 2)

print("El total de casos covid en la semana es:", sum_cvd_cs)
print("El promedio diario de casos covid esta semana es:", avg_daily)
print("El mejor día fue", min(data, key=data.get), "con", find_smallest_element(cvd_cs), "caso(s).")
print("El peor día fue", max(data, key=data.get),"con", find_largest_element(cvd_cs), "caso(s).")