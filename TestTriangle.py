# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual('Right', classifyTriangle(3, 4, 5), '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual('Right', classifyTriangle(5, 3, 4), '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual('Equilateral', classifyTriangle(1, 1, 1), '1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual('Scalene', classifyTriangle(14, 3, 42), '14,3,2 is a Scalene triangle')

    def testIsoceles(self):
        self.assertEqual('Isoceles', classifyTriangle(3, 3, 2), '3,3,2 is a Isoceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
