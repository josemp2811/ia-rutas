Pruebas realizadas (ejecutar en carpeta src):
1) Dijkstra ejemplo:
   python main.py ../kb/kb_sample.txt EstacionA EstacionE dijkstra
   Resultado esperado: Ruta encontrada (...) EstacionA -> EstacionB -> EstacionC -> EstacionE  Costo total (tiempo): 9

2) A* ejemplo:
   python main.py ../kb/kb_sample.txt EstacionA EstacionE astar
   Resultado esperado: mismo camino y costo que Dijkstra (9) — A* usará heurística basada en coords.

3) Caso sin ruta:
   Modificar KB o pedir ruta entre EstacionA y EstacionZ (no existente) -> "No se encontró ruta..."