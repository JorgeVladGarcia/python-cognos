'''
Crear el archivo *.xml del árbol XML de sus abuelos, padres, hermanos,
esposo(a), hijos y nietos (incluir todos los que tenga) indicando la actividad
que cada uno de ellos realiza (profesión o función), verificar que el XML es
correcto y mostrar en un listado el árbol genealógico de la familia.
• Definir y crear el archivo *.xml con el editor de texto Notepad++
• Verificar que el archivo XML es correcto con el navegador de la máquina
• Importar los módulos necesarios, abrir y descargar el árbol XML
• Mostrar el listado del árbol genealógico de la familia (familiar, nombre y actividad)
'''

import xml.etree.ElementTree as ET

datos_empr = open("familia.xml", encoding="utf8")

rruu = ET.parse(datos_empr)

apellido = rruu.findall('familia_materna')
for item in apellido:
    print("- Familia", item.get("apellido"))

prim_gen = rruu.findall('familia_materna/relacion')
for item in prim_gen:
    print("Parentezco:", item.get("parentezco"))
    print("\tOcupación:", item.find("ocupacion").text)
    print("\tNombre familiar:", item.find("nombre").text)

seg_gen = rruu.findall('familia_materna/relacion/relacion')
for item in seg_gen:
    print("Parentezco:", item.get("parentezco"))
    print("\tOcupación:", item.find("ocupacion").text)
    print("\tNombre familiar:", item.find("nombre").text)

apellido = rruu.findall('familia_paterna')
for item in apellido:
    print("\n- Familia", item.get("apellido"))

prim_gen = rruu.findall('familia_paterna/relacion')
for item in prim_gen:
    print("Parentezco:", item.get("parentezco"))
    print("\tOcupación:", item.find("ocupacion").text)
    print("\tNombre familiar:", item.find("nombre").text)

seg_gen = rruu.findall('familia_paterna/relacion/relacion')
for item in seg_gen:
    print("Parentezco:", item.get("parentezco"))
    print("\tOcupación:", item.find("ocupacion").text)
    print("\tNombre familiar:", item.find("nombre").text)    
