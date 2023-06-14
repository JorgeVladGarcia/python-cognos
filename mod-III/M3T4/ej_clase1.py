doc = open("Covid19-Bol.txt")

for line in doc:
    line = line.rstrip()
    line = line.split("\t")
    print('{ "fecha" :' + ' "' + str(line[0]) + '" ,')
    print('"cod_pais" :'+ ' "' + line[1] + '",')
    print('"pais" :' + ' "' + line[2] + '",')
    print('"region_WHO" :' + ' "' + line[3] + '",')
    print('"casos_compr" :' + ' "' + line[4] + '",')
    print('"cc_acumul" :' + ' "' + line[5] + '",')
    print('"muertes" :' + ' "' + line[6] + '",')
    print('"m_acumul" :'+ ' "' + line[7] + '"')
    print('},')