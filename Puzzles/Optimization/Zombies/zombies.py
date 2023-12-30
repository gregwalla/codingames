# while there is some time left
#     generate a random strategy
#     simulate the strategy
# apply the first move of the best strategy seen so far

# A strategy is :

# repeat X times (X chosen randomly between 0 and 3)
#     move to a random position
# for each zombie still alive (the order of the zombies is also chosen randomly)
#     move toward the zombie until he's killed


import time
import random

x_m = 16000
y_m = 9000
max_range = 1000

max_simul = 3
max_moves = 5

humans = 2
zombies_killed = 3


def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
f = fib()

def fibo(n):
    f = fib()
    for i in range(n): 
        r = next(f)
    return r

def score(humans,zombies_killed ):
    return humans*humans*10*fibo(zombies_killed)


def random_move(range: int): 
    """Generate a move of length no more than max range
    """
    x = random.randint(-range,range)
    y = random.randint(-range,range)

    while (x*x + y*y) >= range*range : 
        print(f"(x,y) : {x,y} , recalculating")
        x = random.randint(-range,range)
        y = random.randint(-range,range)

    return (x,y)


def valid_move(func, func_arg, pos, x_m, y_m): 

    """Generate a valid move of length no more than max range
    """
    assert x_m >= 0 
    assert y_m >= 0 
    assert pos[0] >= 0 
    assert pos[1] >= 0 
    assert pos[0] <= x_m
    assert pos[1] <= y_m 

    #initialize
    move = func(func_arg)
    test_pos = (pos[0]+move[0], pos[1]+ move[1])
    in_frame =  ( 0 <= test_pos[0] <= x_m) and ( 0 <= test_pos[1] <= y_m)

    while not in_frame:
        
        move = func(func_arg)
        test_pos = (pos[0]+move[0], pos[1]+ move[1]) 
        in_frame =  ( 0 <= test_pos[0] <= x_m) and ( 0 <= test_pos[1] <= y_m)

    return test_pos

t0 = time.perf_counter()
for j in range(max_simul): 

    print(f"simul: {j}")
    #initialize simulation
    pos = (4200,2100)
    moves = list()
    scores = list()

    t0_0 = time.perf_counter()

    for i in range(max_moves): 
        ##
        pos = valid_move(random_move, max_range, pos, x_m, y_m)
        moves.append(pos)
        scores.append(score(humans, zombies_killed))
        print(f"move: {i}, pos: {moves}, scores: {scores}")

    t0_1 = time.perf_counter()

    print(f"simul: {j} Done in {t0_1 - t0_0:0.4f} seconds")



