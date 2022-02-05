import unittest
from Final.room_1 import Museum

"""
    Unit test created for level 1: Home
"""

class MusuemUnitTest(unittest.TestCase):
    def setUp(self):
        """
            Initialising required attributes
        :return: None
        """
        self.museumItems = ["byzantine coin", "map"]
        self.museumMap = [[1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0],
                          [1, 0, -1, 0, 1],
                          [0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 1]]
        self.museumStartPoint = [2, 2]
        self.museumDesc = "Map of the museum (blue : current point and visited node, red : Artifact, green : Empty space):"
        self.test = Museum(self.museumMap, self.museumStartPoint, self.museumDesc)
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
            Test case 1: for all correctly entered values
        :return: None
        """
        self.assertTrue(self.test.checkPathInput("north")[0], self.correctValue)
        self.assertTrue(self.test.isPathExist([1, 1], 0, 4), self.incorrectValue)
        self.assertTrue(self.test.checkPathInput("south south")[0], self.correctValue)
        self.assertTrue(self.test.isPathExist([1, 3], 0, 4), self.incorrectValue)

    def test_2(self):
        """
            Test case 2: for all correctly entered values with greater threshold
        :return: None
        """
        self.assertTrue(self.test.checkPathInput("east west north")[0], self.correctValue)
        self.assertTrue(self.test.isPathExist([10, 10], 0, 11), self.incorrectValue)
        self.assertTrue(self.test.checkPathInput("west east north south")[0], self.correctValue)
        self.assertTrue(self.test.isPathExist([5, 5], 0, 6), self.incorrectValue)


    def test_3(self):
        """
            Test case 3: for all incorrectly entered values
        :return: None
        """
        self.assertFalse(self.test.checkPathInput("")[0], self.incorrectValue)
        self.assertFalse(self.test.isPathExist([10, 10], 0, 4), self.pathDoesNotExists)
        self.assertFalse(self.test.checkPathInput("")[0], self.incorrectValue)
        self.assertFalse(self.test.isPathExist([10, 10], 11, 15), self.pathDoesNotExists)