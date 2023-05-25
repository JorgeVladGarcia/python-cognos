'''
Obtener CC Covid en los departamentos de Bolivia en un día,
generando los casos con números enteros aleatorios de 0 a 1000
• Importar el módulo random (X)
• Utilizar una lista de los departamentos del país (X)
• Generar en forma aleatoria el dato de los CC Covid por departamento (x)
• Mostrar el dato CC Covid y su departamento (X)
• Mostrar el total de casos Covid en el país de ese día (X)
• Mostrar el promedio de casos Covid de los departamentos (X)

• Mostrar el mejor departamento y su dato del día
• Mostrar el peor departamento y su dato del día
'''

# importar modulos
import random 

# crear lista dpts
bol = ['La Paz', 'Oruro', 'Potosí', 'Cochabamba', 'Chuquisaca', 'Tarija', 'Pando', 'Beni', 'Santa Cruz']

# crear variables
tot = 0
dat_dept = 0
drand_lst= []

# crear bucle
for deptos in bol:
    drand = random.randint(0,100)
    print("Para el departamento de", deptos, "el valor aleatorio es", drand)
    drand_lst.append(drand) # crear lista con valores aleatorios
    try: 
        dat_depto = drand
        tot = tot + dat_depto
        band = True
    except:
        print("Error")
        band = False
        break

# create dictionary from existing lists
res = dict(zip(bol, drand_lst))

if band == True:
    print("\nEl total de casos covid de la semana es", tot)
    print("El promedio diario de la semana es", round(tot/7, 2))  
    print("El mejor departamento del dia es", min(res, key=res.get),"con", min(drand_lst), "casos de covid")
    print("El peor departamento del dia es", max(res, key=res.get),"con", max(drand_lst), "casos de covid")