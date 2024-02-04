import sys
import math
import numpy as np

######################

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Unit(Point) :
    def __init__(self, x, y, id, r, vx, vy):
        super().__init__(x, y)
        self.id = id
        self.r = r
        self.vx = vx
        self.vy = vy

class Checkpoint(Unit): 
    def __init__(self, x, y, id, r, vx, vy):
        super().__init__(x, y, id, r, vx, vy)



class Pod(Unit):

    def __init__(self, x, y, id, r, vx, vy, angle = None, nextCheckpointId = None, checked = None, timeout = None, partner = None, shield = None):
        super().__init__(x, y, id, r, vx, vy)
        self.angle = angle
        self.nextCheckpointId  = nextCheckpointId 
        self.checked = checked
        self.timeout = timeout
        self.partner = partner
        self.shield = shield

    def move(self, t):
        
        self.x += self.vx * t
        self.y += self.vy * t



#######################



p1 = Pod(0, 0, 1 , 400, 0, 0 )
p2 = Pod(0, 0, 2 , 400, 0, 0 )

t = 0

checkpoints = []
checkpoint_units = []


# game loop
while True:
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    t += 1
    p1.x, p1.y = x, y
    p1.vx, p1.vy =   x - p1.vx , y - p1.vy
    p2.x , p2.y = opponent_x , opponent_y
    p2.vx , p2.vy = opponent_x - p2.x, opponent_y - p2.y
    
    checkpoint_pos = (next_checkpoint_x,next_checkpoint_y)
    if checkpoint_pos not in checkpoints: 
        checkpoints.append(checkpoint_pos)
        idx = checkpoints.index(checkpoint_pos) + 1
        checkpoint_units.append(Checkpoint(checkpoint_pos[0],checkpoint_pos[1],  idx , 600, 0,0) )

    idx = checkpoints.index(checkpoint_pos) 
    print(f't: {t}, going to : {checkpoint_units[idx].id}, angle: {next_checkpoint_angle}', file=sys.stderr, flush=True)

    # # You have to output the target position
    # # followed by the power (0 <= thrust <= 100)
    # # i.e.: "x y thrust"

    if next_checkpoint_angle > 45 or next_checkpoint_angle < -40 :
        thrust = 0
    else :
        thrust = 100


    print(f"{str(next_checkpoint_x)} {str(next_checkpoint_y)} {thrust}")
