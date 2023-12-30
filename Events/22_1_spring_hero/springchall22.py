import sys
import math
import numpy as np

def to_array(x, y):
    return np.array([x,y])

def parseline(v):
    k = ["_id", "_type", "pos", "move","shield_life", "is_controlled", "health",  "near_base", "threat_for"]
    d = dict(zip(k, v))
    return d

TYPE_MONSTER = 0
TYPE_MY_HERO = 1
TYPE_OP_HERO = 2
# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3

# game loop
while True:
    monsters = []
    my_heroes = []
    opp_heroes = []
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        position = Point(x, y)
        direction = Point(vx, vy)
        v = [_id, _type, position,  direction,shield_life, is_controlled, health, near_base, threat_for]
        entity = parseline(v)
        cur_type = entity["_type"]
        if  cur_type == TYPE_MONSTER:
            monsters.append(entity)
        elif cur_type == TYPE_MY_HERO:
            my_heroes.append(entity)
        elif cur_type == TYPE_OP_HERO:
            opp_heroes.append(entity)
        if len(monsters) > 0 :
            print(f'monsters:{monsters}', file=sys.stderr, flush=True)
        #if len(my_heroes) > 0 :
        #    print(f'my_heroes: {my_heroes}', file=sys.stderr, flush=True)
        #if len(opp_heroes) > 0 :
        #    print(f'opp_heroes: {opp_heroes}', file=sys.stderr, flush=True)

    for i in range(heroes_per_player):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        print("WAIT")

closest_hero(my_heroes): 
    closest_hero = my_heroes[0]._id
    if monster.coordinates(closest(my_heroes[0].coordinates,my_heroes[1].coordinates)
        closest_hero = my_heroes[0]._id