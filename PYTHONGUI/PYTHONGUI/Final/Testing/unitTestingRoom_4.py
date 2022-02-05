import unittest
from Final.room_4 import JungleWithoutObstacles
from unittest.mock import patch

"""
    Unit test created for level 4: JungleWithoutObstacles
"""

class JungleWithoutObstaclesUnitTesting(unittest.TestCase):
    def setUp(self):
        """
            Initialising all the attributes
        :return: None
        """
        # Jungle map, starting point of the jungle and its respective map color description(for absence of obstacles)
        self.jungleWithoutObstaclesMap = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                          [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                          [2, 1, 5, 2, 0, 0, 0, 0, 1, 2],
                                          [2, 1, 0, 0, 0, 2, 2, 0, 1, 2],
                                          [2, 1, 2, 2, 0, 0, 0, 0, 1, 2],
                                          [2, 1, 0, 0, 0, 2, 2, 0, 1, 2],
                                          [2, 1, 0, 2, 2, 2, 2, 0, 1, 2],
                                          [2, 1, 0, 0, 0, 0, 0, 9, 1, 2],
                                          [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                          [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        self.jungleWithoutObstaclesStartPoint = [2, 2]
        self.jungleWithoutObstaclesMapDesc = "Map of the Jungle (yellow : current point and visited node, red : destination, dark blue : empty path, light blue : obstacle):"
        self.test = JungleWithoutObstacles(self.jungleWithoutObstaclesMap,
                                           self.jungleWithoutObstaclesStartPoint,
                                           self.jungleWithoutObstaclesMapDesc)
        self.jungleWithoutObstaclesMap1 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                          [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                          [2, 1, 5, 2, 0, 0, 0, 0, 1, 2],
                                          [2, 1, 5, 5, 5, 2, 2, 0, 1, 2],
                                          [2, 1, 2, 2, 5, 0, 0, 0, 1, 2],
                                          [2, 1, 5, 5, 5, 2, 2, 0, 1, 2],
                                          [2, 1, 5, 2, 2, 2, 2, 0, 1, 2],
                                          [2, 1, 5, 5, 5, 5, 5, 9, 1, 2],
                                          [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                          [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        self.test1 = JungleWithoutObstacles(self.jungleWithoutObstaclesMap1,
                                           [7, 6],
                                           self.jungleWithoutObstaclesMapDesc)



    def tearDown(self):
        """
            Deleting required test case after completion
        :return: None
        """
        del self.test

    @patch('builtins.input', side_effect=['south'])
    def test_1(self, mock_input):
        """
            Test case for values initial point
        :return: None
        """

        #This function should return 0 because the destination according to the map will be not have been reached yet
        calling_1 = self.test.Path()
        self.assertEqual(calling_1, 0)

    @patch('builtins.input', side_effect=['east'])
    def test_2(self, mock_input):
        """
            Test case for values destination point
        :return: None
        """

        # Enter east. This function should return 1 because the destination according to the map will be reached
        calling_2 = self.test1.Path()
        self.assertEqual(calling_2, 1)