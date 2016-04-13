#!/usr/bin/python
"""
File: Lagrange_poly4.py

Copyright (c) 2016 Michael Seaman

License: MIT

Extends the Lagrange interpolation model from Assignment 2 into a class. This time
The constructor can accept arguments of a function and a range of values and mesh size
to compute its own list of x and y
"""

import numpy as np
import Lagrange_poly2 as LP
from unittest import TestCase

class LagrangeInterpolation():
    def __init__(self, arg1, arg2, arg3):
        if(isinstance(arg1, np.ndarray) and isinstance(arg2, np.nparray)):
            xList = arg1
            yList = arg2
        else:
            minx = arg2[0]
            maxx = arg2[1]
            f = arg1
            n = arg3
            xList = np.linspace(minx, maxx, n)
            f_vec = np.vectorize(f)
            yList = f_vec(xList)
        self.xp = xList #arg1
        self.yp = yList #arg2
    
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
    
    def test_p_L(self, f = np.sin, x = [0, np.pi], n = 11):
        """
        Tests the polynomial interpolation function on the given x values, which should return 
        exactly the given y values. The function uses the values on sin(x) default
        """
        p_L = LagrangeInterpolation(f, x, n)
        LP.test_p_l(p_L.xp, p_L.yp)