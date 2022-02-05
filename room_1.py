'''
    Level 1: Museum

    A class Museum is created which is used to depict a Museum with
    6 articles kept at the corners of the room. The player needs to
    select the correct articles with respect to the objective mentioned.
    SciView required to complete this level.
'''

import copy
from utils import Mapping
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm
import numpy as np
import matplotlib
matplotlib.use('Agg')
import time


class Museum():
    def __init__(self, museumStartPoint, museumMap, museumDesc):
        """
            Initialises the Museum with respect to the parameters
            entered through the main play loop and a few other
            essential parameters. This class inherits the Mapping
            class and uses its functions for various tasks.
        :param museumStartPoint: initial location of the player
        :param museumMap: map of the museum (matrix)
        :param museumDesc: color description of the map
        """
        # Articles placed in the museum and their description

        self.journey = ''
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1500x1500")
        self.win.resizable(False, False)
        self.museumDesc = museumDesc
        self.articleAndDescription = {(0, 0) : {'book': "HIDDEN TREASURES"},
                                      (2, 0) : {'painting' : "PAINTING OF THE PYRAMID OF GIZA"},
                                      (4, 0) : {'map' : "ANCIENT MAP"},
                                      (0, 4) : {'ancient scroll' : "EGYPTIAN SCRIPTURES"},
                                      (2, 4) : {'byzantine coin' : 'COIN WITH THE FOLLOWING WRITTEN '
                                                                   '"THE SOLUTION TO ALL PROBLEMS"'},
                                      (4, 4) : {'ottoman ring' : "ANCIENT GOLD AND DIAMOND RING"}}

        # Description of articles
        self.articleDesc = {key : value for i in self.articleAndDescription.values() for key, value in i.items()}

        # Map of the Museum
        self.map = museumMap

        # Empty bag
        self.bag = []

        self.museumBagThresh = 2
        self.path = museumStartPoint

        # Colormap used for depiction
        self.mapColors = 'jet'

        plt.imshow(self.map, cmap = "jet")
        plt.axis("off")
        plt.savefig("game_images/map1.png")
        self.img = tk.PhotoImage(file='game_images/map1.png')
        self.imgLabel = tk.Label(self.win, image=self.img)
        self.imgLabel.grid(row = 2, column = 1, columnspan = 3)

        #Calling the parent class constructor
        self.directions = self.directions = {'north' : [-1, 0],
                                             'south' : [1, 0],
                                             'east' : [0, 1],
                                             'west' : [0, -1]}


        self.location = tk.Label(self.win, text = "Chapter 1 (Location : Museum)",bg='black',fg='')
        self.objective = tk.Label(self.win, text="Objective: To find the map with the correct directions to the treasure and"
                                                            "the artifact which will be the solution to all your problems!")
        self.location.grid(row = 0, column = 2)
        self.objective.grid(row = 1, column = 2)
        self.tkPath = tk.Label(self.win, text = f"Currently at position : {self.path}",fg='red')
        self.tkPath.grid(row = 3, column = 2)
        self.tkIncPath = tk.Label(self.win, text = f"")
        self.tkIncPath.grid(row = 4, column = 2)
        self.tkMuseumDesc = tk.Label(self.win, text = self.museumDesc)
        self.tkMuseumDesc.grid(row = 5, column = 1, columnspan = 3)
        self.bagItems = tk.Label(self.win, text = "Items in the bag : "+str(self.bag),bg='black',fg='white')
        self.bagItems.grid(row = 6, column = 2)
        self.direction_()
        self.tkArtName = tk.Label(self.win, text="")
        self.tkArtName.grid(row = 7, column = 1, columnspan = 3)
        self.tkArtDesc = tk.Label(self.win, text="")
        self.tkArtDesc.grid(row = 8, column = 1, columnspan = 3)
        self.optionText = tk.Label(text = "")
        self.optionText.grid(rows = 10, column = 1, columnspan = 3)
        self.optionNote = tk.Label(text="")
        self.optionNote.grid(rows=11, column=1, columnspan = 3)
        tk.Button(self.win, text="Quit", command=self.win.destroy, bg='#567', fg='White',relief="raised").grid(row = 0, column = 0)
        self.yes = tk.Button(text="yes", command=self.addItem, bg='#567', fg='White',relief="raised")
        self.win.mainloop()

    def direction_(self):
        tk.Button(self.win,text='North',relief="raised", bg='#567', fg='White' ,command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["north"])], "north"), ).grid(row = 3, column = 6)
        tk.Button(self.win, text = 'East',relief="raised", bg='#567', fg='White', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["east"])], "east")).grid(row = 4, column = 6)
        tk.Button(self.win, text='South', relief="raised", bg='#567', fg='White',command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["south"])], "south")).grid(row = 5, column = 6)
        tk.Button(self.win, text='West', relief="raised", bg='#567', fg='White',command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["west"])], "west")).grid(row = 6, column = 6)

    def displayItemAndDesc(self, itemDict):
        """
            Displaying a single item and its respective description.
        :param itemDict: Dictionary consisting of an item and its description.
        :return: None
        """
        return(f"Item : {list(itemDict.keys())[0]}\nDescription : {list(itemDict.values())[0]}")

    def getBag(self):
        """
            returns the items placed in the bag
        :return: items placed in the bag and their description, and the bag.
        """
        self.bag = sorted(self.bag)
        self.bag.reverse()
        return {i:self.articleDesc[i] for i in self.bag}, self.bag

    def isPathExist(self, tempPath, journeyPath, path_min = 0, path_max = 4):
        """
            To check whether entered path exists wrt the map
        :param tempPath: path entered by the user
        :param path_min: lower bound of the size of the map matrix
        :param path_max: upper bound of the size of the map matrix
        :return:
        """
        self.journey = f"{self.journey}\n{journeyPath}"
        if (tempPath[0] < path_min or tempPath[0] > path_max) or (tempPath[1] < path_min or tempPath[1] > path_max):
            self.tkIncPath.configure(text="INCORRECT PATH ENTERED. RETRY!")
            self.tkPath.configure(text=f"Currently at position : {self.path}")
            return False
        else:
            self.path[0], self.path[1] = tempPath[0], tempPath[1]
            self.tkPath.configure(text=f"Currently at position : {self.path}")
            self.tkIncPath.configure(text="")
            self.movingMuseum()
            return True

    def movingMuseum(self):
        if len(self.bag) != self.museumBagThresh:
            if self.map[self.path[0]][self.path[1]] == 1:
                itemDict = self.articleAndDescription[tuple(self.path)]
                self.tkArtName.configure(text = f"Article Name : {list(itemDict.keys())[0]}")
                self.tkArtDesc.configure(text = f"Article Description : {list(itemDict.values())[0]}")
                self.map[self.path[0]][self.path[1]] = -1
                self.optionText.configure(text = "Do you want to put the item in the bag?")
                self.optionNote.configure(text = "NOTE: ONLY 2 ITEMS CAN BE PLACED IN THE BAG!")
                plt.imshow(self.map, cmap="jet")
                plt.savefig("game_images/map.png")
                self.img = tk.PhotoImage(file='game_images/map.png')
                self.imgLabel.configure(image = self.img)
                if len(self.bag) != self.museumBagThresh:
                    self.yes = tk.Button(text = "yes", command = self.addItem,relief="raised", bg='#567', fg='White')
                    self.yes.grid(rows = 12, column = 2)
            elif self.map[self.path[0]][self.path[1]] != 1:
                if self.yes.winfo_exists() == 1:
                    self.yes.destroy()

        else:
            tk.Label(text = "Exiting the museum! (in 3 seconds)",relief="raised",fg='red').grid(rows = 13, columns = 2)
            self.win.destroy()
            self.win.mainloop()

    def addItem(self):
        self.journey = f"{self.journey}\nyes"
        if len(self.bag) != self.museumBagThresh:
            if list(self.articleAndDescription[tuple(self.path)].keys())[0] in self.bag:
                pass
            else:
                self.bag.append(list(self.articleAndDescription[tuple(self.path)].keys())[0])
                self.bagItems.configure(text="Items in the bag : " + str(self.bag))
                if len(self.bag) == 2:
                    tk.Label(text="Exiting the museum! (in 3 seconds)").grid(rows=13, column = 2)
                    self.win.destroy()
                    self.win.mainloop()
        else:
            tk.Label(text = "Two items stolen! exiting the museum (in 3 seconds)!")
            time.sleep(3)
            self.win.destroy()
            self.win.mainloop()

    def returnJourney(self):
        return self.journey