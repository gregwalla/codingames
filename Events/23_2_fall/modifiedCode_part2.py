
#######################
#part2
#######################

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


    


#################

if not testing :

    ############################
    # Define the game variables:
    ############################

    # Define the points
    points: List[Vector] = [Vector(2000, 2500), Vector(2000, 5000), Vector(2000, 8000), Vector(5000, 8000),
                            Vector(5000, 5000), Vector(5000, 2500), Vector(8000, 2500), Vector(8000, 5000),
                            Vector(8000, 8000)]

    boundary = Vector(10000, 10000)

    #flags: List[bool] = [False] * len(points)  # Initialize flags
    flags_1 : List[bool] = [False] * len(points)
    flags_2 : List[bool] = [False] * len(points)
    flags = [flags_1, flags_2]

    min_fishes_scanned = 3

    fish_details: Dict[int, FishDetail] = {}
    fish_details = get_fish_details(fish_details, verbose = True)
    my_states = {}
    Turn = 0
    threshold_distance = 1640


    #############
    # game loop
    #############
    while True:

        #############
        # Parse the input
        #############
        

        drone_by_id: Dict[int, Drone] = {}
        my_radar_blips: Dict[int, List[RadarBlip]] = {}
        

        my_score, foe_score = get_scores(verbose = False)
        my_scans = get_my_scans(verbose = False)
        foe_scans = get_foe_scans(verbose = False)
        my_drones = get_my_drones(verbose = False)
        # my_drones: [
        #     Drone(drone_id=0, pos=Vector(x=2994, y=5734), dead=False, battery=30, scans=[]), 
        #     Drone(drone_id=2, pos=Vector(x=380, y=7249), dead=False, battery=29, scans=[])] 
        foe_drones = get_foe_drones(verbose = True)
        drone_by_id = add_drone_scans(drone_by_id, verbose = True)
        # Example of drones_by_id : 
        # drones_by_id: {
        #     0: Drone(drone_id=0, pos=Vector(x=2000, y=5600), dead=False, battery=25, scans=[11]), 
        #     2: Drone(drone_id=2, pos=Vector(x=4400, y=5000), dead=False, battery=25, scans=[4, 5, 7]), 
        #     1: Drone(drone_id=1, pos=Vector(x=7149, y=5043), dead=False, battery=22, scans=[5, 6, 10, 13]), 
        #     3: Drone(drone_id=3, pos=Vector(x=2874, y=5140), dead=False, battery=22, scans=[4, 11, 7])} 
        visible_fish = get_visible_fish(verbose = True)
        my_radar_blips = get_my_radar_blips(my_radar_blips, verbose =True )
        

        print(f'my_drones:{my_drones}', file=sys.stderr, flush=True)


        #############
        # update the game variables
        #############

        # isolate monsters:
        monster_creatures = [fish for fish in visible_fish if fish.detail.type == -1]
        #print(f"monster_creatures: {monster_creatures} ", file=sys.stderr, flush=True)
        
        # Instantiate MyDroneState for each drone
        if Turn == 0:
            for drone in my_drones:
                my_states[drone.drone_id] = MyDroneState(drone.drone_id)  # Pass only the drone_id, not the whole drone
        else: 
            for drone in my_drones:
                my_states[drone.drone_id].update_status(drone)
                print(f"my_states: {my_states}", file=sys.stderr, flush=True)


        #############
        # Action decision tree by drone 
        #############


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


                if len(drone.scans) >= min_fishes_scanned :

                    print(f"MOVE {drone.pos.x} {490} {0} SURFACE")
                    
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

        Turn += 1
