import sys

square = 0
vertexes = list()
for vertex in list(map(str.strip, sys.stdin)):
    vertex = vertex.split()
    vertexes.append((float(vertex[0]), float(vertex[1])))
vertexes.sort()
prev = 0
for vertex in vertexes:
    if prev != 0:
        square += (vertex[1] + prev[1]) / 2 * (vertex[0] - prev[0])
    prev = vertex
with open('res.txt', mode='w') as f:
    f.write(str(square))
