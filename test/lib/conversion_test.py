# -*- coding: UTF-8 -*-

import unittest2

from temp_converter.lib.conversion import *

class ConversionFunctionsTest(unittest2.TestCase):
    def test_converts_farenheit_to_celcius(self):
        self.assertEqual(farenheit_to_celcius(32), 0)
        
    def test_converts_celcius_to_farenheit(self):
        self.assertEqual(celcius_to_farenheit(0), 32)
        
    def test_rounds_temperature_conversions(self):
        temp_in_celcius = farenheit_to_celcius(92)
        self.assertEqual(temp_in_celcius, 33)
        temp_in_fahrenheit = celcius_to_farenheit(33)
        self.assertEqual(temp_in_fahrenheit, 91)
