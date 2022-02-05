import unittest
from Final.room_7 import CaveToPyramid
from unittest.mock import patch

"""
    Unit test created for level : CaveToPyramid
"""

class CaveToPyramidUnitTesting(unittest.TestCase):
    def setUp(self):
        """
            Initialising all the attributes
        :return: None
        """

        self.test1 = CaveToPyramid(['byzantine coin', 'map', 'mountain climbing boots', 'waterproof jacket', 'rope', 'ladder'])
        self.test2 = CaveToPyramid(['byzantine coin', 'map', 'mountain climbing boots', 'windcheater', 'rope', 'ladder'])


    def tearDown(self):
        """
            Deleting required test case after completion
        :return: None
        """
        del (self.test1)

    @patch('builtins.input', side_effect=['3', '3', 'mountain climbing boots, waterproof jacket', 'rope', 'ladder'])
    def test_1(self, mock_input):
        """
            Test 1 for the unit
        :return: None
        """

        # Entering
        #  1. 3
        #  2. 3
        #  3. mountain climbing boots, waterproof jacket
        #  4. rope
        #  5. ladder
        #  These values will lead to the correct assertion!

        calling_1 = self.test1.journey()

        self.assertEqual(calling_1, ['byzantine coin', 'map'], "Incorrect values chosen!")

    @patch('builtins.input', side_effect=['3', '3', 'mountain climbing boots, windcheater', 'rope', 'ladder'])
    def test_2(self, mock_input):
        """
            Test 2 for the unit
        :return: None
        """

        # Enter
        #  1. 3
        #  2. 3
        #  3. mountain climbing boots, windcheater
        #  4. rope
        #  5. ladder
        #  Entering these values will lead to the correct assertion
        self.assertEqual(self.test2.journey(), ['byzantine coin', 'map'], "Incorrect values chosen!")