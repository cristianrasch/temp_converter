# -*- coding: UTF-8 -*-

from fractions import Fraction

def farenheit_to_celcius(degrees):
    """ Tc = (5/9)*(Tf-32); """
    return int(Fraction(5, 9)*(degrees-32))
        
def celcius_to_farenheit(degrees):
    """ Tf = (9/5)*Tc+32; """
    return int(Fraction(9, 5)*degrees+32)
