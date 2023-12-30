import sys
import math

from itertools import zip_longest

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = 5, 2 , 1, 10

#generate two lists of max length and fill with zeros
ways = [light_x - initial_tx , light_y-initial_ty]

lengths = [abs(way) for way in ways]
max_length = max(lengths)


#produce two lists of (-1, 1) possible values
list_x = ['N' if ways[0] < 0 else 'S' for _ in range(lengths[0])]
list_y = ['W' if ways[1] < 0 else 'E' for _ in range(lengths[1])]
#list_x = [-1 if ways[0] < 0 else 1 if ways[0] > 0 for _ in range(lengths[0])]
two_lists = zip_longest(list_x,list_y , fillvalue='')
two_lists = [elt[0]+elt[1] for elt in two_lists]

#moves_x = [-1  if (light_x - initial_tx) < 0 else 1 for _in range(lenght_x)]

# game loop
#while True:
#    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    

    
        
    # Write an action using print
print(f"rrrr {two_lists}", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW

