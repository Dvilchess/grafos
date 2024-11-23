# Simulación de una ciudad utilizando Grafos

Este programa simula una ciudad representada como un grafo, utilizando Python, PyQt5 y NetworkX. Los nodos representan familias, servicios esenciales (hospitales, escuelas, bomberos, etc.) y edificios, mientras que las aristas representan caminos con pesos que indican distancias o costos. Es ideal para visualizar rutas y gestionar eventos en la ciudad.

1.Creación de grafos:
Genera una ciudad con familias y servicios conectados aleatoriamente.
Evita nodos aislados y asigna pesos a las conexiones.

2.Visualización:
Muestra el grafo de la ciudad con nodos y caminos usando Matplotlib.
Destaca rutas específicas durante eventos.

3.Simulación de ciudad:
Permite crear familias con atributos (número de miembros, niños, trabajos).
Simula eventos como robos, incendios y emergencias médicas.

4.Cálculo de rutas:
Calcula rutas óptimas usando NetworkX, por ejemplo:
Rutinas diarias (llevar niños al colegio, ir al trabajo).
Respuestas rápidas a emergencias.

5. Interacción GUI:
Crear, visualizar y eliminar ciudades.
Gestionar familias y responder a eventos directamente desde una interfaz gráfica.


Requisitos:
-Python 3.x
-pyqt5
-networkx
-matplotlib
