#!/usr/bin/python

import unittest
from controller import Controller


class MyTestClass(unittest.TestCase):
    def test_left_border(self):
        self.assertEqual(Controller.getListNum(1, 6), [1, 2, '..', 6])

    def test_right_border(self):
        self.assertEqual(Controller.getListNum(6, 6), [1, '..', 5, 6])

    def test_second(self):
        self.assertEqual(Controller.getListNum(2, 6), [1, 2, 3, '..', 6])

    def test_prelast(self):
        self.assertEqual(Controller.getListNum(5, 6), [1, '..', 4, 5, 6])

    def test_zero_count(self):
        self.assertEqual(Controller.getListNum(5, 0), [])

    def test_out_of_border(self):
        self.assertEqual(Controller.getListNum(7, 6), [1, '..', 5, 6])
        self.assertEqual(Controller.getListNum(0, 6), [1, 2, '..', 6])

if __name__ == '__main__':
    unittest.main()
