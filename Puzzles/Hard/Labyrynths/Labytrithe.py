import sys
import math
from collections import deque


graph =  {(6, 5): [('RIGHT', (6, 6))], 
        (6, 6): [('LEFT', (6, 5)), ('RIGHT', (6, 7))], 
        (6, 7): [('LEFT', (6, 6)), ('RIGHT', (6, 8))], 
        (6, 8): [('LEFT', (6, 7)), ('RIGHT', (6, 9))], 
        (6, 9): [('LEFT', (6, 8)), ('RIGHT', (6, 10))], 
        (6, 10): [('LEFT', (6, 9)), ('RIGHT', (6, 11))], 
        (6, 11): [('LEFT', (6, 10)), ('RIGHT', (6, 12))], 
        (6, 12): [('LEFT', (6, 11))] }


start = (6, 12)
goal = (6, 5)


queue = deque([("", start)])
print(f"queue: {queue}", file=sys.stderr, flush=True)
visited_2 = set()
while queue:
    print('next step')
    path, current = queue.popleft()
    if current == goal:
        break
    if current in visited_2:
        print(f"current {current[1]} already visited in {visited_2}")
        continue

    visited_2.add(current)
    print(f"path: {path}", file=sys.stderr, flush=True)

    print(f"current node: {current}", file=sys.stderr, flush=True)

    print(f"graph[current]: {graph[current]}", file=sys.stderr, flush=True)
    for direction, neighbour in graph[current]:
        queue.append((path+"," + direction, neighbour))
        print(f"queue: {queue}", file=sys.stderr, flush=True)

print(f"visited_return: {visited_2}", file=sys.stderr, flush=True)
print(f"final path: {path}")


directions = {"L": 'LEFT',"R": 'RIGHT', 'E': 'EAST', 'W' : 'WEST'}







