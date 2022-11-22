"""
    Level 4: part of the jungle without animals

    Class JungleWithoutObstacles is created which depicts a jungle
    where no obstacles are present and the user is supposed to
    cross the jungle through the path shown.

"""

import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class JungleWithoutObstacles():
    def __init__(self, map, startPoint, mapDesc, colorMap):
        """
            Initialises the JungleWithoutObstacles.
            Necessary parameters are passed to the function
        :param map: map of the jungle
        :param startPoint: starting point on the map
        :param mapDesc: color description of the map
        """

        # initialising the required parameters
        self.Map = map
        self.path = startPoint
        self.mapDesc = mapDesc
        self.colorMap = colorMap
        self.journey = ''
        self.directions = self.directions = {'north': [-1, 0],
                                             'south': [1, 0],
                                             'east': [0, 1],
                                             'west': [0, -1]}
        self.levelComplete = False

        # Initialising the tkinter GUI
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)

        # creation of buttons and widgets
        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(row=0, column=0)

        self.loadMap()

        self.location = tk.Label(self.win, text = self.displayLocation())
        self.location.grid(row = 1, column = 2)
        self.objective = tk.Label(self.win, text=self.displayObjective())
        self.objective.grid(row=2, column=2)

        self.printMessage = tk.Label(self.win, text = "")
        self.printMessage.grid(row = 4, column = 2)
        self.direction_()
        self.tkPath = tk.Label(self.win, text=f"Currently at position : {self.path}")
        self.tkPath.grid(row=5, column=2)
        self.tkJungleDesc = tk.Label(self.win, text=self.mapDesc)
        self.tkJungleDesc.grid(row=6, column=2)
        self.win.mainloop()


    def direction_(self):
        """
            Function linking direction buttons on screen to the traversal logic
        :return: None
        """
        tk.Button(self.win, text='North', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["north"])], "north")).grid(row = 4, column = 6)
        tk.Button(self.win, text = 'East', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["east"])], "east")).grid(row = 5, column = 6)
        tk.Button(self.win, text='South', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["south"])], "south")).grid(row = 6, column = 6)
        tk.Button(self.win, text='West', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["west"])], "west")).grid(row = 7, column = 6)

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

        # checking conditions whether the path entered lies in the overall map
        if (tempPath[0] < 0 or tempPath[0] > 9) or (tempPath[1] < 0 or tempPath[1] > 9):
            self.printMessage.configure(text = "INCORRECT PATH ENTERED. RETRY!")
        elif (self.Map[tempPath[0]][tempPath[1]] == 1):
            self.printMessage.configure(text="OUT OF BOUNDS PATH CHOSEN! RETRY!")
        elif (self.Map[tempPath[0]][tempPath[1]] == 2):
            self.printMessage.configure(text="OBSTACLE IN THE PATH! RETRY")
        elif (self.Map[tempPath[0]][tempPath[1]] == 5):
            self.printMessage.configure(text="CANNOT MOVE BACK! RETRY!")
        else:

            # If correct input entered, respective updation will be made in the map
            self.printMessage.configure(text = "")
            self.path[0], self.path[1] = tempPath[0], tempPath[1]
            self.tkPath.configure(text=f"Currently at position : {self.path}")
            if self.Map[self.path[0]][self.path[1]] == 9:
                self.levelComplete = True
                self.loadMap()
                self.win.destroy()
            else:
                self.Map[self.path[0]][self.path[1]] = 5
                self.loadMap()

    def displayObjective(self):
        """
            displaying the objective of this level
        :return: None
        """
        return "Objective: to reach the destination!"

    def displayLocation(self):
        """
            displaying the location
        :return:
        """
        return "Chapter 4 (Location : part of the jungle without animals)"

    def checkLevel(self):
        """
            function to check whether level is completed
        :return: True if level completed else False
        """
        return self.levelComplete

    def returnJourney(self):
        """
            Returning the user journey for this level
        :return: user journey for this level
        """
        return self.journey