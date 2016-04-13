#!/usr/bin/python
"""
File: Polynomial_vec.py

Copyright (c) 2016 Michael Seaman

License: MIT

Creating a class for polynomials that implements standard functions that
are common for polynomials. The class's code is later vectorized
"""

import timeit
import numpy as np
from unittest import TestCase

class Polynomial:
    """
    The polynomial class stores a list of coefficient values in increasing
    order of powers of x. Polynomials can be added, multiplied, subtracted
    differentiated, and outputed as strings
    """
    def __init__(self, coefficients):
        """
        Initiializes with a (python) list of coefficients, in
        increasing order by powers of x
        """
        self.coeff = coefficients
    
    def __add__(self, other):
        """
        Uses vectorized adding to the arrays that are reduced to the same size
        then concatenates the left overs.
        """
        smaller_array = np.copy(self.coeff)
        larger_array = np.copy(other.coeff)
        
        if len(self.coeff) > len(other.coeff):
            smaller_array = np.copy(other.coeff)
            larger_array = np.copy(self.coeff)
        smaller_array += larger_array[:len(smaller_array)]
        return Polynomial(np.concatenate([smaller_array, larger_array[len(smaller_array):]]))
    
    def __call__(self, x):
        """
        Evaluates this polynomial at the given value of x
        """
        power_array = np.arange(len(self.coeff))
        power_array = x ** power_array
        return np.inner(self.coeff, power_array)
    
    def differentiate(self):
        """
        Differentiate this polynomial in-place.
        This implementation I think is a bit more elegant
        than the book's solution
        """
        coeff_factors = np.arange(len(self.coeff))
        self.coeff = (self.coeff * coeff_factors)[1:]

    
    def call_unvectorized(self, x):
        """
        From this point down, the methods are unvectorized
        
        Evaluates the polynomial at the given value of x
        """
        s = 0
        for i in xrange(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def add_unvectorized(self, other):
        """
        Adds two polynomials, adding the coefficients only at their respective
        powers of x. Returns a polynomial.
        """
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  #copy!
            for i in xrange(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in xrange(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
    
    def mul_unvectorized(self, other):
        """
        Returns a list of coefficients of from multiplying two polynomials
        that is no longer than the sum of the two coefficient list
        """
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = np.zeros(M + N + 1)
        for i in xrange(0, M+1):
            for j in xrange(0, N+1):
                result_coeff[i+j] += c[i]*d[i]
        return Polynomial(result_coeff)
    
    def differentiate_unvectorized(self):
        """
        Differentiate this polynomial in-place.
        """
        for i in xrange(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]
    
    def derivative(self):
        """
        Differentiates this polynomial by copying it and the returning the
        differentiated version
        """
        dpdx = Polynomial(self.coeff[:]) # make a copy
        dpdx.differentiate()
        return dpdx
    
    def __str__(self):
        s = ""
        for i in range(len(self.coeff)):
            if(self.coeff[i] != 0):
                s += " + %g*x^%d" % (self.coeff[i], i)
        s = s.replace("+ -", "- ")
        s = s.replace("x^0", "1")
        s = s.replace(" 1*", " ")
        s = s.replace("x^1 ", "x ")
        if s[0:3] == " + ":
            s = s[3:]
        if s[0:3] == " - ":
            s = "-" + s[3:]
        return s

class test_Polynomial(TestCase):
    """
    This class contains the test on the Polynomial class
    """
    def test_vectorized_call(self):
        """
        Tests that when x = 1, the output is the list of sum of the polynomial list,
        that the output is the first coeff when x = 0, and tests the basic case of
        5 + 0(4)^1 + 2(4)^2 - 3(4)^3 = -155
        """
        testPoly = Polynomial(np.array([5,0,2,-3]))
        assert(testPoly(1) == np.sum(testPoly.coeff))
        assert(testPoly(0) == testPoly.coeff[0])
        assert(testPoly(4) == -155)
        
    
    def test_vectorized_add(self):
        """
        Tests the vectorized add on a basic case and a case
        where the one array is empty
        """
        poly1 = Polynomial(np.arange(5))
        poly2 = Polynomial(np.ones(10))
        empty_poly = Polynomial(np.zeros(0))
        sum_of_1_and_2 = Polynomial(np.concatenate([np.arange(1,6), np.ones(5)]))
        assert( np.array_equal(sum_of_1_and_2.coeff, (poly1 + poly2).coeff))
    
    def test_vectorized_differentiate(self):
        """
        Tests the vectorized differentiation on a simple test case:
        f(x) = 4 + 2x - 5x^2 + 13x^3
        f'(x) = 2 - 10x + 39x^2
        """
        poly1 = Polynomial([4,2,-5,13])
        poly1.differentiate()
        poly1_prime = Polynomial([2,-10,39])
        assert(np.array_equal(poly1.coeff, poly1_prime.coeff))

def time_method(name_of_method_with_args, nRepeats):
    return timeit.timeit('poly1.' + name_of_method_with_args, setup='from Polynomial_vec import Polynomial;x = 50 ; poly1 = Polynomial([7,4,-2,0,0,0,4,1,-1,0,2]); poly2 = Polynomial([0,4, 8,8,5, 0, -2,-3])', number = nRepeats)
    

