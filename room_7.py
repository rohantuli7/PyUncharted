"""
    Level 7: Pyramid

    class Pyramid1 is created which inherits the Museum class.
    The user is required to choose a set of objects from the pyramid
    courtyard in order to create a burning torch to enter the pyramid.
"""

import time
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import copy

class Pyramid1():
    def __init__(self, pyramidStart, pyramidMap, pyramidDesc, bag):
        """
            Constructor method initialising required attributes and
            passing parameters received to the superclass.
        :param pyramidStart: starting point of the pyramid
        :param pyramidMap: map of the pyramid
        :param pyramidDesc: color description of the map
        :param bag: bag of items
        """

        self.journey = ''
        # Dictionary containing the location of items and their description
        self.articleAndDescription = {(0, 0) : {'sticks' : "Wood from an an old tree."},
                                      (2, 0) : {'stones' : "Egyptian pyramid stone."},
                                      (4, 0) : {'brick' : "Pyramid brick."},
                                      (0, 4) : {'leaf' : "Leaf from a tree."},
                                      (2, 4) : {'water' : "Rainwater in a puddle."},
                                      (4, 4) : {'old scripture' : "Old papyrus scroll."}}
        self.articleDesc = {key : value for i in self.articleAndDescription.values() for key, value in i.items()}
        self.map = pyramidMap
        # self.tempBag = bag
        self.bag = bag
        self.exit = False

        # Threshold of items which can be stored in the bag
        self.museumBagThresh = 5
        self.path = [2, 2]

        # color of map
        self.mapColors = 'flag'

        # items present
        self.items = ["Oil lamp", "Unlit torch", "Sand", "Brick"]

        self.directions = self.directions = {'north' : [-1, 0],
                                             'south' : [1, 0],
                                             'east' : [0, 1],
                                             'west' : [0, -1]}

        self.tempPyramidMap = copy.deepcopy(self.map)
        self.tempPyramidStartPoint = copy.deepcopy(self.path)

        # initialising the tkinter GUI
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)
        self.museumDesc = pyramidDesc

        # initialising and placing widgets on the frame
        self.location = tk.Label(self.win, text = "Chapter 7 (Location : Pyramid)")
        self.objective = tk.Label(self.win, text = "Objective : to create a fire and enter the pyramid!")
        self.instructions_1 = tk.Label(self.win, text = '')
        self.instructions_2 = tk.Label(self.win, text = "")
        self.task = tk.Label(self.win, text = "Task 1")
        self.selection = tk.Label(self.win, text = "")

        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(row=0, column=0)
        self.location.grid(row = 0, column = 2, columnspan = 4)
        self.objective.grid(row = 1, column = 2, columnspan = 4)
        self.task.grid(row = 2, column = 2, columnspan = 4)
        self.instructions_1.grid(row=3, column=2, columnspan = 4)
        self.instructions_2.grid(row=4, column=2, columnspan = 4)
        self.flame()
        self.selection.grid(row = 7, column = 2, columnspan = 4)
        self.win.mainloop()

    def destroy_widgets(self):
        """
            Destroying all widgets
        :return: None
        """
        for widgets in self.win.winfo_children():
            widgets.destroy()

    def item_selection(self, text):
        """
            checking if correct item selected
        :param text: value of button clicked
        :return:
        """
        self.journey = f"{self.journey}\n{text}"
        variable = self.var.get()
        if variable == 1:
            self.selection.configure(text="Correct item selected! (Exiting room in 3 seconds)")
            self.destroy_widgets()
            self.bag.append("torch")
            self.courtyard()
        else:
            self.selection.configure(text = "Incorrect item selected!")

    def flame(self):
        """
            displaying items to be chosen from
        :return: None
        """

        # initialising required variables and placing them on the GUI
        self.instructions_1.configure(text= "After entering the Pyramid, you realise that there is no light inside.")
        self.instructions_2.configure(text = "You are on you way outside to a courtyard and find the following objects")
        self.img_brick = ImageTk.PhotoImage(Image.open('GUI images/brick.png').resize((200, 200)))
        self.img_label_brick = tk.Label(image = self.img_brick)
        self.img_label_brick.grid(row = 5, column = 2)

        self.img_lamp = ImageTk.PhotoImage(Image.open('GUI images/oil_lamp.png').resize((200, 200)))
        self.img_label_lamp = tk.Label(image = self.img_lamp)
        self.img_label_lamp.grid(row = 5, column = 3)

        self.img_sand = ImageTk.PhotoImage(Image.open('GUI images/sand.png').resize((200, 200)))
        self.img_label_sand = tk.Label(image = self.img_sand)
        self.img_label_sand.grid(row = 5, column = 4)

        self.img_torch = ImageTk.PhotoImage(Image.open('GUI images/unlit_torch.png').resize((200, 200)))
        self.img_label_torch = tk.Label(image = self.img_torch)
        self.img_label_torch.grid(row = 5, column = 5)

        self.var = tk.IntVar()

        # Dictionary to create multiple buttons
        values = {"Brick": "2",
                  "Oil lamp": "4",
                  "Sand": "3",
                  "Unlit torch": "1"}

        for i, (text, value) in enumerate(values.items()):
            tk.Radiobutton(self.win, text=text, variable=self.var, value=value, command = lambda: self.item_selection(text)).grid(row = 6, column = i+2)

        tk.Label(self.win, text = "(On selection of correct item, you will be directed to the next page!)").grid(row = 8, column = 2, columnspan = 4)


    def courtyard(self):
        """
            setting up values for simulation of traversal in the courtyard
        :return: None
        """

        # creation of map for traversal
        plt.imshow(self.map, cmap = self.mapColors)
        plt.axis("off")
        plt.savefig("game_images/map8.png")
        self.img = tk.PhotoImage(file='game_images/map8.png')
        self.imgLabel = tk.Label(self.win, image=self.img)
        self.imgLabel.grid(row = 2, column = 1, columnspan = 3)

        self.directions = self.directions = {'north' : [-1, 0],
                                             'south' : [1, 0],
                                             'east' : [0, 1],
                                             'west' : [0, -1]}

        # initializing widgets and placing them on the frame
        self.location = tk.Label(self.win, text = "Chapter 8 (Location : Pyramid)")
        self.objective = tk.Label(self.win, text="Objective: To find the map with the correct directions to the treasure and"
                                                            "the artifact which will be the solution to all your problems!")

        self.location.grid(row = 0, column = 2)
        self.objective.grid(row = 1, column = 2)
        self.tkPath = tk.Label(self.win, text = f"Currently at position : {self.path}")
        self.tkPath.grid(row = 3, column = 2)
        self.tkIncPath = tk.Label(self.win, text = f"")
        self.tkIncPath.grid(row = 4, column = 2)
        self.tkMuseumDesc = tk.Label(self.win, text = self.museumDesc)
        self.tkMuseumDesc.grid(row = 5, column = 1, columnspan = 3)
        self.bagItems = tk.Label(self.win, text = "Items in the bag : "+str(self.bag))
        self.bagItems.grid(row = 6, column = 2)
        self.direction_()
        self.tkArtName = tk.Label(self.win, text="")
        self.tkArtName.grid(row = 7, column = 1, columnspan = 3)
        self.tkArtDesc = tk.Label(self.win, text="")
        self.tkArtDesc.grid(row = 8, column = 1, columnspan = 3)
        self.optionText = tk.Label(self.win, text = "")
        self.optionText.grid(row = 10, column = 1, columnspan = 3)
        self.optionNote = tk.Label(self.win, text="")
        self.optionNote.grid(row=11, column=1, columnspan = 3)
        self.l1 = tk.Label(self.win, text="(On completion of this round, you will be directed to the next room!)")
        self.l2 = tk.Label(self.win, text="(Failure to find the correct items will lead to redirection to the same room!)")
        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(row = 0, column = 0)
        self.yes = tk.Button(text="yes", command=self.addItem)
        self.win.mainloop()

    def direction_(self):
        """
            Function linking direction buttons on screen to the traversal logic
        :return: None
        """
        tk.Button(self.win,text='North', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["north"])], "north")).grid(row = 3, column = 6)
        tk.Button(self.win, text = 'East', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["east"])], "east")).grid(row = 4, column = 6)
        tk.Button(self.win, text='South', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["south"])], "south")).grid(row = 5, column = 6)
        tk.Button(self.win, text='West', command = lambda : self.isPathExist([i+j for i, j in zip(self.path, self.directions["west"])], "west")).grid(row = 6, column = 6)

    def isPathExist(self, tempPath, text, path_min = 0, path_max = 4):
        """
            To check whether entered path exists wrt the map
        :param tempPath: path entered by the user
        :param path_min: lower bound of the size of the map matrix
        :param path_max: upper bound of the size of the map matrix
        :return: True if path exists else False
        """
        self.journey = f"{self.journey}\n{text}"
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

    def getBag(self):
        """
            returns item present in the bag
        :return: items in the bag (list)
        """
        return self.bag

    def movingMuseum(self):
        """
            Displaying item and its description on the GUI
        :return:
        """
        # Allowing user only to store 2 items at most
        if len(self.bag) != self.museumBagThresh:

            # only if node isn't visited
            if self.map[self.path[0]][self.path[1]] == 1:

                # displaying item and respective attributes on the GUI
                itemDict = self.articleAndDescription[tuple(self.path)]
                self.tkArtName.configure(text=f"Article Name : {list(itemDict.keys())[0]}")
                self.tkArtDesc.configure(text=f"Article Description : {list(itemDict.values())[0]}")
                self.map[self.path[0]][self.path[1]] = -1
                self.optionText.configure(text="Do you want to put the item in the bag?")
                self.optionNote.configure(text="NOTE: ONLY 2 ITEMS CAN BE PLACED IN THE BAG!")
                plt.imshow(self.map, cmap="jet")
                plt.savefig("game_images/map.png")
                self.img = tk.PhotoImage(file='game_images/map.png')
                self.imgLabel.configure(image=self.img)

                # making sure only 2 items are present in the bag
                if len(self.bag) != self.museumBagThresh:
                    self.yes = tk.Button(text="yes", command=self.addItem)
                    self.yes.grid(rows=12, column=2)

            # showing a yes button only on positions where items are present
            elif self.map[self.path[0]][self.path[1]] != 1:
                if self.yes.winfo_exists() == 1:
                    self.yes.destroy()

        # exiting the museum
        else:
            tk.Label(text="Exiting the museum! (in 3 seconds)").grid(rows=13, columns=2)
            self.win.destroy()
            self.win.mainloop()

    def addItem(self):
        """
            Function for adding item if the correct path is entered and item exists at current location
        :return: None
        """

        # updating the journey
        self.journey = f"{self.journey}\nyes"

        # Item added only if it is less than the threshold
        if len(self.bag) != self.museumBagThresh:
            # avoiding repetitions of items
            if list(self.articleAndDescription[tuple(self.path)].keys())[0] in self.bag:
                pass
            else:
                # Inserting item in the bag
                self.bag.append(list(self.articleAndDescription[tuple(self.path)].keys())[0])
                self.bagItems.configure(text="Items in the bag : " + str(self.bag))
                if len(self.bag) == 2:
                    tk.Label(text="Exiting the museum! (in 3 seconds)").grid(rows=13, column=2)
                    self.win.destroy()
                    self.win.mainloop()
        else:
            # exiting
            tk.Label(text="Two items stolen! exiting the museum (in 3 seconds)!")
            time.sleep(3)
            self.win.destroy()
            self.win.mainloop()

    def returnJourney(self):
        """
            Function for returning the overall journey for this level
        :return: user journey for this level
        """
        return self.journey
