# -*- coding: UTF-8 -*-

import unittest2

from temp_converter.lib.conversion import *

class ConversionFunctionsTest(unittest2.TestCase):
    def test_converts_farenheit_to_celcius(self):
        self.assertEqual(farenheit_to_celcius(32), 0)
        
    def test_converts_celcius_to_farenheit(self):
        self.assertEqual(celcius_to_farenheit(0), 32)
