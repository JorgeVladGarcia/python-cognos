'''
Dibujar manualmente un gráfico de gradas utilizando pygal, la construcción del
gráfico debe ser hecha anotando las coordenadas de los extremos de los
segmentos. Utilizar un espacio donde el eje “x” varie de 25 a 35 y el eje “y” de -5 a
5, empezando en x=25, y=-5, terminando en x=35, y=5. Los segmentos deben ser
de magnitud 1 tanto en el eje “x” como en el eje “y”.
'''
import pygal

xyplot = pygal.XY()
xyplot.title = "Grafico facil"

'''

'''
xyplot.add('Gradas_abajo', [(25, -5), (25, -4), (26, -4), (26, -3), (27, -3), (27, -2), (28, -2), (28, -1)])
xyplot.add('Gradas_centro', [(28, -1), (29, -1), (29, 0), (30, 0), (30, 1), (31, 1), (31, 2), (32, 2)])
xyplot.add('Gradas_arriba', [(32, 2), (32, 3), (33, 3), (33, 4), (34, 4), (34, 5), (35, 5)])


xyplot.render_to_file('plot.svg')