import unittest
from Final.room_3 import Market
from unittest.mock import patch

"""
    Unit test created for level 3: Market
"""

class MarketUnitTest(unittest.TestCase):
    def setUp(self):
        """
            Initialising all the attributes
        :return: None
        """
        self.bag = ['Byzantine coin', 'Map']
        self.test = Market(self.bag)
        self.correctValue = "Value entered!"
        self.incorrectValue = "Incorrect value entered!"
        self.pathExists = "Path exists!"
        self.pathDoesNotExists = "Path does not exists!"


    def tearDown(self):
        """
            Deleting required test case after completion
        :return: None
        """
        del(self.test)

    @patch('builtins.input', side_effect=['1 2', '3 1'])
    def test_1(self, mock_input):
        """
            Test cases where the correct input is entered (for the function: checkItems())
        :return: None
        """

        # When entering 1 2, ['Mountain climbing boots', 'Windcheater'] should be chosen
        calling_1 = self.test.checkItems({"Mountain climbing boots": 10, "Windcheater": 20, "Waterproof jacket": 20, "Swim wear": 90, "Balenciaga T shirt": 100}, 2)
        self.assertEqual(calling_1, ['Mountain climbing boots', 'Windcheater'], "Incorrect!")

        # When entering 3 1, ['Waterproof jacket', 'Mountain climbing boots'] should be chosen
        calling_2 = self.test.checkItems({"Mountain climbing boots": 10, "Windcheater": 20, "Waterproof jacket": 20, "Swim wear": 90,
             "Balenciaga T shirt": 100}, 2)
        self.assertEqual(calling_2, ['Waterproof jacket', 'Mountain climbing boots'], "Incorrect!")

    @patch('builtins.input', side_effect=['1 2', '3'])
    def test_2(self, mock_input):
        """
            More test cases where the correct input is entered (for the function: checkItems())
        :return: None
        """

        # When entering 1 2, ['Knife', 'Pistol'] should be chosen
        calling_1 = self.test.checkItems({"Knife": 10, "Pistol": 30, "Hunting rifle": 40, "Assault rifle": 100, "AK-47": 200}, 2)
        self.assertEqual(calling_1, ['Knife', 'Pistol'], "Incorrect!")

        # When entering 3, ['Hunting rifle'] should be chosen
        calling_2 = self.test.checkItems({"Knife": 10, "Pistol": 30, "Hunting rifle": 40, "Assault rifle ": 100, "AK-47": 200}, 2)
        self.assertEqual(calling_2, ['Hunting rifle'], "Incorrect!")

    @patch('builtins.input', side_effect=['1 2', '1 2', '1 2'])
    def test_3(self, mock_input):
        """
            Test case for function checkConditions() which asks user to enter items
        :return: None
        """
        # Entering 1 2 (for 1st condition), 1 2(for 2nd condition) and 1 2(for 3rd condition) should return
        # ['Byzantine coin', 'Map', 'Mountain climbing boots', 'Windcheater', 'Knife', 'Pistol', 'Rope', 'Ladder']
        calling_1 = self.test.checkConditions()

        self.assertEqual(calling_1, ['Byzantine coin', 'Map', 'Mountain climbing boots', 'Windcheater', 'Knife', 'Pistol', 'Rope', 'Ladder'], "Incorrect items!")

    @patch('builtins.input', side_effect=['1 2', '3', '1 2'])
    def test_4(self, mock_input):
        """
            Another test case for function checkConditions() which asks user to enter items
        :return: None
        """

        # Entering 1 2 (for 1st condition), 3(for 2nd condition) and 1 2(for 3rd condition) should return
        # ['Byzantine coin', 'Map', 'Mountain climbing boots', 'Windcheater', 'Hunting rifle', 'Rope', 'Ladder']
        calling_1 = self.test.checkConditions()
        self.assertEqual(calling_1,
                         ['Byzantine coin', 'Map', 'Mountain climbing boots', 'Windcheater', 'Hunting rifle', 'Rope',
                          'Ladder'], "Incorrect items!")