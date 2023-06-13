'''
Dibujar manualmente una estrella de 5 puntas como la gráfica que se adjunta
utilizando pygal, la construcción del gráfico debe ser hecha anotando las
coordenadas de los extremos de los segmentos. El espacio XY a utilizar es decisión
propia de cada uno.
'''
import pygal

xyplot = pygal.XY()
xyplot.title = "Grafico facil"


xyplot.add('linea-1', [(-2, -6), (0, 6)])
xyplot.add('linea-2', [(0, 6), (2, -6)])
xyplot.add('linea-3', [(2, -6), (-2, 2)])
xyplot.add('linea-4', [(-2, 2), (2, 2)])
xyplot.add('linea-6', [(2, 2), (-2, -6)])
#xyplot.add('Gradas_centro', [(28, -1), (29, -1), (29, 0), (30, 0), (30, 1), (31, 1), (31, 2), (32, 2)])
#xyplot.add('Gradas_arriba', [(32, 2), (32, 3), (33, 3), (33, 4), (34, 4), (34, 5), (35, 5)])
#

xyplot.render_to_file('tarea-1.svg')