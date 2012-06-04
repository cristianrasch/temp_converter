# -*- coding: UTF-8 -*-

import math

from fractions import Fraction

def farenheit_to_celcius(degrees):
    """ Tc = (5/9)*(Tf-32); """
    res = Fraction(5, 9)*(degrees-32)
    return math.trunc(res)
        
def celcius_to_farenheit(degrees):
    """ Tf = (9/5)*Tc+32; """
    res = Fraction(9, 5)*degrees+32
    return math.trunc(res)
