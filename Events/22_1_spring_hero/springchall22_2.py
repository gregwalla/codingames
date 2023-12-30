import sys
import math


def offset(p,  top_base ):
    offset = (200, 100)
    if p.in_a() and top_base:
        return Point(p.x + offset[0],p.y - offset[1] ) 
    elif p.in_a() and not top_base: 
        return Point(p.x-offset[0], p.y)
    elif p.in_b() and top_base:
        return Point(p.x + offset[0], p.y) 
    elif p.in_b() and not top_base: 
        return Point(p.x-offset[0], p.y - offset[1])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance2(self, p): 
        return (self.x - p.x)*(self.x - p.x) + (self.y - p.y)*(self.y - p.y)

    def distance(self, p): 
        return math.sqrt(self.distance2(p))

    def closest(self, p1, p2): 
        if self.distance2(p1)>= self.distance2(p2):
            return p2
        else:
            return p1

    def in_a(self): 
        if (self.x > 5000) and (self.y < 5000) : 
            return True
        else:
            return False

    def in_b(self): 
        if (self.x < 12850) and (self.y > 5000) : 
            return True
        else:
            return False

    def __repr__(self):
        rep = f"Point({self.x},{self.y}), in_a: {str(self.in_a())}, in_b: {str(self.in_b())}" 
        return rep

class Monster: 
    def __init__(self, _id, x, y, vx, vy, health, near_base):
        self._id = _id
        self.position  = Point(x, y)
        self.nextpos = Point(vx, vy)
        self.health = health
        self.near_base = near_base
    
    def __repr__(self):
        rep = f'M:({self._id},P: {self.position}, N: {self.nextpos}, H:{self.health}, NB:{self.near_base})' 
        return rep
    
    def distance(self, p) :
        return self.position.distance(p)

    def closest_hero(self, my_heroes): 
        closest_hero = 0
        if self.distance(my_heroes[0].position) > self.distance(my_heroes[1].position): 

            closest_hero = 1
        if self.distance(my_heroes[1].position) > self.distance(my_heroes[2].position)   
            close = 2
        if self.distance(my_heroes[1].position) > self.distance(my_heroes[2].position) 
        


class Hero: 
    def __init__(self, _id, x, y):
        self._id = _id
        self.position  = Point(x, y)

    def __repr__(self):
        rep = f'H:({self._id},P: {self.position})' 
        return rep


    @staticmethod
    def move(p):
        print(f'MOVE {p.x} {p.y}')

    @staticmethod
    def control(target, p):
        print(f'SPELL CONTROL  {target._id} {p.x} {p.y}')


def sort_list(lst): 
    indices = list(range(len(lst)))
    indices.sort(key=lambda x: lst[x])
    output = [0] * len(indices)
    for i, x in enumerate(indices):
        output[x] = i
    return output


# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
base = Point(base_x, base_y)
heroes_per_player = int(input())  # Always 3
top_base = True
if base_x > 5000: 
    top_base = False
# game loop

while True:
    my_monsters = []
    my_heroes = []

        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
    my_health, my_mana = [int(j) for j in input().split()]
    op_health, op_mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]

        if  _type == 0 and threat_for == 1:
            my_monsters.append(Monster(_id, x, y, vx, vy, health, near_base))
        elif _type == 1 :
            my_heroes.append(Hero(_id, x, y))
        else:
            continue
    
    dist_to_base = []
    dist_to_heroes = []

    for monster in my_monsters: 
        dist_to_base.append(monster.distance(base))
        dist_to_heroes.append(
            [monster.distance(hero.position) for hero in my_heroes])

    #print(f'monstersdistbase:{dist_to_base}', file=sys.stderr, flush=True)
    #print(f'monsterdisheroes:{dist_to_heroes}', file=sys.stderr, flush=True)
    targets = [monster.position for monster in my_monsters[:3]]

    regroup = [Point(1000, 800), Point(3000, 4500), Point(5600,2000)]
    if not top_base: 
        regroup = [Point(17000, 8400), Point(12500, 7000), Point(15000,4000)]

    if len(targets) == 0: 
        my_heroes[0].move(regroup[0])
        my_heroes[1].move(regroup[1])
        my_heroes[2].move(regroup[2])

    elif len(targets) == 1: 
        offst = offset(targets[0], top_base )
        print(f'target: {targets[0]},offst: {offst} top_base: {top_base}', file=sys.stderr, flush=True)

        my_heroes[0].move(targets[0])
        my_heroes[1].move(targets[0])
        my_heroes[2].move(regroup[0])
    
    elif len(targets) == 2: 

        my_heroes[0].move(targets[0])
        my_heroes[1].move(targets[0])
        my_heroes[2].move(targets[1])

    else : 
        for i, target in enumerate(targets[:3]) : 
            if (target.in_a() or target.in_b()) and my_mana > 10 : 
                print(f'trying to control : {target} to: {offset(target, top_base)}',file=sys.stderr, flush=True)
                try : 
                    my_heroes[i].control(target, offset(target, top_base))
                except  : 
                    break
            else : 
                my_heroes[i].move(target)


        
