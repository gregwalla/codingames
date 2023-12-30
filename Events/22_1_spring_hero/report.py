import sys
import math


def offset(p,  top_base ):
    offset = (450, 50)
    if p.in_a() and top_base:
        return Point(p.x + offset[0],p.y - offset[1] ) 
    elif p.in_a() and not top_base: 
        return Point(p.x-offset[0], p.y-offset[1])
    elif p.in_b() and top_base:
        return Point(p.x + offset[0], p.y+ offset[1]) 
    elif p.in_b() and not top_base: 
        return Point(p.x-offset[0], p.y - offset[0])


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
        if (self.x > 4100) and (self.y < 6000) : 
            return True
        else:
            return False

    def in_b(self): 
        if (self.x < 14000) and (self.y > 3500) : 
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

    def distance(self, p) :
        return self.position.distance(p)


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
    targets = [monster.position for monster in my_monsters]

    regroup = [Point(1800, 4200), Point(3500, 2500), Point(4300,1000)]
    if not top_base: 
        regroup = [
            Point(13000, 7000), Point(14000, 6000), Point(15500,4500)]

    print(f'targets: {targets}', file=sys.stderr, flush=True)

    if len(my_monsters) == 0:
        my_heroes[0].move(regroup[1])
        my_heroes[1].move(regroup[0])
        my_heroes[2].move(regroup[2])

    if len(my_monsters) == 1: 
        for monster in my_monsters : 
            distances =  [monster.distance(hero.position) for hero in my_heroes]
            val, idx = min((val, idx) for (idx, val) in enumerate(distances))
            closest_hero = my_heroes[idx]
            my_heroes.remove(closest_hero)
            cond1 = (monster.position.in_a() or monster.position.in_b())
            cond2 = (val < 2000)
            cond3 = (my_mana >= 10)
            print(f'hero: {closest_hero}, monster: {monster}, val : {val}', file=sys.stderr, flush=True)
            if cond1 and cond2 and cond3  :
                closest_hero.control(monster, offset(monster.position, top_base))
            else : 
                closest_hero.move(monster.position)

        my_heroes[0].move(regroup[0])
        my_heroes[1].move(regroup[2])

    if len(my_monsters) == 2: 
        for monster in my_monsters : 
            distances =  [monster.distance(hero.position) for hero in my_heroes]
            val, idx = min((val, idx) for (idx, val) in enumerate(distances))
            closest_hero = my_heroes[idx]
            my_heroes.remove(closest_hero)
            cond1 = (monster.position.in_a() or monster.position.in_b())
            cond2 = (val < 2000)
            cond3 = (my_mana >= 10)
            print(f'closest hero: {closest_hero}, for monster: {monster}, val : {val}', file=sys.stderr, flush=True)
            if cond1 and cond2 and cond3  :
                closest_hero.control(monster, offset(monster.position, top_base))
            else : 
                closest_hero.move(monster.position)

        my_heroes[0].move(my_monsters[-1].position)



    if len(my_monsters) >= 3: 
        for monster in my_monsters[:3] : 
            distances =  [monster.distance(hero.position) for hero in my_heroes]
            val, idx = min((val, idx) for (idx, val) in enumerate(distances))
            closest_hero = my_heroes[idx]
            my_heroes.remove(closest_hero)
            cond1 = (monster.position.in_a() or monster.position.in_b())
            cond2 = (val < 2000)
            cond3 = (my_mana >= 10)
            print(f'hero: {closest_hero}, monster: {monster}, val : {val}', file=sys.stderr, flush=True)
            if cond1 and cond2 and cond3  :
                closest_hero.control(monster, offset(monster.position, top_base))
            else : 
                closest_hero.move(monster.position)

