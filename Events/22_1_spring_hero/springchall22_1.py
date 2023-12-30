import sys
import math

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

    def __repr__(self):
        rep = f'Point({self.x},{self.y})' 
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

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
base = Point(base_x, base_y)
heroes_per_player = int(input())  # Always 3

# game loop
while True:
    my_monsters = []
    my_heroes = []
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]

        if  _type == 0 and threat_for == 1:
            my_monsters.append(Monster(_id, x, y, vx, vy, health, near_base))
        elif _type == 1 :
            my_heroes.append(Hero(_id, x, y))
        else:
            continue
    
    c_monsters = my_monsters
    c_heroes = my_heroes
        
    
    dist_to_base = []
    dist_to_heroes = []
    for monster in my_monsters: 
        dist_to_base.append(monster.distance(base))
        dist_to_heroes.append(
            [monster.distance(hero.position) for hero in my_heroes])
    print(f'monstersdistbase:{dist_to_base}', file=sys.stderr, flush=True)
    print(f'monsterdisheroes:{dist_to_heroes}', file=sys.stderr, flush=True)

    for i in range(heroes_per_player):
        targets = [Point(1200, 600), Point(1000,1000 ), Point(600,1200)]
        my_heroes[i].move(targets[i])
