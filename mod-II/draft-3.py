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