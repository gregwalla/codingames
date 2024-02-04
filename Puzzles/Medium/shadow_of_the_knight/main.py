import sys

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"
    
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def update(self, x, y):
        self.x = x
        self.y = y

class SearchLimits:
    def __init__(self, right, down):
        self.left_most = 0
        self.right_most = right
        self.up_most = 0
        self.down_most = down
    
    def __repr__(self) -> str:
        return f"left: {self.left_most}, right: {self.right_most}, up: {self.up_most}, down: {self.down_most}"
    

    def update(self, pos,  direction):
        if 'L' in direction:
            self.right_most = pos.x-1
        elif 'R' in direction:
            self.left_most = pos.x+1
        if 'U' in direction:
            self.down_most = pos.y - 1
        elif 'D' in direction:
            self.up_most = pos.y + 1
    


w, h = map(int, input().split())
search_limits = SearchLimits(w, h)
n = int(input())
x, y = map(int, input().split())
pos = Position(x, y)
print(f"pos: {pos}", file=sys.stderr, flush=True)

print(f"search_limits: {search_limits}", file=sys.stderr, flush=True)


# game loop
while True:

    bomb_dir = input()
    print(f"bomb_dir: {bomb_dir}", file=sys.stderr, flush=True)
    search_limits.update(pos, bomb_dir)
    print(f"search_limits: {search_limits}", file=sys.stderr, flush=True)
    next_x = (search_limits.left_most + search_limits.right_most) // 2
    next_y = (search_limits.up_most + search_limits.down_most) // 2


    pos.update(next_x, next_y)

    print(f"{pos.x} {pos.y}")

