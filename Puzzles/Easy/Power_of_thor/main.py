
import numpy as np

x1 = np.array([2,0])
x2 = np.array([0,  3])
x3 = np.array([4, 7])

ms = [x2 , x3]

def distance(x1, x2):
    """ returns a scalar given an array """
    return   np.sqrt(np.sum((x1 - x2)**2))


def relative_dist(x1, x2):
    """ returns element wise difference starting from first element """
    return x1 - x2

def movement(x):
    """ returns element wise movement
    """
    return np.where(x<0, -1, np.where(x==0, 0, 1))

def add_pos(x1, x2):
    """ returns element wise addition """
    return x1 + x2

def generate_range():
    """ returns 9 positions around zero """
    return np.array([ [[i, j] for j in np.linspace(-1, 1, 3)] for i in np.linspace(-1, 1, 3)])

def potential_pos(x1, rg):
    """ returns 9 positions around position """
    return add_pos(x1, rg)

def in_grid(pos, limits): 
    """ returns a boolean wether position is in grid """
    test = (pos[0] >= 0) & (pos[1] >= 0) & (pos[0] < limits[0]) & (pos[1] < limits[1])
    return test

def check_matrix(grd, grid):
    """ generate a matrix with zero or one wether or not in grid """
    check_mat = np.zeros(shape=(3, 3))
    for i in range(3): 
        for j in range(3): 
            check_mat[i][j] = in_grid(grd[i][j], grid) 
    return check_mat

def manh_dist(x1, x2):
    """ returns element wise difference starting from first element """
    return np.sum(np.abs(x1 - x2))



