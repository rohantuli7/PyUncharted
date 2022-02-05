"""
    Helper file consisting of the Mapping class
    which contains mapping functions inherited by
    all classes using maps.
"""

import matplotlib.pyplot as plt
import tkinter as tk

class Mapping():
    def __init__(self, startingPath, Map, pathDescription):
        """
            Initialises the map with respect to the parameters
        :param startingPath: starting point
        :param Map: map of the location
        :param pathDescription: color description of the map
        """

        # Directions and their respective values in 2D space
        self.directions = self.directions = {'north' : [-1, 0],
                                             'south' : [1, 0],
                                             'east' : [0, 1],
                                             'west' : [0, -1]}
        self.path = startingPath
        self.Map = Map
        self.pathDescription = pathDescription


    def showMap(self, colorMap):
        """
            Displaying the map
        :param colorMap: colormap to be used
        :return: None
        """
        plt.imshow(self.Map, cmap=colorMap)
        plt.axis("off")
        plt.show()

    def displayLocations(self):
        """
            Display directions available
        :return: None
        """
        print(f"Directions available : {list(self.directions.keys())}")

    def directionsLocationsAndMap(self):
        """
            Current position in the map, directions available and map description
        :return: None
        """
        self.displayLocations()
        print(f"Currently at position : {self.path}")
        print(self.pathDescription)