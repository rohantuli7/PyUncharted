"""
    Level 9: Pyramid

    Class Pyramid2 is created which makes the user re-enter
    the pyramid and sets up a series of obstacles in their
    quest to reach the tree of invincibility. Final
    level in the game. The respective class inherits the
    JungleWithoutObstacles class.
"""

import time
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import copy
import numpy as np

class Pyramid2():
    def __init__(self, map, startpoint, mapDesc, bag):
        """
            Constructor method initialising required attributes and
            passing parameters received to the superclass.
        :param map: map of the pyramid
        :param startpoint: starting point
        :param mapDesc: color description of the map
        :param bag: bag of items
        """
        self.journey = ''
        self.bag = bag

        # Options available
        self.options = ["Burn the map with the torch", "Rub the wall with the map"]

        # Map of the pyramid room
        self.finalMap = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                         [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                         [2, 1, 5, 0, 0, 0, 0, 2, 1, 2],
                         [2, 1, 2, 2, 2, 2, 0, 2, 1, 2],
                         [2, 1, 2, 0, 0, 0, 0, 0, 1, 2],
                         [2, 1, 0, 0, 2, 2, 2, 0, 1, 2],
                         [2, 1, 0, 2, 0, 0, 0, 0, 1, 2],
                         [2, 1, 0, 0, 0, 2, 0, 9, 1, 2],
                         [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

        # Starting point of the second pyramid room
        self.finalMapStartPoint = [2, 2]

        # Map description of the second pyramid room
        self.finalMapDesc = "Map of the Jungle : (yellow : current point and visited node, red : obstacle, black :empty path, white : destination)"

        # initialising variables for this class
        self.Map = self.finalMap
        self.path = self.finalMapStartPoint
        self.mapDesc = self.finalMapDesc
        self.colorMap = 'viridis'

        self.directions = self.directions = {'north': [-1, 0],
                                             'south': [1, 0],
                                             'east': [0, 1],
                                             'west': [0, -1]}

        self.levelComplete = False

        # initializing the GUI window
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)

        # initialising variables required for this level and placing them on the frame
        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(row=0, column=0)

        self.loadMap()

        self.location = tk.Label(self.win, text=self.displayLocation())
        self.location.grid(row=1, column=2, columnspan = 4)
        self.objective = tk.Label(self.win, text=self.displayObjective())
        self.objective.grid(row=2, column=2, columnspan = 4)

        self.printMessage = tk.Label(self.win, text="")
        self.printMessage.grid(row=4, column=2, columnspan = 4)
        self.direction_()
        self.tkPath = tk.Label(self.win, text=f"Currently at position : {self.path}")
        self.tkPath.grid(row=5, column=2, columnspan = 4)
        self.tkJungleDesc = tk.Label(self.win, text=self.mapDesc)
        self.tkJungleDesc.grid(row=6, column=2, columnspan = 4)
        self.win.mainloop()

    def direction_(self):
        """
            Function linking direction buttons on screen to the traversal logic
        :return: None
        """
        tk.Button(self.win, text='North',
                  command=lambda: self.isPathExist([i + j for i, j in zip(self.path, self.directions["north"])], "north")).grid(
            row=4, column=6)
        tk.Button(self.win, text='East',
                  command=lambda: self.isPathExist([i + j for i, j in zip(self.path, self.directions["east"])], "east")).grid(
            row=5, column=6)
        tk.Button(self.win, text='South',
                  command=lambda: self.isPathExist([i + j for i, j in zip(self.path, self.directions["south"])], "south")).grid(
            row=6, column=6)
        tk.Button(self.win, text='West',
                  command=lambda: self.isPathExist([i + j for i, j in zip(self.path, self.directions["west"])], "west")).grid(
            row=7, column=6)

    def loadMap(self):
        """
            Function for storing and loading the map after every move
        :return:
        """
        plt.imshow(self.Map, cmap=self.colorMap)
        plt.axis("off")
        plt.savefig("game_images/map1.png")
        self.img = tk.PhotoImage(file='game_images/map1.png')
        self.imgLabel = tk.Label(self.win, image=self.img)
        self.imgLabel.grid(row=3, column=1, columnspan=3)

    def isPathExist(self, tempPath, text):
        """
            Function for checking if path exits
        :param tempPath: temporary path entered by the user
        :param text: button clicked
        :return:
        """
        self.journey = f"{self.journey}\n{text}"
        if (tempPath[0] < 0 or tempPath[0] > 9) or (tempPath[1] < 0 or tempPath[1] > 9):
            self.printMessage.configure(text="INCORRECT PATH ENTERED. RETRY!")
        elif (self.Map[tempPath[0]][tempPath[1]] == 1):
            self.printMessage.configure(text="OUT OF BOUNDS PATH CHOSEN! RETRY!")
        elif (self.Map[tempPath[0]][tempPath[1]] == 2):
            self.printMessage.configure(text="OBSTACLE IN THE PATH! RETRY")
        elif (self.Map[tempPath[0]][tempPath[1]] == 5):
            self.printMessage.configure(text="CANNOT MOVE BACK! RETRY!")
        else:
            # If correct input entered, respective updation will be made in the map
            self.printMessage.configure(text="")
            self.path[0], self.path[1] = tempPath[0], tempPath[1]
            self.tkPath.configure(text=f"Currently at position : {self.path}")
            if self.Map[self.path[0]][self.path[1]] == 9:
                self.levelComplete = True
                self.loadMap()
                self.finalMission()
            else:
                self.Map[self.path[0]][self.path[1]] = 5
                self.loadMap()

    def displayObjective(self):
        """
            displaying the objective of this level
        :return: objective
        """
        return "Objective : to find the invincibility tree."

    def displayLocation(self):
        """
            displaying the location
        :return: chapter and location
        """
        return "Chapter 8 : inside the pyramid"

    def checkLevel(self):
        """
            function to check if level is complete
        :return: True if complete else False
        """
        return self.levelComplete

    def finalMission(self):
        """
            function for final mission simulation
        :return: None
        """

        # initialising and placing widgets on the GUI frame
        self.empty = tk.Label(self.win, text="")
        self.text1 = tk.Label(self.win, text = "The path ahead is not visible with the current flame.")
        self.instructions1 = tk.Label(self.win, text = "The following is written on the wall: The map which brought you here will guide you further!")
        self.options1 = tk.Label(self.win, text = "Following options are available : ")
        self.button1_1 = tk.Button(self.win, text = "Burn the map", command = self.Mission)
        self.button1_2 = tk.Button(self.win, text = "Rub map against the wall", command = lambda : self.incorrectInput(self.condition1, "CAUTION: The map is destroyed and you are stuck in the Pyramid! Restart!", "Rub map against the wall"))
        self.condition1 = tk.Label(self.win, text = "")

        self.empty.grid(row = 8, column = 1)
        self.text1.grid(row = 9, column = 1, columnspan = 4)
        self.instructions1.grid(row = 10, column = 1, columnspan = 4)
        self.options1.grid(row = 11, column = 1, columnspan = 4)
        self. button1_1.grid(row = 12, column = 1, columnspan = 2)
        self.button1_2.grid(row = 12, column = 3, columnspan = 2)
        self.condition1.grid(row = 13, column = 1, columnspan = 4)

    def Mission(self):
        """
            final room simulation
        :return: None
        """

        # initialising widgets and placing them on the GUI frame
        self.journey = f"{self.journey}\nBurn the map"
        self.text2 = tk.Label(self.win, text = 'You have reached a door which says "You hold the solution to all your problems!"')
        self.text3 = tk.Label(self.win, text="There is a coin shaped key present at a pedestal next to the door.")
        self.text4 = tk.Label(self.win, text="Would you like use the key or use an item from your bag to open the door?")
        self.finalButton1 = tk.Button(self.win, text="Byzantine coin", command = lambda : self.gameEnd())
        self.finalButton2 = tk.Button(self.win, text="Coin shaped key", command = lambda : self.incorrectInput(self.text5, "Incorrect item chosen!", "Coin shaped key"))
        self.text5 = tk.Label(self.win, text="")
        self.text6 = tk.Label(self.win, text="")
        self.text7 = tk.Label(self.win, text="")

        self.text2.grid(row = 14, column = 1, columnspan = 4)
        self.text3.grid(row=15, column=1, columnspan=4)
        self.text4.grid(row=16, column=1, columnspan=4)
        self.finalButton1.grid(row=17, column=1, columnspan=2)
        self.finalButton2.grid(row=17, column = 3, columnspan = 2)
        self.text5.grid(row=18, column=1, columnspan=4)
        self.text6.grid(row=19, column=1, columnspan=4)
        self.text7.grid(row=20, column=1, columnspan=4)


    def incorrectInput(self, button, ip, text):
        """
            updation of value on incorrect input
        :param button: label to be updated
        :param ip: updation value
        :param text: label value
        :return:
        """
        self.journey = f"{self.journey}\n{text}"
        button.configure(text=ip)

    def gameEnd(self):
        """
            Ending of the game
        :return: None
        """
        self.journey = f"{self.journey}\nByzantine coin"
        self.text5.configure(text="CONGRATULATION! YOU HAVE REACHED THE BLUE SAP!\n")
        self.text6.configure(text="You are now invincible!")
        self.text7.configure(text="Game Completed! (Ending game in 5 seconds)")
        self.win.after(5000, self.win.destroy)

    def returnJourney(self):
        """
            Returning the user journey for this level
        :return: user journey for this level
        """
        return self.journey