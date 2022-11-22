"""
    Level 2: Home

    A class Home is created in order to allow the user to
    examine the artifacts stolen from the Museum and take
    appropriate decisions to reach the correct location.

"""

import tkinter as tk
import matplotlib
matplotlib.use('Agg')
from PIL import Image, ImageTk

class Home:
    def __init__(self,  bagAndDesc):
        """
            Constructor method which initialises the variables required to
            complete this level.
        :param bagAndDesc: Bag and description of all its items.
        """
        self.journey = ''

        # Items and their description
        self.bagAndDesc = bagAndDesc
        self.bag = sorted(list(self.bagAndDesc.keys()))
        self.bag.reverse()

        # initializing the GUI window
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)

        # initialising variables required for this level
        self.location = tk.Label(self.win, text="Chapter 2 (Location : Home)")
        self.objective = tk.Label(self.win, text="Objective: to examine the articles stolen from the museum.")
        self.mapDesc = bagAndDesc["map"]
        self.coinDesc = bagAndDesc["byzantine coin"]

        # creating labels for instructions and images
        self.instructions_1 = tk.Label(self.win, text='')
        self.instructions_2 = tk.Label(self.win, text="")
        self.img_map = ImageTk.PhotoImage(Image.open(f'images/map.png').resize((300, 200)))
        self.task = tk.Label(self.win, image=self.img_map)

        # putting the widgets on the frame
        self.selection = tk.Label(self.win, text="")
        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(row=0, column=0)
        self.location.grid(row=0, column=2, columnspan=4)
        self.objective.grid(row=1, column=2, columnspan=4)
        self.task.grid(row=2, column=2, columnspan=4)
        self.instructions_1.grid(row=3, column=2, columnspan=4)
        self.instructions_2.grid(row=4, column=2, columnspan=4)

        # calling the function for simulation of the room
        self.flame()
        self.selection.grid(row=7, column=2, columnspan=4)
        self.win.mainloop()

    def item_selection(self, text):
        """
            Function used for validation of item chosen by the user
        :param text: passing button clicked by the user
        :return: None
        """
        self.journey = f"{self.journey}\n{text}"
        variable = self.var.get()
        if variable == 1:
            self.selection.configure(text="Correct destination! (Exiting room in 3 seconds)")
            self.win.destroy()
        else:
            self.selection.configure(text="Incorrect Destination!")

    def flame(self):
        """
            Displaying images and options on the GUI
        :return: None
        """

        # instructions and items
        self.instructions_1.configure(text=f"Map : {self.mapDesc}")
        self.instructions_2.configure(text=f"Coin : {self.coinDesc}")

        # images and options
        self.img_mad = ImageTk.PhotoImage(Image.open('images/madagascar.png').resize((200, 200)))
        self.img_mad_label = tk.Label(image=self.img_mad)
        self.img_mad_label.grid(row=5, column=2)

        self.img_sk = ImageTk.PhotoImage(Image.open('images/south korea.png').resize((200, 200)))
        self.img_sk_label = tk.Label(image=self.img_sk)
        self.img_sk_label.grid(row=5, column=3)

        self.img_uk = ImageTk.PhotoImage(Image.open('images/uk.png').resize((200, 200)))
        self.img_uk_label = tk.Label(image=self.img_uk)
        self.img_uk_label.grid(row=5, column=4)

        self.img_nepal = ImageTk.PhotoImage(Image.open('images/nepal.gif').resize((200, 200)))
        self.img_nepal_label = tk.Label(image=self.img_nepal)
        self.img_nepal_label.grid(row=5, column=5)

        # accessing the values of items enter by the user
        self.var = tk.IntVar()

        # Dictionary to create multiple buttons
        values = {"Madagascar": "2",
                  "South Korea": "4",
                  "United Kingdom": "3",
                  "Nepal": "1"}

        for i, (text, value) in enumerate(values.items()):
            tk.Radiobutton(self.win, text=text, variable=self.var, value=value, command=lambda : self.item_selection(text)).grid(row=6, column=i + 2)

        tk.Label(self.win, text="(On selection of correct item, you will be directed to the next page!)").grid(row=8, column=2, columnspan=4)

    def returnJourney(self):
        """
            Returning the user journey for this level
        :return: user journey for this level
        """
        return self.journey