#!/usr/bin/python
"""
File: Polynomial_dict.py

Copyright (c) 2016 Michael Seaman

License: MIT

The same class for polynomials, except coefficients are now stored in a dictionary vs.
an array
"""

from unittest import TestCase

class Polynomial:
    """
    The polynomial class stores a list of coefficient values in increasing
    order of powers of x. Polynomials can be added and outputed as strings
    """
    def __init__(self, coefficients):
        """
        Initiializes with a list of coefficients which are passed into a dictionary constructor.
        coefficients are paired with their index in increasing order
        """
        if(isinstance(coefficients, dict)):
            self.coeff = coefficients
        else:           #assuming it's a list
            self.coeff = dict()
            for i in xrange(len(coefficients)):
                if coefficients[i] != 0:
                    self.coeff[i] = coefficients[i]
    
    def __add__(self, other):
        """
        Uses vectorized adding to the arrays that are reduced to the same size
        then concatenates the left overs.
        """
        output_dict = self.coeff.copy()
        for k,v in other.coeff.iteritems():
            if k in output_dict:
                output_dict[k] += v
            else:
                output_dict[k] = v
        return Polynomial(output_dict)
    
    def __call__(self, x):
        """
        Evaluates this polynomial at the given value of x
        """
        output = 0
        for k,v in self.coeff.iteritems():
            output += v * (x ** k)
        return output

    def __eq__(self, other):
        """
        Overloads the equals operator by comparing the coefficient parameter
        for use in testing
        """
        return self.coeff == other.coeff


    def get_coefficient_list(self):
        """
        Returns a python list of coefficients with the correct ordering and indexing
        from the coefficient dictionary
        """
        output_length = max(self.coeff.keys()) + 1
        output = [0] * output_length
        for k, v in self.coeff.iteritems():
            output[k] = v
        return output
    
    def __str__(self):
        """
        Outputs as a string using algebreic notation, with increasing powers of x
        This code is repurposed from the non-dictionary part
        """

        coefficient_list = self.get_coefficient_list()
        s = ""
        for i in range(len(coefficient_list)):
            if(coefficient_list[i] != 0):
                s += " + %g*x^%d" % (coefficient_list[i], i)
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
    
    def test_add(self):
        """
        Tests the add method on a basic case and a case
        where the second dictionary is empty
        """
        poly1 = Polynomial([0,1,2,3,4])
        poly2 = Polynomial([1,1,1,1,1,1,1,1,1,1])
        empty_poly = Polynomial([])
        sum_of_1_and_2 = Polynomial([1,2,3,4,5,1,1,1,1,1])
        assert( sum_of_1_and_2 == poly1 + poly2 and poly1 + empty_poly == poly1 )
