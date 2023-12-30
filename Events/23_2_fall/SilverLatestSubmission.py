from typing import List, NamedTuple, Dict
import math
import numpy as np
import sys

testing = False
############################################################################################################
# Define input functions: 
############################################################################################################

def get_fish_details(fish_details, verbose: bool = False ):
    
    fish_count = int(input())
    for _ in range(fish_count):
        fish_id, color, _type = map(int, input().split())
        fish_details[fish_id] = FishDetail(color, _type)
    if verbose:
        print(f"fish_details: {fish_details} ", file=sys.stderr, flush=True)    
    return fish_details


def get_scores(verbose: bool = False):
    my_score = int(input())
    foe_score = int(input())

    if verbose:
        print(f'my_score: {my_score} foe sc.{ foe_score}', file=sys.stderr, flush=True)
    
    return my_score, foe_score

def get_my_scans(verbose: bool = False):
    my_scans: List[int] = []
    my_scan_count = int(input())
    for _ in range(my_scan_count):
        fish_id = int(input())
        my_scans.append(fish_id)
    if verbose:
        print(f"my_scans: {my_scans} ", file=sys.stderr, flush=True)
    
    return my_scans
    
def get_foe_scans(verbose: bool = False):
    foe_scans: List[int] = []
    foe_scan_count = int(input())
    for _ in range(foe_scan_count):
        fish_id = int(input())
        foe_scans.append(fish_id)
    if verbose:
        print(f"foe_scans: {foe_scans} ", file=sys.stderr, flush=True)

    return foe_scans

def get_my_drones(verbose: bool = False):

    my_drones: List[Drone] = []

    my_drone_count = int(input())

    for _ in range(my_drone_count):
        drone_id, drone_x, drone_y, dead, battery = map(int, input().split())
        pos = Vector(drone_x, drone_y)
        drone = Drone(drone_id, pos, dead == '1', battery, [])
        drone_by_id[drone_id] = drone
        my_drones.append(drone)

        my_radar_blips[drone_id] = []

    if verbose:
        print(f"my_drones: {my_drones} ", file=sys.stderr, flush=True)
    
    return my_drones

def get_foe_drones(verbose: bool = False):
    foe_drones: List[Drone] = []
    foe_drone_count = int(input())
    
    for _ in range(foe_drone_count):
        drone_id, drone_x, drone_y, dead, battery = map(int, input().split())
        pos = Vector(drone_x, drone_y)
        drone = Drone(drone_id, pos, dead == '1', battery, [])
        drone_by_id[drone_id] = drone
        foe_drones.append(drone)
    if verbose:
        print(f"foe_drones: {foe_drones} ", file=sys.stderr, flush=True)

    return foe_drones

def add_drone_scans(drone_by_id, verbose: bool = False):
    drone_scan_count = int(input())
    for _ in range(drone_scan_count):
        drone_id, fish_id = map(int, input().split())
        drone_by_id[drone_id].scans.append(fish_id)
    if verbose:
        print(f"drones_by_id: {drone_by_id} ", file=sys.stderr, flush=True)

    return drone_by_id

def get_visible_fish(verbose: bool = False):
    visible_fish: List[Fish] = []

    visible_fish_count = int(input())

    for _ in range(visible_fish_count):
        fish_id, fish_x, fish_y, fish_vx, fish_vy = map(int, input().split())
        pos = Vector(fish_x, fish_y)
        speed = Vector(fish_vx, fish_vy)
        visible_fish.append(Fish(fish_id, pos, speed, fish_details[fish_id]))
    if verbose:
        print(f"visible_fish: {visible_fish} ", file=sys.stderr, flush=True)
    
    return visible_fish


def get_my_radar_blips(my_radar_blips, verbose: bool = False ):
    
    my_radar_blip_count = int(input())
    
    for _ in range(my_radar_blip_count):
        drone_id, fish_id, dir = input().split()
        drone_id = int(drone_id)
        fish_id = int(fish_id)
        my_radar_blips[drone_id].append(RadarBlip(fish_id, dir))
    if verbose:
        print(f"my_radar_blips: {my_radar_blips} ", file=sys.stderr, flush=True)

    return my_radar_blips

############################################################################################################
# Define the data structures :
############################################################################################################
class Vector(NamedTuple):
    x: int
    y: int

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def divide(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def multiply(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def normalize(self):
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        if magnitude == 0:
            return (0, 0)
        return (self.x / magnitude, self.y / magnitude)

    def distance(self, other):
        return round(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2))


class FishDetail(NamedTuple):
    color: int
    type: int

class Fish(NamedTuple):
    fish_id: int
    pos: Vector
    speed: Vector
    detail: FishDetail

class RadarBlip(NamedTuple):
    fish_id: int
    dir: str

class Drone(NamedTuple):
    drone_id: int
    pos: Vector
    dead: bool
    battery: int
    scans: List[int]




############################################################################################################
# Define the game functions
############################################################################################################
    
# Function to calculate distance
def calculate_distance(point1: Vector, point2: Vector) -> float:
    return int(math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2))

# Function to find the next closest point
def find_closest(drone_position: Vector, points: List[Vector], flags: List[bool]) -> int:
    min_distance: float = float('inf')
    min_index: int = -1
    for i in range(len(points)):
        if not flags[i]:
            distance: float = calculate_distance(drone_position, points[i])
            if distance < min_distance:
                min_distance = distance
                min_index = i
    return min_index


def flee(drone_position: Vector, boundary: Vector, monsters_list: List[Fish]) -> Vector:
    max_distance = 600  # Maximum distance the drone can move in one turn

    # Handle the case where the monster will reach the drone in the next turn
    for monster in monsters_list:
        if monster.pos.x + monster.speed.x == drone_position.x and monster.pos.y + monster.speed.y == drone_position.y :

            dangerous_monster = monster

        else:
            dangerous_monster = None
            # Calculate the opposite direction of the monster's speed


        if dangerous_monster is not None:
            flee_position = drone_position.add(dangerous_monster.speed)
            print(f"Dangerous monster: {flee_position}", file=sys.stderr, flush=True)
            #adjust flee position
            # Move up for the remaining of the move (60 units)
            if monster.pos.y > drone_position.y: #monster is below drone
                flee_position = flee_position.add(Vector(0,- 60)) #move further up
                print(f"monster below - moving up: {flee_position}", file=sys.stderr, flush=True)
            elif monster.pos.y < drone_position.y: #monster is above drone
                if monster.pos.x < drone_position.x : #monster is above drone and to the left
                    flee_position = flee_position.add(Vector(60, 0)) #move right
                    print(f"monster above left - moving down - right: {flee_position}", file=sys.stderr, flush=True)
                else: #monster is above drone and to the right or at same longitude
                    flee_position = flee_position.add(Vector(-60, 0))  #move left
                    print(f"monster above right - moving down - left: {flee_position}", file=sys.stderr, flush=True)
            else:
                flee_position = flee_position.multiply(1.1)
                print(f"Moving opposite: {flee_position}", file=sys.stderr, flush=True)
        
        elif dangerous_monster is None:
            print(f"No dangerous monster", file=sys.stderr, flush=True)
            max_distance = 600  # Maximum distance the drone can move in one turn
            
            # Calculate the average (barycenter) of the monsters' coordinates
            average_x = int(sum(monster.pos.x + monster.speed.x for monster in monsters_list) / len(monsters_list))
            average_y = int(sum(monster.pos.y + monster.speed.y for monster in monsters_list) / len(monsters_list))

            # Calculate the direction vector from the average position to the drone position
            direction_vector = Vector(drone_position.x - average_x, drone_position.y - average_y)
            #print(f"direction vector: {direction_vector}", file=sys.stderr, flush=True)
            # Normalize the direction vector
            direction_magnitude = calculate_distance(drone_position, Vector(average_x, average_y))
            print(f"direction_magnitude: {direction_magnitude}", file=sys.stderr, flush=True)
            normalized_direction = [direction_vector.x / direction_magnitude, direction_vector.y / direction_magnitude]
            print(f"normalized_direction: {normalized_direction}", file=sys.stderr, flush=True)
            
            # Calculate the farthest position based on the maximum distance the drone can move
            flee_position = Vector(int(drone_position.x + normalized_direction[0] * max_distance),
                                    int(drone_position.y + normalized_direction[1] * max_distance))
            

        # Handle bouncing off the map borders if the farthest position exceeds the boundaries
        if flee_position.x < 0:
            flee_position = flee_position._replace(x=abs(flee_position.x))
        elif flee_position.x > boundary.x:
            flee_position = flee_position._replace(x=2 * boundary.x - flee_position.x)
        if flee_position.y < 0:
            flee_position = flee_position._replace(y=abs(flee_position.y))
        elif flee_position.y > boundary.y:
            flee_position = flee_position._replace(y=2 * boundary.y - flee_position.y)

        return flee_position

############################################################################################################
# Define the game variables
############################################################################################################
    
# Define the points
points: List[Vector] = [Vector(2000, 2500), Vector(2000, 5000), Vector(2000, 8000), Vector(5000, 8000),
                        Vector(5000, 5000), Vector(5000, 2500), Vector(8000, 2500), Vector(8000, 5000),
                        Vector(8000, 8000)]

boundary = Vector(10000, 10000)

#flags: List[bool] = [False] * len(points)  # Initialize flags
flags_1 : List[bool] = [False] * len(points)
flags_2 : List[bool] = [False] * len(points)
flags = [flags_1, flags_2]


############################################################################################################

if not testing :

    fish_details: Dict[int, FishDetail] = {}
    fish_details = get_fish_details(fish_details, verbose = True)

    #first_turn = True
    ############################################################################################################
    # game loop
    ############################################################################################################
    while True:

        drone_by_id: Dict[int, Drone] = {}
        my_radar_blips: Dict[int, List[RadarBlip]] = {}
        

        my_score, foe_score = get_scores(verbose = True)
        my_scans = get_my_scans(verbose = True)
        foe_scan = get_foe_scans(verbose = True)
        my_drones = get_my_drones(verbose = True)
        foe_drones = get_foe_drones(verbose = True)
        drone_by_id = add_drone_scans(drone_by_id, verbose = True)
        visible_fish = get_visible_fish(verbose = True)
        my_radar_blips = get_my_radar_blips(my_radar_blips, verbose =True )
        


        # isolate monsters:
        # Create a list of monsters including their details 
        monster_creatures = [fish for fish in visible_fish if fish.detail.type == -1]
        # if verbose:
        #print(f"monster_creatures: {monster_creatures} ", file=sys.stderr, flush=True)
        
        threshold_distance = 1640

        for i, drone in enumerate(my_drones):
            print(f"drone: {drone} ", file=sys.stderr, flush=True)

            moved = False

            if len(monster_creatures) > 0:
                distances_to_monsters = [calculate_distance(drone.pos, monster_creature.pos) for monster_creature in monster_creatures]
                #print(f"distances_to_monsters: {distances_to_monsters} ", file=sys.stderr, flush=True)
                threatening_monsters = [monster_creature for monster_creature, distance in zip(monster_creatures, distances_to_monsters) if distance < threshold_distance]
                #print(f"threatening_monsters: {threatening_monsters}", file=sys.stderr, flush=True)
                
                if len(threatening_monsters) > 0:
                    farthest_position = flee(drone.pos, boundary, threatening_monsters)
                    #print(f"farthest_position: {farthest_position}", file=sys.stderr, flush=True)
                    print(f"MOVE {farthest_position.x} {farthest_position.y} {0} FLEING")
                    #print(f"drone: {drone.drone_id}, flew: x:{farthest_position.x} y: {farthest_position.y}", file=sys.stderr, flush=True)
                    
                    moved = True

            if moved == False :
                if False in flags[i] : 
                    
                # Find the closest point
                    closest_point_index: int = find_closest(drone.pos, points, flags[i])

                    # Check if the drone reaches the point or it's the initial move
                    if calculate_distance(drone.pos, points[closest_point_index]) <= 600:
                        
                        drone = drone._replace(pos=points[closest_point_index])
                        flags[i][closest_point_index] = True
                        light = 1
                        
                        print(f"MOVE {points[closest_point_index].x} {points[closest_point_index].y} {light} SCANNING")

                    else:
                        
                        direction_vector = points[closest_point_index].subtract(drone.pos)
                        normalized_direction = direction_vector.divide(np.linalg.norm(direction_vector))
                        drone = drone._replace(pos=Vector(drone.pos.x + 600 * normalized_direction.x, 
                                                        drone.pos.y + 600 * normalized_direction.y))
                        light = 0

                        print(f"MOVE {points[closest_point_index].x} {points[closest_point_index].y} {light} EXPLORING")
                
                else: 
                    
                    print(f"MOVE {5000} {500} {0} SURFACE")

