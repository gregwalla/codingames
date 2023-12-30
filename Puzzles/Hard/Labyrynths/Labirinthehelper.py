import sys
from collections import deque

maze0 = ['???????', 
        '?x...x?',      
        '?x...x?',
        '?..T.x?',
        '?....x?',
        '?...Cx?',
        '???????']

maze1 = ['???????', 
         '?xx..x?', 
         '?x...x?',      
         '?x.T.x?',
         '?....x?',
         '?....x?',
         '?...xC?',
         '???????']

maze2 = ['????????', 
         '?x...x.?',      
         '?x...xx?',
         '?....xx?',
         '?....x.?',
         '?...xx.?',
         '????????']

def maze2graph(maze): 
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if maze[i][j] in ['.', 'T', 'C']  }
    for row, col in graph.keys():
        if row < height - 1 and  maze[row + 1][col] in ['.', 'T', 'C'] :
            graph[(row, col)].append(("D", (row + 1, col)))
            graph[(row + 1, col)].append(("U", (row, col)))
        if col < width - 1 and  maze[row][col + 1] in ['.', 'T', 'C'] :
            graph[(row, col)].append(("R", (row, col + 1)))
            graph[(row, col + 1)].append(("L", (row, col)))
    return graph

def find_candidates(graph, maze): 
    candidates = []
    for key in graph.keys() : 
        i = key[0]
        j = key[1]
        if  (maze[i+1][j] == '?' or maze[i-1][j] == '?' or  maze[i][j+1] == '?' or maze[i][j-1] == '?'):
            candidates.append(key)
    return(candidates)

def bfs(graph, start, goal ):
    queue = deque([("", start)])
    visited = set()
    way = str()
    while queue:
        path, current = queue.popleft()
        way = path
        if current == goal:
            break
        elif current in visited:
            continue
        else: 
            visited.add(current)
            for direction, neighbour in graph[current]:
                queue.append((path + direction, neighbour))
    return way

def search_goal(maze):
    goal = tuple()
    for i , row in enumerate(maze) : 
        for j , letter in enumerate(row): 
            if letter == 'C':
                goal = (i, j)
                break
    return goal

def explore_graph(graph, potential_moves, candidates ): 
    move = potential_moves[0][0]
    shortest_length  =  100 #high number
    for potential_move in potential_moves: 
        #print(f'studying move :  {potential_move}')
        for candidate in candidates : 
            #print(f'studying candidate :  {candidate}')
            path = bfs(graph, potential_move[1], candidate )
            if len(path) < shortest_length: 
                shortest_length = len(path)
                move = path[0]
    return move

#######
directions = {"L": 'LEFT',"R": 'RIGHT', 'U': 'UP', 'D' : 'DOWN'}
start_pos = (3,3)
current_pos = (2,3)
moves_left = 4
on_target = False
control_room_activated = False

goal = tuple()

#enter while 

#parse stuff

maze = maze1
#parse current graph
graph = maze2graph(maze)
kirk_position = (3,3)
candidates = find_candidates(graph, maze )
potential_moves = graph[kirk_position]

if not control_room_activated: 

    #if goal not found yet
    if not goal : 
        #see if goal is found
        goal = search_goal(maze)
        #if goal not found
        if not goal : 
            print(f'Goal still not found exploring', file=sys.stderr, flush=True)
            #explore further
            move = explore_graph(graph, potential_moves, candidates )
            print(directions[move])
    
        #if goal is found
        else: 
            if kirk_position != goal : 
                #if you can reach it
                if goal in graph: 
                    #there is a way back 
                    moves_back = bfs(graph, start_pos, goal )
                    if len(moves_back) <= moves_left:
                        print(f'goal found - way back ok - moving to control room', file=sys.stderr, flush=True)
                        #get the way from current position to control room
                        path = bfs(graph, current_pos, goal)
                        move = path[0]
                        print(directions[move])

                    else : 
                        print(f'goal found - but for shorter path', file=sys.stderr, flush=True)
                        #explore further
                        move = explore_graph(graph, potential_moves, candidates )
                        print(directions[move])

            elif kirk_position == goal : 
                print(f"Activating countdown", file=sys.stderr, flush=True)
                control_room_activated == True
                path = bfs(graph, goal, start_pos)
                move = path[0]
                print(directions[move])


elif control_room_activated:
    path = bfs(graph, kirk_position, start_pos)
    move = path[0]
    print(directions[move])
            




