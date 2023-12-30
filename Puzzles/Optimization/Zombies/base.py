import numpy as np

a = [(1,2), (3,4), (12,4)]
b = (2,2)

def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)

print(closest_node(b, a))