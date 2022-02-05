"""
    Level 6: inside the cave

    Class Cave is created to simulate the interiors of a cave.
    The user is required to towards the end of the cave while
    they will be subjected to a number of obstacles.

    SciView required to complete this level.
"""
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Cave():
    def __init__(self, map, startPoint, mapDesc, colorMap):
        """
            Initialises the JungleWithoutObstacles.
            This class inherits the Mapping class
            and uses its functions for various tasks.
            The parameters are passed to the superclass
        :param map: map of the jungle
        :param startPoint: starting point on the map
        :param mapDesc: color description of the map
        """
        self.journey = ""
        self.Map = map
        self.path = startPoint
        self.mapDesc = mapDesc
        self.colorMap = colorMap

        self.directions = self.directions = {'north': [-1, 0],
                                             'south': [1, 0],
                                             'east': [0, 1],
                                             'west': [0, -1]}

        self.levelComplete = False

        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)

        tk.Button(self.win, text="Quit", command=self.win.destroy, bg='#567', fg='White').grid(row=0, column=0)

        self.loadMap()

        self.location = tk.Label(self.win, text = self.displayLocation(), bg='black', fg='White')
        self.location.grid(row = 1, column = 2)
        self.objective = tk.Label(self.win, text=self.displayObjective())
        self.objective.grid(row=2, column=2)

        self.printMessage = tk.Label(self.win, text = "",fg='red')
        self.printMessage.grid(row = 4, column = 2)
        self.direction_()
        self.tkPath = tk.Label(self.win, text=f"Currently at position : {self.path}")
        self.tkPath.grid(row=5, column=2)
        self.tkJungleDesc = tk.Label(self.win, text=self.mapDesc)
        self.tkJungleDesc.grid(row=6, column=2)
        self.win.mainloop()


    def direction_(self):
        tk.Button(self.win, text='North', bg='#567', fg='White', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["north"])], "north")).grid(row = 4, column = 6)
        tk.Button(self.win, text = 'East', bg='#567', fg='White', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["east"])], "east")).grid(row = 5, column = 6)
        tk.Button(self.win, text='South', bg='#567', fg='White', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["south"])], "south")).grid(row = 6, column = 6)
        tk.Button(self.win, text='West', bg='#567', fg='White', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["west"])], "west")).grid(row = 7, column = 6)

    def loadMap(self):
        plt.imshow(self.Map, cmap=self.colorMap)
        plt.axis("off")
        plt.savefig("game_images/map1.png")
        self.img = tk.PhotoImage(file='game_images/map1.png')
        self.imgLabel = tk.Label(self.win, image=self.img)
        self.imgLabel.grid(row=3, column=1, columnspan=3)

    def isPathExist(self, tempPath, text):
        self.journey = f"{self.journey}\n{text}"
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

            #Obstacle 1: flooding
            if self.path == [4, 6]:
                self.Map[4][7] = 2
                self.printMessage.configure(text="CAUTION: The river has overflown into the cave! Reroute!")

            # Obstacle 2: falling rocks
            elif self.path == [5, 3]:
                self.Map[5][4], self.Map[5][5], self.Map[5][6], self.Map[7][5] =  0, 0, 0, 0
                self.Map[6][6], self.Map[6][5] = 2, 2
                self.printMessage.configure(text="CAUTION: Rocks are falling! Reroute!")

            # Obstacle 3: falling rocks
            elif self.path == [7, 4] and self.Map[5][2] == 5:
                self.printMessage.configure(text="CAUTION: Falling rocks have made the area unreachable! Reroute!")
                self.Map[6][4] = 2
            elif self.path == [7, 4] and self.Map[5][2] == 0:
                self.printMessage.configure(text="CAUTION: Falling rocks have made the area unreachable! Reroute!")
                self.Map[7][3], self.Map[7][2], self.Map[6][2], self.Map[5][2] = 2, 2, 2, 2

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
        return "Chapter 6 (Location : Cave)"

    def checkLevel(self):
        return self.levelComplete

    def returnJourney(self):
        return self.journey