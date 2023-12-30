
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
    def __init__(self, _id, x, y):
        self._id = _id
        self.position  = Point(x, y)


    
    def __repr__(self):
        rep = f'M:({self._id},P: {self.position})' 
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


h1 = Hero('thor', 1,2)
h2 = Hero('conan', 3,5000)

m1 = Monster('blob',3,6000 )
m2 = Monster('gor',4,5500)
m3 = Monster('rfo',1000000,1 )

my_heroes = [h1 ,h2]
my_monsters = [m1, m2, m3]

my_mana = 100
top_base = True


for hero in my_heroes : 
    distances =  [hero.distance(monster.position) for monster in my_monsters]
    val, idx = min((val, idx) for (idx, val) in enumerate(distances))
    closest_monster = my_monsters[idx]
    my_monsters.remove(closest_monster)

    cond1 = (closest_monster.position.in_a() or closest_monster.position.in_b())
    cond2 = (val < 2200)
    cond3 = (my_mana >= 10)
    #print(f'hero: {hero}, monster: {closest_monster}, val : {val}')
    if cond1 and cond2 and cond3  :
        hero.control(closest_monster, offset(closest_monster.position, top_base))
    else : 
        hero.move(closest_monster.position)
    