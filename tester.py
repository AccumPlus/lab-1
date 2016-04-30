#!/usr/bin/python
''' Класс тестирования генератора списка номеров страниц '''

import unittest
from controller import Controller


class MyTestClass(unittest.TestCase):
    ''' Класс тестирования генератора списка номеров страниц '''
    def test_left_border(self):
        ''' Тест левой границы '''
        self.assertEqual(Controller.get_list_num(1, 6), [1, 2, '..', 6])

    def test_right_border(self):
        ''' Тест правой границы '''
        self.assertEqual(Controller.get_list_num(6, 6), [1, '..', 5, 6])

    def test_second(self):
        ''' Тест второй позиции '''
        self.assertEqual(Controller.get_list_num(2, 6), [1, 2, 3, '..', 6])

    def test_prelast(self):
        ''' Тест предпоследней позиции '''
        self.assertEqual(Controller.get_list_num(5, 6), [1, '..', 4, 5, 6])

    def test_zero_count(self):
        ''' Тест нулевого количества страниц '''
        self.assertEqual(Controller.get_list_num(5, 0), [])

    def test_out_of_border(self):
        ''' Тест выхода за границу '''
        self.assertEqual(Controller.get_list_num(7, 6), [1, '..', 5, 6])
        self.assertEqual(Controller.get_list_num(0, 6), [1, 2, '..', 6])

if __name__ == '__main__':
    unittest.main()
