#!/usr/bin/python
"""
File: Lagrange_poly3.py

Copyright (c) 2016 Michael Seaman

License: MIT

Extends the Lagrange interpolation model from Assignment 2 into a class
"""

import numpy as np
import Lagrange_poly2 as LP
from unittest import TestCase

class LagrangeInterpolation():
    def __init__(self, xList, yList):
        """Constructor"""
        self.xp = xList
        self.yp = yList
    
    def __call__(self, x):
        """
        Evaluates the interpolation model at point x
        """
        return LP.p_L(x, self.xp, self.yp)
    
    def plot(self, res = 1001):
        """
        Plots the linear interpolation of the coordinate 
        lists provided. Resolution is optional and defaults
        to 1001.
        """
        LP.graph(self.xp, self.yp, resolution = res)

class test_LagrangeInterpolation(TestCase):
    """
    This class contains the test on the Lagrange interpolation function
    """
    
    def test_p_L(self, xp = np.linspace(0,np.pi, 5), yp = np.array([np.sin(y) for y in np.linspace(0,np.pi, 5)]) ):
        """
        Tests the polynomial interpolation function on the given x values, which should return 
        exactly the given y values. The function uses the values on sin(x) default
        """
        LP.test_p_l(xp, yp)