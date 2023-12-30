import numpy as np 

raw_lists = {
    'scrap_amount': np.array([
        [ 6.,  8.,  8.,  8.,  8.,  8.,  8., 10.,  8.,  6.,  0.,  0.],
       [ 8.,  6.,  8.,  6.,  9.,  4.,  4.,  9.,  0.,  4.,  8.,  8.],
       [ 0.,  8., 10.,  4.,  8.,  6.,  8.,  8.,  8., 10.,  1.,  8.],
       [ 8.,  1., 10.,  8.,  8.,  8.,  6.,  8.,  4., 10.,  8.,  0.],
       [ 8.,  8.,  4.,  0.,  9.,  4.,  4.,  9.,  6.,  8.,  6.,  8.],
       [ 0.,  0.,  6.,  8., 10.,  8.,  8.,  8.,  8.,  8.,  8.,  6.]]), 
    'owner': np.array([
        [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
       [-1., -1., -1., -1., -1., -1., -1., -1., -1.,  0., -1., -1.],
       [-1., -1.,  1., -1., -1., -1., -1., -1.,  0.,  0.,  0., -1.],
       [-1.,  1.,  1.,  1., -1., -1., -1., -1., -1.,  0., -1., -1.],
       [-1., -1.,  1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
       [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.]]), 
    'units': np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), 
    'recycler': np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), 
    'can_bulid': np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), 
    'can_spawn': np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), 
    'in_range_of_recycler': np.array([
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]),
       }


my_tiles = np.where(raw_lists["owner"] == 1)
my_coords = [(my_tiles[0][i], my_tiles[1][i]) for i in range(len(my_tiles[0]))]

op_tiles = np.where(raw_lists["owner"] == 0) # move towards opp tiles

print(my_coords)



# def sum_around(nparray, i,j ) : 

    
    
#     height = nparray.shape[0]
#     width = nparray.shape[1]

#     if nparray[i][j] == 0 : 
#         score = 0

#     elif i > 0 and i < height and j > 0 and j < width : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i+1][j] + nparray[i][j-1] + nparray[i][j+1] 
    
#     elif i == 0 and j > 0 and j < width : 
#         score = nparray[i][j] + nparray[i+1][j] + nparray[i][j-1] + nparray[i][j+1]
#     elif i == height and j > 0 and j < width : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i][j-1] + nparray[i][j+1] 

#     elif i > 0 and i < height and j ==  0 : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i+1][j] + nparray[i][j+1]
#     elif i > 0 and i < height and j == width : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i+1][j] + nparray[i][j-1] 

#     elif i == 0 and j ==  0 : 
#         score = nparray[i][j] + nparray[i+1][j] + nparray[i][j+1] 
#     elif i == height and j ==  width : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i][j-1] 
#     elif i == height and j ==  0 : 
#         score = nparray[i][j] + nparray[i-1][j] + nparray[i][j+1] 
#     elif i == 0 and j ==  width : 
#         score = nparray[i][j] + nparray[i][j-1] + nparray[i+1][j] 
    
#     return score


def sum_around(nparray):
    padded_array = np.pad(nparray, pad_width=1, mode='constant', constant_values=0)
    u_array = np.pad(padded_array[1:, :], pad_width=((0,1),(0,0)), mode='constant', constant_values=0 )
    d_array = np.pad(padded_array[:-1, :], pad_width=((1,0),(0,0)), mode='constant', constant_values=0 )
    l_array = np.pad(padded_array[:, 1:], pad_width=((0,0),(0,1)), mode='constant', constant_values=0 )
    r_array = np.pad(padded_array[:, :-1], pad_width=((0,0),(1,0)), mode='constant', constant_values=0 )
    s_array = padded_array + u_array+ d_array + l_array + r_array
    result = s_array[1:-1,1:-1]
    return result


mtrx = sum_around(raw_lists['scrap_amount'])
print(mtrx*raw_lists['can_bulid' ])