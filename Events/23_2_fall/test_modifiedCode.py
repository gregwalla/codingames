import unittest
from modifiedCode import Vector, collision, Drone, Fish, FishDetail
import math

class TestVector(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.max_x = 10000
        self.max_y = 10000

    def test_addition(self):
        print("test_addition")
        v1 = Vector(100, 100)
        v2 = Vector(200, 300)
        result = v1.add(v2)
        self.assertEqual(result, Vector(300, 400))

    def test_subtraction(self):
        print("test_subtraction")
        v1 = Vector(500, 500)
        v2 = Vector(100, 100)
        result = v1.subtract(v2)
        self.assertEqual(result, Vector(400, 400))

    def test_multiply(self):
        print("test_multiply")
        v = Vector(100, 200)
        scalar = 5
        result = v.multiply(scalar)
        self.assertEqual(result, Vector(500, 1000))

    def test_divide(self):
        print("test_divide")
        v = Vector(100, 200)
        scalar = 2
        result = v.divide(scalar)
        self.assertEqual(result, Vector(50, 100))

    def test_normalize(self):
        print("test_normalize")
        v = Vector(300, 400)
        result = v.normalize()
        # Using an acceptable error margin due to floating point arithmetic
        self.assertAlmostEqual(result[0], 0.6, places=1)
        self.assertAlmostEqual(result[1], 0.8, places=1)

    def test_distance(self):
        print("test_distance")
        v1 = Vector(100, 100)
        v2 = Vector(400, 400)
        result = v1.distance(v2)
        self.assertEqual(result, 424)  # Rounded distance from (100, 100) to (400, 400)


    def test_closest_point(self):
        print("test_closest_point")
        line_start = Vector(0, 0)
        line_end = Vector(0, 10)
        point = Vector(5, 5)
        expected_closest_point = Vector(0, 5)
        self.assertEqual(point.closest(line_start, line_end), expected_closest_point)

    def test_closest_point2(self):
        print("test_closest_point2")
        line_start = Vector(0, 0)
        line_end = Vector(10, 0)
        point = Vector(5, 5)
        expected_closest_point = Vector(5, 0)
        self.assertEqual(point.closest(line_start, line_end), expected_closest_point)


 
class TestCollisionRealistic(unittest.TestCase):
    # Map boundaries
    max_x = 10000
    max_y = 1000
    # Movement ranges
    drone_range = 600
    monster_range = 540
    collision_range = 500

    def test_drone_monster_horizontal_collision(self):
        print("test_before-3")
        # Drone and monster moving towards each other on the same Y coordinate (horizontal line)
        drone = Drone(drone_id=0, pos=Vector(8500, 500), dead=False, battery=100, scans=[], speed=Vector(500, 0))
        monster = Fish(fish_id=1, pos=Vector(9500, 500), speed=Vector(-500, 0), detail=FishDetail(color=0, type=-1))
        result = collision(drone, monster, self.collision_range)
        self.assertIsNotNone(result)
        # The time to collision is determined by the distance over the sum of speeds
        time_to_collision = 0.5
        self.assertAlmostEqual(result.t, time_to_collision)

    def test_drone_monster_vertical_collision(self):
        print("test_before-2")
        # Drone and monster moving towards each other on the same X coordinate (vertical line)
        drone = Drone(drone_id=0, pos=Vector(5000, 8500), dead=False, battery=100, scans=[], speed=Vector(0, 250))
        monster = Fish(fish_id=1, pos=Vector(5000, 9500), speed=Vector(0, -250), detail=FishDetail(color=0, type=-1))
        result = collision(drone, monster, self.collision_range)
        self.assertIsNotNone(result)

        time_to_collision = 1.0
        self.assertAlmostEqual(result.t, time_to_collision)

    def test_drone_monster_vertical_immediate_collision(self):
        print("test_beforen")
        # Drone and monster passing each other on parallel Y coordinates (horizontal line near miss)
        drone = Drone(drone_id=0, pos=Vector(9000, 0), dead=False, battery=100, scans=[], speed=Vector(10, 0))
        monster = Fish(fish_id=1, pos=Vector(9000, 200), speed=Vector(-40, 0), detail=FishDetail(color=0, type=-1))
        result = collision(drone, monster, self.collision_range)
        time_to_collision = 0.0
        self.assertAlmostEqual(result.t, time_to_collision)

    def test_drone_monster_future_collision(self):
        print("test_drone_monster_future_collision")
        # Drone and monster moving towards each other but too far away to collide
        drone = Drone(drone_id=0, pos=Vector(7000, 0), dead=False, battery=100, scans=[], speed=Vector(-600, 0))
        monster = Fish(fish_id=1, pos=Vector(5000, 0),  detail=FishDetail(color=0, type=-1), speed=Vector(500, 0),)
        result = collision(drone, monster, self.collision_range)
        print(f'result: {result}')
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()