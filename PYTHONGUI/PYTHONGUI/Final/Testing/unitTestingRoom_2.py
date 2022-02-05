import unittest
from Final.room_2 import Home

"""
    Unit test created for level 2: Home
"""

class HomeUnitTest(unittest.TestCase):
    def setUp(self):
        """
            Initialising all the attributes
        :return: None
        """
        self.museumBagAndDesc = {'Map' : "ANCIENT MAP WITH THE A PATH LEADING TO SOME PLACE", 'Byzantine coin' : 'COIN WITH THE FOLLOWING WRITTEN "THE SOLUTION TO ALL PROBLEMS"'}
        self.test = Home(self.museumBagAndDesc)
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

    def test_1(self):
        """
            Test case where correct input is entered (yes)
        :return: None
        """
        self.assertTrue(self.test.checkUserInput('yes', "Home"), self.correctValue)

    def test_2(self):
        """
            Test case where correct input is entered (no)
        :return: None
        """
        self.assertTrue(self.test.checkUserInput('no', "Home"), self.correctValue)

    def test_3(self):
        """
            Test case where incorrect input is entered
        :return: None
        """
        self.assertTrue(self.test.checkUserInput('ededeld', "Home"), self.incorrectValue)

    def test_4(self):
        """
            Test case where incorrect input is entered
        :return: None
        """
        self.assertFalse(self.test.checkUserInput('dedede', "Home")[0], self.correctValue)

    def test_5(self):
        """
            Test case where an empty string is passed
        :return: None
        """
        self.assertFalse(self.test.checkUserInput('', "Home")[0], self.correctValue)


