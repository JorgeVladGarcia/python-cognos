'''
Transformar ABC Sevilla.docx, que es un documento del procesador de
palabra “Word”, a un formato JSON.
• Analizar el archivo ABC Sevilla.docx
• Convertir el documento Word a un formato JSON
• Cargar el documento al editor Notepad++
• Verificar que cumple adecuadamente con el formato JSON
• Escribir un programa Python que lea el archivo JSON y muestre el texto en pantalla
'''

'''
doc = open("ABC Sevilla.txt")
save = open("ABC Sevilla.json", "w")
data = []

for line in doc:
    line = line.rstrip()
    data.append(line)

#for i in data:
    #print(data[0])
save.write("[\n\t{")
save.write('\n\t\t"linea 1": ' + '"' + data[0] + '",')
save.write('\n\t\t"linea 2": ' + '"' + data[1] + '",')
save.write('\n\t\t"linea 3": ' + '"' + data[2] + '",')
save.write('\n\t\t"linea 4": ' + '"' + data[3] + '",')
save.write("\n\t}\n]")
'''

'''
programa para leer jsons
'''
import json
man_arch = open("ABC Sevilla3.json")
data = man_arch.read()

info = json.loads(data)

print("Cantidad de datos:", len(info))

for item in info:
    print(item["linea"])
