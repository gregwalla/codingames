from collections import defaultdict

def addEdge(X, Y, C): edges[X][Y] = edges[Y][X] = C

localcode = True
verbose = False
localFilename = 'examples/slightlylarger.txt'

if localcode: 

    with open(localFilename, 'r') as file:
        input_lines = [line.strip() for line in file]


N, E, S, G = map(int, input_lines[0].split())
hscore = list(map(int, input_lines[1].split()))

gscore = [(100000, 0)[i == S] for i in range(N)]
fscore = [(100000, hscore[i])[i == S] for i in range(N)]
edges = defaultdict(dict); [addEdge(*map(int, input_lines[2:][_].split())) for _ in range(E)]
open, close = set([S]), set()

while open:
    c = min(open, key=lambda x: fscore[x])
    print(c, fscore[c])
    if c == G: break
    open.discard(c); close.add(c)
    for k,v in edges[c].items():
        if not k in close and gscore[c] + v < gscore[k]:
            open.add(k); fscore[k], gscore[k] = gscore[c] + v + hscore[k], gscore[c] + v
