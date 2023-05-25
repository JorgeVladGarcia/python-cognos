'''
Expandir los grupos de datos del archivo Valores.txt en una sola
línea y almacenarlos en el archivo Una_linea.txt
• Abrir el archivo Valores.txt el mismo que tiene grupos de datos
• Cada grupo de datos se compone de 5 líneas, la primera tiene un solo dato y las 4
restantes tienen 6 datos, por consiguiente son 25 datos por grupo.
• El propósito es colocar los 25 datos del grupo en una sola línea, respetando los
anchos de los datos.
• Grabar las líneas expandidas de 25 datos cada una en el archivo Una_linea.txt
'''

# abrir el archivo
file = open("Valores.txt")
outf = open("Una_linea.txt", "w")
# leer en bucle
cont = 0
output = ""
for line in file:
    # rstrip quita retorno de carro
    line = line.strip()
    #print(line)
    # separar cada valor de las lineas
    values = line.split()
    #print(values)
    # leer cada valor en una linea
    for value in values:
        output += value + ", "
        #print(output)
        cont += 1
        # PENDIENTE, SEPARAR LINEAS CADA 25 ELEMENTOS
        for split in output:
            output2 = output.split(",", 25)
            print(output2[1])
    #outf.write(output[:-1])
file.close()
outf.close()