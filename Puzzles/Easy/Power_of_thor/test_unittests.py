import unittest
import main
import numpy as np 

x1 = np.array([4,5])
x2 = np.array([0, 1])
x3 = np.array([0, -1])
grid = np.array([40, 18])

class Test_TestMain(unittest.TestCase):

    def test_distance(self):
        result = main.distance(x1, x2)
        self.assertTrue(0 <= result < 100)

    def test_relative_dist(self):
        result = main.relative_dist(x1, x2)
        self.assertTrue(np.sum(result) < 100)
    
    def test_movement(self):
        result = main.movement(x2)
        self.assertEqual(result[0] , 0)

    def test_add_pos(self):
        result = main.add_pos(x2, x3)
        self.assertEqual(result[0] , 0)
    
    def test_generate_range(self):
        result = main.generate_range()
        self.assertEqual(np.sum(result) , 0)

    def test_potential_pos(self):
        rg = main.generate_range()
        result = main.potential_pos(x1, rg)
        self.assertEqual(np.sum(result) , 9*np.sum(x1))

    def test_in_grid(self): 
        result = main.in_grid(x1 , grid)
        self.assertEqual(result, True)

    def test_check_matrix(self):
        rg = main.generate_range()
        result = main.check_matrix(rg, grid)
        self.assertEqual(np.sum(result) < 9, True)

    def test_manh_dist(self):
        result = main.manh_dist(x1,x2)
        self.assertEqual(result, 8)


if __name__ == 'main': 
    unittest.main()