import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

beacons = []
connexions = []


number_of_cells = int(input())  # amount of hexagonal cells in this map
for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    neighbours = [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 ]
    if initial_resources > 0 : 
        beacons.append((i, initial_resources) )
    for _ , neigh in enumerate(neighbours):
            connexions.append((i,neigh))

print(f"beacons: {beacons}", file=sys.stderr, flush=True)
print(f"connexions: {connexions}", file=sys.stderr, flush=True)

number_of_bases = int(input())
for i in input().split():
    my_base_index = int(i)
for i in input().split():
    opp_base_index = int(i)



# game loop
while True:
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    statements = ''
    for i , beacon in enumerate(beacons) : 
        statement = f' LINE {my_base_index} {beacons[i][0]} 1 ; ' 
        statements += statement

    print(statements[:-2])
    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    
