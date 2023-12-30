import sys

connected_candidates =   [
    ((4, 8), 'LLLLLLDDRRRRRRDR'), 
    ((6, 8), 'LLLLLLDDDDDDDRRRRRRRUU'), 
    ((7, 8), 'LLLLLLDDDDDDDRRRRRRRU'), 
    ((8, 8), 'LLLLLLDDDDDDDRRRRRRR'), 
    ((1, 9), 'RR'), 
    ((3, 9), 'LLLLLLDDRRRRRRRR')]

directions = {"L": 'LEFT',"R": 'RIGHT', 'U': 'UP', 'D' : 'DOWN'}


def closest_move(connected_candidates): 
#takes a list of tuples as input 
    move = connected_candidates[0][1][0]
    closest_dist = len(connected_candidates[0][1])
    for candidate in connected_candidates[1:]: 
        current_dist = len(candidate[1])
        if current_dist <= closest_dist  :
            closest_dist = current_dist
            move = candidate[1][0]
    print(f'closest move: {move}', file=sys.stderr, flush=True)
    return move

move = closest_move(connected_candidates)

print(directions[move])
    