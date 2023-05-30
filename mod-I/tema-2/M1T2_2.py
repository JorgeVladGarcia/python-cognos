cvd_cs_lun = int(input("No. casos lunes: "))
cvd_cs_mar = int(input("No. casos martes: "))
cvd_cs_mir = int(input("No. casos miercoles: "))
cvd_cs_juv = int(input("No. casos jueves: "))
cvd_cs_vir = int(input("No. casos viernes: "))
cvd_cs_sab = int(input("No. casos sabado: "))
cvd_cs_dom = int(input("No. casos domingo "))

def cvd_cs(decimals = 2):
    total_sem = cvd_cs_lun + cvd_cs_mar + cvd_cs_mir + cvd_cs_juv + cvd_cs_vir + cvd_cs_sab + cvd_cs_dom
    print("Total casos covid en la semana es: ", total_sem)
    avg_daily = round(total_sem / 7, 2)
    print("Promedio diario de casos covid es: ", avg_daily)

cvd_cs()