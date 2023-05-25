'''
Organizar y almacenar en una tabla Excel los datos de los Casos
Confirmados Covid de los países y regiones de América provenientes
de la Organización Mundial de la Salud (OMS).
• Revisar los datos del archivo “WHO-COVID-19-global-data.txt”.
• Leer los datos del archivo y seleccionar solo los países y regiones de América
(WHO_region = AMRO).
• Seleccionar solo el dato "Casos Confirmados Covid" (New_cases).
• Transformar los datos de una estructura secuencial a paralela.
• Adecuar los datos en un formato apropiado para Excel.
• Migrar la tabla resultante al programa Excel.
• Mostrar en Excel los datos completos (de enero 2020 a febrero 2021) de la
forma que se indica en “America_Ejemplo.xlsx”. En el ejemplo se muestran
solo los datos de abril 2020.
'''
# abrir archivo
march = open("WHO-COVID-19-global-data.txt", encoding= "latin")

# crear variables
lp = list()

# interar data del archivo para crear datos en formato larog
for linea in march:
    # agregar elementos a una lista
    dato = linea.split()
    # encontrar elementos para crear titulos de columna
    if dato[0] == "Date_reported":
        x = dato[0]+","+dato[2]+","+dato[4]+"\n"
        lp.append(x)
        continue
    # encontrar elementos de la region AMRO
    if dato[3] == "AMRO":
        x = dato[0]+","+dato[2]+","+dato[4]+"\n"
        lp.append(x)

# exportar archivo en formato largo
fout = open("America_long.csv", "w")
for dato in lp:
    fout.write(dato)
fout.close()
march.close()

# importar modulo para reconfigurar datos
import pandas as pd

# leer datos en formato largo
csvFile = pd.read_csv('America_long.csv')
 
# crear data frame 
df = pd.DataFrame(csvFile)

# reconfigurar datos de secuencial a paralela
df = pd.pivot(df, index='Date_reported', columns='Country', values='New_cases')

# verificar datos son correctos
#print(df)

# exportar datos en formato correct a csv
df.to_csv("America_final.csv", index = True, header = True)