from room_1 import Museum
from room_2 import Home
from room_3 import Market
from room_4 import JungleWithoutObstacles
from room_5 import JungleExpedition
from room_6 import Cave
from room_7 import Pyramid1
from room_8 import Pyramid2
import copy
import time
import tkinter as tk


"""
    This is main class for the Game, Uncharted. This game consists of 9 levels
    where the a single player will be shown multiple obstacles in each of these
    levels. The player further needs come up with viable and logical solutions
    to each of the obstacles displayed and complete the assigned task.

    The goal of this game is to :
        locate blue sap of a tree, which when ingested makes the drinker
        nearly invincible.

    In order to play this game, a class Game is created which initialises all
    rooms and the required variables. The function, play() is used as the
    calling functions for al other levels. A player can only move onto the
    next level if they have successfully completed the current level. In
    the case of incomplete levels, the specific level will have to be repeated 
    from a certain point until it has been completed with respect to the 
    objective.

    The game requires the user to have access to the SciView plot access in
    PyCharm as it is used to display maps and other vital images.

    This game has been developed by taking inspiration from the Playstation
    game, Uncharted.
"""

class Game():
    def __init__(self):
        """
            Initialises all the variables required for each level
        """
        self.name = ''
        self.bag = []
        self.bagThresh = 10
        self.museumBagAndDesc = {}

        # Correct Museum items, map, starting point of the Museum and its respective map color description
        self.museumItems = ["byzantine coin", "map"]
        self.museumMap = [[1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0],
                          [1, 0, -1, 0, 1],
                          [0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 1]]
        self.museumStartPoint = [2, 2]
        self.museumDesc = "Map of the museum (blue : current point and visited node, red : Artifact, green : Empty space):"

        # Jungle map, starting point of the jungle and its respective map color description (for absence of obstacles)
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

        # Jungle map, starting point of the jungle and its respective map color description (for presence of obstacles)
        self.jungleWithObstaclesMap = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                       [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                       [2, 1, 5, 0, 0, 0, 0, 2, 1, 2],
                                       [2, 1, 2, 2, 2, 2, 0, 2, 1, 2],
                                       [2, 1, 2, 0, 0, 0, 0, 0, 1, 2],
                                       [2, 1, 0, 0, 2, 2, 2, 0, 1, 2],
                                       [2, 1, 0, 2, 0, 0, 0, 0, 1, 2],
                                       [2, 1, 0, 0, 0, 2, 0, 9, 1, 2],
                                       [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        self.jungleWithObstaclesStartPoint = [2, 2]
        self.jungleWithObstaclesMapDesc = "Map of the Jungle : (yellow : current point and visited node, red : obstacle, black :empty path, white : destination)"

        # Pyramid map, starting point of the pyramid and its respective map color description (for choosing articles)
        self.pyramidMap = [[1, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0],
                           [1, 0, -1, 0, 1],
                           [0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 1]]
        self.pyramidStart = [2, 2]
        self.pyramidDesc = "Map of the courtyard (orange : current point and visited node, black : Item, red : Empty space):"

        # Pyramid map, starting point of the pyramid and its respective map color description (for the final room)
        self.pyramidRoom1Map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                [2, 1, 2, 0, 0, 5, 0, 2, 1, 2],
                                [2, 1, 2, 0, 2, 2, 0, 2, 1, 2],
                                [2, 1, 0, 0, 0, 0, 0, 2, 1, 2],
                                [2, 1, 0, 2, 2, 2, 2, 2, 1, 2],
                                [2, 1, 0, 2, 0, 0, 0, 0, 1, 2],
                                [2, 1, 0, 0, 0, 2, 2, 9, 1, 2],
                                [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        self.pyramidRoom1Start = [2, 5]
        self.pyramidRoom1Desc = "Map of the Pyramid : (orange : current point and visited node, yellow : obstacle, white :empty path, black : destination)"
        self.journey = ''

    def displayBag(self, level):
        """
            Function to display items in the bag.
        :param level: level at which the user is currently at
        :return: None
        """
        print(f"Items present in the bag after the {level} : {self.bag}")

    def tempWindow(self, txt, flag):
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("800x180")
        self.win.resizable(False, False)
        flash = 'red'
        if flag == 1:
            tk.Label(self.win, text= txt, fg=flash).pack()
        elif flag == 2:
            tk.Label(self.win, text=txt[0], fg='green').pack()
            tk.Label(self.win, text=txt[1], fg='green').pack()

        tk.Button(self.win, text="Okay", command=self.win.destroy,relief="raised",bg='#567', fg='White').pack()
        self.win.mainloop()

    def play(self):
        """
            Initialises all rooms and displays all the objectives.
            Overall the main play loop.
        :return: None
        """

        self.win = tk.Tk()  # Create a window
        self.win.title("Uncharted")  # Set window title
        self.win.geometry("500x180")  # Set window size
        self.win.resizable(False, False)

        tk.Label(self.win, text = f"Hi {self.name}\nWelcome to Uncharted!",bg='black',fg='white').grid(row = 1, column = 2)
        tk.Label(self.win, text = f"You have recently discovered that a certain tree sap can lead to invincibility!").grid(row = 2, column = 2)
        tk.Label(self.win, text = "The objective of this game is to find the invincibility tree by crossing all the levels!\n").grid(row = 3, column = 2)
        tk.Button(self.win, text = "Okay", command = self.win.destroy,bg='#567', fg='White',relief="raised").grid(row = 4, column = 2)
        self.journey = f"Okay"
        self.win.mainloop()
        # ``````````````````````````````````````````````````````````````````````````````
        #Creating the level: Museum
        tempMuseumMap = copy.deepcopy(self.museumMap)
        tempMusemStartPoint = copy.deepcopy(self.museumStartPoint)
        #
        # loop until correct items stolen from the museum
        while True:
            room1 = Museum(self.museumStartPoint, self.museumMap, self.museumDesc)
            museumBagAndDesc, bag = room1.getBag()
            journeyPath = room1.returnJourney()
            self.journey = f"{self.journey}{journeyPath}"
            if set(bag) == set(self.museumItems):
                self.bag = bag
                self.museumBagAndDesc = museumBagAndDesc
                break
            else:
                self.tempWindow("INCORRECT ITEMS STOLEN FROM THE MUSEUM! RETRY!", 1)
                self.journey = f"{self.journey}\nOkay"
                tempMuseumMap1 = copy.deepcopy(tempMuseumMap)
                tempMuseumStartPoint1 = copy.deepcopy(tempMusemStartPoint)
                self.museumMap = tempMuseumMap1
                self.museumStartPoint = tempMuseumStartPoint1
        self.tempWindow(["Correct items stolen form the museum!", "Going back home......."], 2)
        self.journey = f"{self.journey}\nOkay"

        self.museumBagAndDesc, bag = room1.getBag()
        # Creating the level: Home
        #self.museumBagAndDesc = {'Map' : "ANCIENT MAP WITH THE A PATH LEADING TO SOME PLACE", 'Byzantine coin' : 'COIN WITH THE FOLLOWING WRITTEN "THE SOLUTION TO ALL PROBLEMS"'}
        #  Uncomment the above lines to check the below code individually

        # ``````````````````````````````````````````````````````````````````````````````
        room2 = Home(self.museumBagAndDesc)
        self.tempWindow(["All items analysed! and destination found!", "Going to the market......."], 2)
        self.journey = f"{self.journey}\nOkay"
        room2journey = room2.returnJourney()
        self.journey = f"{self.journey}{room2journey}"


        # Creating the level: Market
        self.bag = ['Byzantine coin', 'Map']
          # Uncomment the above lines to check the below code individually
        print("Chapter 3 (Location : Market)")
        # ``````````````````````````````````````````````````````````````````````````````
        self.bag = self.museumItems
        room3 = Market(self.bag)
        room3journey = room3.returnJourney()
        self.journey = f"{self.journey}{room3journey}"
        self.tempWindow(["All items bought! Going to the destination", f"Items in bag : {self.bag}"], 2)
        self.journey = f"{self.journey}\nOkay"
        # ``````````````````````````````````````````````````````````````````````````````
        # Creating the level: jungle without animals
        tempJungleObstacesMap = copy.deepcopy(self.jungleWithoutObstaclesMap)
        tempJungleWithoutObstaclesStartPoint = copy.deepcopy(self.jungleWithoutObstaclesStartPoint)
        while True:
            room4 = JungleWithoutObstacles(self.jungleWithoutObstaclesMap, self.jungleWithoutObstaclesStartPoint, self.jungleWithoutObstaclesMapDesc, "jet")
            room4journey = room4.returnJourney()
            self.journey = f"{self.journey}{room4journey}"
            if room4.levelComplete:
                break
            else:
                temp1 = copy.deepcopy(tempJungleObstacesMap)
                temp2 = copy.deepcopy(tempJungleWithoutObstaclesStartPoint)
                self.jungleWithoutObstaclesMap = temp1
                self.jungleWithoutObstaclesStartPoint = temp2
                self.tempWindow("Cannot exit from the jungle! Retry", 1)
                self.journey = f"{self.journey}\nOkay"
        self.tempWindow(["First part of the jungle crossed!", "Moving ahead......."], 2)
        self.journey = f"{self.journey}\nOkay"
        # Creating the level: jungle with animals
        #self.bag = ['Byzantine coin', 'Map', 'Boots', 'Windcheater', 'Knife', 'Pistol', 'Rope', 'Ladder']
        #self.bag = ['Byzantine coin', 'Map', 'Boots', 'Windcheater', 'Hunting rifle', 'Rope', 'Ladder']
        #  Uncomment the above lines to check the below code individually (uncomment only one at one time)
        # ``````````````````````````````````````````````````````````````````````````````
        room5 = JungleExpedition(self.bag)
        self.bag = room5.getBag()
        room5journey = room5.returnJourney()
        self.journey = f"{self.journey}{room5journey}"
        self.tempWindow(["You have escaped the hyenas!", "Walking in the cave......."], 2)
        self.journey = f"{self.journey}\nOkay"
        # ``````````````````````````````````````````````````````````````````````````````
        # Creating the level: cave
        tempCaveMap = copy.deepcopy(self.jungleWithObstaclesMap)
        tempCaveStartPoint = copy.deepcopy(self.jungleWithObstaclesStartPoint)
        while True:
            room6 = Cave(self.jungleWithObstaclesMap, self.jungleWithObstaclesStartPoint, self.jungleWithObstaclesMapDesc, "hot")
            room6journey = room6.returnJourney()
            self.journey = f"{self.journey}{room6journey}"
            if room6.levelComplete:
                break
            else:
                temp1 = copy.deepcopy(tempCaveMap)
                temp2 = copy.deepcopy(tempCaveStartPoint)
                self.jungleWithObstaclesMap = temp1
                self.jungleWithObstaclesStartPoint = tempCaveStartPoint
                self.tempWindow("Cannot exit from the Cave! Retry", 1)
                self.journey = f"{self.journey}\nOkay"
        self.bag = ["byzantine coin", "map"]
        self.tempWindow(["After exiting the cave, you made your way towards the pyramid", f"The following items remain in the bag : {self.bag}"], 2)
        self.journey = f"{self.journey}\nOkay"
        # ``````````````````````````````````````````````````````````````````````````````
        # Creating the level: pyramid
        self.bag = ["byzantine coin", "map"]
        #  Uncomment the above class to check the below code individually
        self.pyramidItems =  ['sticks', 'byzantine coin', 'torch', 'map', 'stones']
        tempPyramidMap = copy.deepcopy(self.pyramidMap)
        tempPyramidStartPoint = copy.deepcopy(self.pyramidStart)
        while True:
            room7 = Pyramid1(self.pyramidStart, self.pyramidMap, self.pyramidDesc, self.bag)
            room7journey = room7.returnJourney()
            self.journey = f"{self.journey}{room7journey}"
            bag = room7.getBag()
            if set(bag) == set(self.pyramidItems):
                self.bag = bag
                break
            else:
                self.tempWindow("INCORRECT ITEMS STOLEN FROM THE MUSEUM! RETRY!", 1)
                self.journey = f"{self.journey}\nOkay"
                tempMuseumMap1 = copy.deepcopy(tempPyramidMap)
                tempMuseumStartPoint1 = copy.deepcopy(tempPyramidStartPoint)
                self.pyramidMap = tempMuseumMap1
                self.pyramidStart = tempMuseumStartPoint1
                self.bag = ['byzantine coin', 'map']

        self.tempWindow(["Correct items stolen from the museum!", "Fire created using sticks, stones and the torch"], 2)
        self.journey = f"{self.journey}\nOkay"
        self.bag.remove('sticks')
        self.bag.remove("stones")
        self.bag.remove("torch")
        # Creating the level: inside the pyramid
        self.bag = ["byzantine coin", "map"]
        #  Uncomment the above class to check the below code

        room8 = Pyramid2(self.pyramidRoom1Map, self.pyramidRoom1Start, self.pyramidRoom1Desc, self.bag)
        room8journey = room8.returnJourney()
        self.journey = f'{self.journey}{room8journey}'
        text_file = open("userJourney.txt", "w")
        n = text_file.write(self.journey)
        text_file.close()
        return True

def main():
    """
        Calling function for the game
    :return: None
    """
    game = Game()
    if game.play() == True:
        print("Game Completed!")


if __name__ == "__main__":
    main()