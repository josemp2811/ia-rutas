import sys
from kb_parser import parse_kb
from graph_search import Graph, dijkstra, astar

def build_graph(edges):
    g = Graph()
    for a,b,w in edges:
        g.add_edge(a, b, w)
    return g

def main(kb_path, origen, destino, mode='dijkstra'):
    edges, coords = parse_kb(kb_path)
    g = build_graph(edges)
    if mode == 'astar' and coords:
        path, cost = astar(g, origen, destino, coords)
    else:
        path, cost = dijkstra(g, origen, destino)
    if path is None:
        print("No se encontró ruta entre", origen, "y", destino)
    else:
        print("Ruta encontrada ({}):".format(mode))
        print(" -> ".join(path))
        print("Costo total (tiempo):", cost)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Uso: python main.py kb/kb_sample.txt EstacionA EstacionC [dijkstra|astar]")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv)>4 else 'dijkstra')
