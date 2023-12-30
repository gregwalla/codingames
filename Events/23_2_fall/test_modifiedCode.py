import unittest
from modifiedCode import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.max_x = 10000
        self.max_y = 10000

    def test_addition(self):
        v1 = Vector(100, 100)
        v2 = Vector(200, 300)
        result = v1.add(v2)
        self.assertEqual(result, Vector(300, 400))

    def test_subtraction(self):
        v1 = Vector(500, 500)
        v2 = Vector(100, 100)
        result = v1.subtract(v2)
        self.assertEqual(result, Vector(400, 400))

    def test_multiply(self):
        v = Vector(100, 200)
        scalar = 5
        result = v.multiply(scalar)
        self.assertEqual(result, Vector(500, 1000))

    def test_divide(self):
        v = Vector(100, 200)
        scalar = 2
        result = v.divide(scalar)
        self.assertEqual(result, Vector(50, 100))

    def test_normalize(self):
        v = Vector(300, 400)
        result = v.normalize()
        # Using an acceptable error margin due to floating point arithmetic
        self.assertAlmostEqual(result[0], 0.6, places=1)
        self.assertAlmostEqual(result[1], 0.8, places=1)

    def test_distance(self):
        v1 = Vector(100, 100)
        v2 = Vector(400, 400)
        result = v1.distance(v2)
        self.assertEqual(result, 424)  # Rounded distance from (100, 100) to (400, 400)


if __name__ == '__main__':
    unittest.main()