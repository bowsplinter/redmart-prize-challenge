import unittest
import solution

class TestSolutionMethods(unittest.TestCase):

    def test_sum_id(self):
        tuples = [(1, 1, 3),(2, 1, 3),(4, 1, 3)]
        self.assertEqual(solution.get_sum_id(tuples), 7)

    def test_sum_id_negative(self):
        tuples = [(-1, 1, 3),(-10, 1, 3),(-2, 1, 3)]
        self.assertEqual(solution.get_sum_id(tuples), -13)

    def test_volume(self):
        dims = [3,4,8]
        self.assertEqual(solution.get_volume(dims),96)

    def test_knapsack(self):
        items = [(1,4,12,1), (2,2,1,1), (3,6,4,2), (4,1,1,1), (5,2,2,1)]
        expected_items = [(2,2,1,1), (3,6,4,2), (4,1,1,1), (5,2,2,1)]
        self.assertEqual(solution.knapsack(items, 15), expected_items)

    def test_knapsack_weight(self):
        items = [(1,4,12,1), (2,2,1,1), (3,3,4,2), (4,1,1,1), (5,2,2,1), (3,3,4,1)]
        expected_items = [(2,2,1,1), (4,1,1,1), (5,2,2,1), (3,3,4,1)]
        self.assertEqual(solution.knapsack(items, 8), expected_items)

    def test_knapsack_weight_reverse_order(self):
        items = [(1,4,12,1), (2,2,1,1), (3,3,4,1), (4,1,1,1), (5,2,2,1), (3,3,4,2)]
        expected_items = [(2,2,1,1), (3,3,4,1), (4,1,1,1), (5,2,2,1)]
        self.assertEqual(solution.knapsack(items, 8), expected_items)

if __name__ == '__main__':
    unittest.main()