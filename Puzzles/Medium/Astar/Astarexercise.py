#
import sys
import math
from queue import PriorityQueue
from collections import deque, OrderedDict

localcode = True
verbose = False
localFilename = 'examples/slightlylarger.txt'

################

def get_neighbors(edges_dict, node):
    ''' '''
    neighbors = set()
    for key in edges_dict.keys() : 
        key = key.split('-')
        if key[0] == node : 
            neighbors.add(key[-1])
        elif key[-1] == node :
            neighbors.add(key[0])
        else:
            pass
    return neighbors


def get_path(nodes_origin, f, start, goal):

    assert start in nodes_origin.values()

    de = deque()

    while nodes_origin[goal] != start :
        de.appendleft(f'{goal} {f[goal]}')
        goal = nodes_origin[goal]

    de.appendleft(f'{goal} {f[goal]}')
    de.appendleft(f'{start} {f[start]}')

    return de

#################

if localcode: 
    #start parsing
    with open(localFilename, 'r') as file:
        input_lines = [line.strip() for line in file]
    #first line
    n, e, s, gl = [int(i) for i in input_lines[0].split()]

    #nodes
    #Heuristic for each node
    heuristics = []
    for i in input_lines[1].split():
        heuristics.append(int(i))
    nodes = [str(i) for i in range(n)]
    h= dict(zip(nodes, heuristics))

    #edges
    #create a dictionary with the weight of the edges
    edges_costs = input_lines[2:]

    edges_dict = dict()

    for elt in edges_costs: 
        edge = elt.split()
        ky = edge[0] + '-' + edge[1]
        ky2 = edge[1] + '-' + edge[0]
        vl = int(edge[2])
        edges_dict[ky] = vl
        edges_dict[ky2] = vl


else : 

    n, e, s, gl = [int(i) for i in input().split()]

    nodes = [str(i) for i in range(n)]
    heuristics = []
    for i in input().split():
        heuristics.append(int(i))
    h= dict(zip(nodes, heuristics))

    edges = []
    for i in range(e):
        edge_cost = [int(j) for j in input().split()]
        edges.append(edge_cost)
    edges_list = [str(edge[0]) + '-'+ str(edge[1]) for edge in edges]
    edges_list2 = [str(edge[1]) + '-'+ str(edge[0]) for edge in edges]
    edge_costs = [int(edge[2]) for edge in edges]
    edges_dict = dict(zip(edges_list, edge_costs))
    edges_dict2 = dict(zip(edges_list2, edge_costs))
    edges_dict = dict(edges_dict, **edges_dict2)

##################

start = str(s) 
came_from  = start
g= dict() 
g[came_from] = 0

goal = str(gl) 

nodes_origin = dict()

openSet = PriorityQueue() 

closed_nodes = set()

f= dict()
f[start] = h[start] 
openSet.put((f[start], start))

visiting = OrderedDict()
visiting[start] = f[start]

node = start
i  = 0

##################

while (node != goal and i < 30) : 

    neighbors = get_neighbors(edges_dict, node)

    closed_nodes.add(came_from)
    if verbose:
        print(f'stp : {i}, nd : {node} , cm_fr : {came_from}, nbhrs: {neighbors} , clo_nds: {closed_nodes}', file=sys.stderr, flush=True)
    
    for neighbor in neighbors:
        if neighbor not in closed_nodes :
            
            edge_dist = edges_dict[str(node)+'-'+str(neighbor)]
            potential_cost = g[came_from] + edge_dist

            if  not g.get(neighbor):
                g[neighbor] = potential_cost
                nodes_origin[neighbor] = node
            if potential_cost < g[neighbor]:
                g[neighbor] = potential_cost
                nodes_origin[neighbor] = node
            
            f[neighbor] = h[neighbor] + g[neighbor]

            openSet.put((f[neighbor], neighbor))
            #print(f'inserted neighbor: {neighbor} with f:{f[neighbor]}', file=sys.stderr, flush=True)

    came_from = node

    node = openSet.get()[-1] #select node with minimum f 
    
    if node not in visiting:
        visiting[node] = f[node]
    elif visiting[node] < f[node]:
        visiting[node] = f[node]
    else:
        pass
    
    g[came_from] = g[node] 

    i= i+1

#print(f'visiting: {visiting}')

path = get_path(nodes_origin, f, start, goal)

for k, v in visiting.items(): 
    print(k, v)

