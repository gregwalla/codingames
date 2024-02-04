import sys

class Lander:
    def __init__(self, x, y, h_speed, v_speed, fuel, rotate, power):
        self.x = x
        self.y = y
        self.h_speed = h_speed
        self.v_speed = v_speed
        self.fuel = fuel
        self.rotate = rotate
        self.power = power

    def get_rotation(self):
        return str(-20)

    def get_power(self):
        return str(3)
    
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, h_speed: {self.h_speed}, v_speed: {self.v_speed}, fuel: {self.fuel}, rotate: {self.rotate}, power: {self.power}"





def read_surface_points():
    # ex : [(0, 100), (1000, 500), (1500, 100), (3000, 100), (5000, 1500), (6999, 1000)]
    surface_n = int(input())  # the number of points used to draw the surface of Mars.
    print(f"surface_n: {surface_n}", file=sys.stderr, flush=True)
    surface_points = []
    for _ in range(surface_n):
        land_x, land_y = [int(j) for j in input().split()]
        surface_points.append((land_x, land_y))
    print(f"{surface_points}", file=sys.stderr, flush=True)
    return surface_points

def find_first_landing_zone(surface_points):
    for i in range(len(surface_points) - 1):
        if surface_points[i][1] == surface_points[i+1][1]:
            print(f"landing_zone: {surface_points[i]} {surface_points[i+1]}", file=sys.stderr, flush=True)
            return surface_points[i], surface_points[i+1]
    
    return None

def calculate_target(landing_zone):
    target = ((landing_zone[0][0] + landing_zone[1][0]) // 2 , landing_zone[0][1])
    print(f"target: {target}", file=sys.stderr, flush=True)
    return target

def find_path_to_target(lander, target):
    path_to_target = (target[0] - lander.x, target[1] - lander.y)
    print(f"path to target: {target}", file=sys.stderr, flush=True)
    return path_to_target


def main_loop():
    while True:
        x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        lander = Lander(x, y, h_speed, v_speed, fuel, rotate, power)
        print(lander, file=sys.stderr, flush=True)

        rotation = lander.get_rotation()
        thrust_power = lander.get_power()
        print(f"{rotation} {thrust_power}")

if __name__ == "__main__":
    surface_points = read_surface_points()
    landing_zone = find_first_landing_zone(surface_points)
    target = calculate_target(landing_zone)
    main_loop()
