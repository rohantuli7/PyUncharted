import unittest
from Final.room_5 import JungleExpedition
from unittest.mock import patch

"""
    Unit test created for level 5: JungleExpedition
"""

class JungleExpeditionUnitTesting(unittest.TestCase):
    def setUp(self):
        """
            Initialising all the attributes
        :return: None
        """
        self.test1 = JungleExpedition(['Byzantine coin', 'Map', 'Boots', 'Windcheater', 'Knife', 'Pistol', 'Rope', 'Ladder'])

        self.test2 = JungleExpedition(['Byzantine coin', 'Map', 'Boots', 'Windcheater', 'Hunting rifle', 'Rope', 'Ladder'])


    def tearDown(self):
        """
            Deleting required test case after completion
        :return: None
        """
        del (self.test1)
        del (self.test2)

    @patch('builtins.input', side_effect=['pistol', 'yes', 'yes', 'yes', 'yes', 'yes', 'knife', 'yes', 'stop','1'])
    def test_1(self, mock_input):
        """
            Test 1 for the unit
        :return: None
        """

        calling_1 = self.test1.jungle()

        # Choose the pistol, shoot the bear 5 times, kill the cobra with the knife, stop in front of the elephants
        #  Run inside the case. Only when you enter these items, the bag will be correctly updated
        self.assertEqual(calling_1, ['byzantine coin', 'map', 'boots', 'windcheater', 'rope', 'ladder'], "Incorrect values chosen!")

    @patch('builtins.input', side_effect=['hunting rifle', 'yes', 'yes', 'yes', 'yes', 'yes', 'hunting rifle', 'yes', 'stop', '1'])
    def test_2(self, mock_input):
        """
            Test case 2 for the unit
        :return: None
        """

        calling_1 = self.test2.jungle()

        # Choose the hunting rifle, shoot the bear 5 times, shoot the cobra, stop in front of the elephants
        #  Run inside the case. Only when you enter these items, the bag will be correctly updated
        self.assertEqual(calling_1, ['byzantine coin', 'map', 'boots', 'windcheater', 'rope', 'ladder'], "Incorrect values chosen!")