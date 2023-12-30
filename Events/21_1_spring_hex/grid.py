import collections
import math

m = [{"index":0,"x":0,"y":0,"z":0},{"index":1,"x":1,"y":-1,"z":0},{"index":2,"x":1,"y":0,"z":-1},{"index":3,"x":0,"y":1,"z":-1},{"index":4,"x":-1,"y":1,"z":0},{"index":5,"x":-1,"y":0,"z":1},{"index":6,"x":0,"y":-1,"z":1},
{"index":7,"x":2,"y":-2,"z":0},{"index":8,"x":2,"y":-1,"z":-1},{"index":9,"x":2,"y":0,"z":-2},{"index":10,"x":1,"y":1,"z":-2},{"index":11,"x":0,"y":2,"z":-2},{"index":12,"x":-1,"y":2,"z":-1},{"index":13,"x":-2,"y":2,"z":0},{"index":14,"x":-2,"y":1,"z":1},
{"index":15,"x":-2,"y":0,"z":2},{"index":16,"x":-1,"y":-1,"z":2},{"index":17,"x":0,"y":-2,"z":2},{"index":18,"x":1,"y":-2,"z":1},{"index":19,"x":3,"y":-3,"z":0},{"index":20,"x":3,"y":-2,"z":-1},{"index":21,"x":3,"y":-1,"z":-2},{"index":22,"x":3,"y":0,"z":-3},
{"index":23,"x":2,"y":1,"z":-3},{"index":24,"x":1,"y":2,"z":-3},{"index":25,"x":0,"y":3,"z":-3},{"index":26,"x":-1,"y":3,"z":-2},{"index":27,"x":-2,"y":3,"z":-1},{"index":28,"x":-3,"y":3,"z":0},{"index":29,"x":-3,"y":2,"z":1},{"index":30,"x":-3,"y":1,"z":2},
{"index":31,"x":-3,"y":0,"z":3},{"index":32,"x":-2,"y":-1,"z":3},{"index":33,"x":-1,"y":-2,"z":3},{"index":34,"x":0,"y":-3,"z":3},{"index":35,"x":1,"y":-3,"z":2},{"index":36,"x":2,"y":-3,"z":1}]


_Hex = collections.namedtuple("Hex", ["q", "r", "s"])

def Hex(q, r, s):
    assert not (round(q + r + s) != 0), "q + r + s must be 0"
    return _Hex(q, r, s)

def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)

def parse(dct, idx):
    return Hex( dct[idx]["x"]  , dct[idx]["y"], dct[idx]["z"])

def hex_length(hex):
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2

def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)

def hex_distance(a, b):
    return hex_length(hex_subtract(a, b))

import time

tic = time.perf_counter()



print(hex_distance(parse(m, 0), parse(m, 0)))

toc = time.perf_counter()
print(f"Done in {toc - tic:0.5f} seconds")
