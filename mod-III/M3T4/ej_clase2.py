import json

man_arch = open("bolivia2.json")
data = man_arch.read()

info = json.loads(data)

for item in info:
    print('\nFecha:', item["fecha"])
    print('Codigo pais:', item["cod_pais"])    
    print('Pais:', item["pais"])    
    print('Region WHO:', item["region_WHO"])    
    print('Casos comprobados:', item["casos_compr"])    
    print('Casos acumulados:', item["cc_acumul"])    
    print('Muertes:', item["muertes"])    
    print('Muertes acumuladas:', item["m_acumul"])    
