"""
Simple parser para archivos KB con hechos del tipo:
conecta(EstacionA,EstacionB,3)
coord(EstacionA, -74.05, 4.66)
Comentarios con #
"""
import re

def parse_kb(path):
    edges = []
    coords = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split('#',1)[0].strip()
            if not line: continue
            m = re.match(r'conecta\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([0-9.]+)\s*\)', line)
            if m:
                a = m.group(1).strip()
                b = m.group(2).strip()
                w = float(m.group(3))
                edges.append((a,b,w))
                continue
            m2 = re.match(r'coord\(\s*([^,]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)', line)
            if m2:
                n = m2.group(1).strip()
                coords[n] = (float(m2.group(2)), float(m2.group(3)))
                continue
    return edges, coords
