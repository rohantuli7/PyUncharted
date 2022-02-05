"""
    Level 5: part of the jungle with animals

    Class JungleExpedition is created which depicts a series
    of obstacles faced in the jungle with respect and the respective
    actions possible.

    SciView not required to complete this level.
"""

import time
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import copy

class JungleExpedition:
    def __init__(self, bag):
        """
            Constructor initialising all required variables
            and updating the bag parameter
        :param bag: bag of items
        """
        self.journey = ''
        self.bag = [i.lower() for i in bag]
        # Setting the number of bullets available to the user
        self.isPistol = False
        if 'pistol (with 5 bullets)' in self.bag:
            self.bullets = 5
            self.isPistol = True
        elif "hunting rifle (with 6 bullets)":
            self.bullets = 6
            self.isPistol = False

        # Obstacles
        self.obstacleDesc = ["A WILD BEAR IS TRYING TO ATTACK YOU!",
                             "A POISONOUS COBRA HAS APPEARED IN FRONT OF YOU!",
                             "A HERD OF HYENAS ARE CHASING YOU!"]


        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(True, True)

        self.location = tk.Label(self.win, text="Chapter 5 (Location : part of the jungle with animals)",bg='black', fg='White')
        self.objective = tk.Label(self.win, text="Objective : Beware of your surroundings and react appropriately to any animal sightings!\n")
        self.caution = tk.Label(self.win, text = "You have entered the jungle with presence of wild animals!",fg='red')
        self.img_bear = ImageTk.PhotoImage(Image.open(f'GUI images/bear.png').resize((300, 200)))
        self.condition_image1 = tk.Label(self.win, image = self.img_bear)
        self.condition1 = tk.Label(self.win, text=self.obstacleDesc[0])
        self.conditionCase1 = tk.Label(self.win, text = '')
        self.conditionButton1_1 = tk.Button(self.win, text = "Shoot the bear!", command  = lambda  : self.killBear(), bg='#567', fg='White')
        self.conditionButton1_2 = tk.Button(self.win, text= "Fight the bear!", bg='#567', fg='White', command = lambda : self.incorrectInput(self.conditionCase1, "You have been killed by the bear!", "Fight the bear!"))
        self.condition1_label = tk.Label(self.win, text = "")

        self.selection = tk.Label(self.win, text="")
        tk.Button(self.win, text="Quit", command=self.win.destroy, bg='#567', fg='White').grid(row=0, column=0)
        self.location.grid(row=0, column=2, columnspan=4)
        self.objective.grid(row=1, column=2, columnspan=4)
        self.caution.grid(row=2, column=2, columnspan=4)
        self.condition_image1.grid(row=3, column=2, columnspan=4)
        self.condition1.grid(row=4, column=2, columnspan=4)
        self.conditionCase1.grid(row = 5, column = 2, columnspan = 4)
        self.conditionButton1_1.grid(row = 6, column = 2, columnspan = 2)
        self.conditionButton1_2.grid(row = 6, column = 4, columnspan = 2)

        self.win.mainloop()

    def incorrectInput(self, button, ip, text, flag = 0):
        self.journey = f"{self.journey}\n{text}"
        if "hunting rifle (with 6 bullets)" in self.bag and self.bullets!=1:
            button.configure(text=ip)
            self.bullets = 6
        if "pistol (with 5 bullets)" in self.bag:
            button.configure(text=ip)
            self.bullets = 5
        if flag == 1:
            button.configure(text=ip)


    def killBear(self):
        self.journey = f"{self.journey}\nShoot the bear!"
        if self.isPistol:
            if self.bullets>1:
                self.bullets -= 1
                self.conditionCase1.configure(text = f"YOU SHOT THE BEAR BUT IT ISNT DEAD (BULLETS = {self.bullets})")
            elif self.bullets == 1:
                self.bullets -=1
                self.conditionCase1.configure(text = f"THE BEAR IS DEAD! (Discarding the pistol)")
                self.bag.remove('pistol (with 5 bullets)')
                self.condition1_label.configure(text = f"Walking in the jungle (for 3 seconds)")
                time.sleep(3)
                self.Snake()
            else:
                self.conditionCase1.configure(text = "MISSION COMPLETE! MOVE AHEAD!")
        else:
            if self.bullets>2:
                self.bullets -= 1
                self.conditionCase1.configure(text=f"YOU SHOT THE BEAR BUT IT ISNT DEAD (BULLETS = {self.bullets})")
            elif self.bullets == 2:
                self.bullets -= 1
                self.conditionCase1.configure(text=f"THE BEAR IS DEAD!")
                self.condition1_label.configure(text=f"Walking in the jungle (for 3 seconds)")
                time.sleep(3)
                self.Snake()
            else:
                self.conditionCase1.configure(text="MISSION COMPLETE! MOVE AHEAD!")

    def Snake(self):
        self.img_snake = ImageTk.PhotoImage(Image.open(f'GUI images/snake.png').resize((300, 200)))
        self.condition_image2 = tk.Label(self.win, image=self.img_snake)
        self.condition2 = tk.Label(self.win, text=self.obstacleDesc[1])
        self.conditionCase2 = tk.Label(self.win, text='')
        if self.isPistol:
            self.conditionButton2_1 = tk.Button(self.win, bg='#567', fg='White',text="Stab the snake with the knife!", command=lambda: self.killSnake())
        else:
            self.conditionButton2_1 = tk.Button(self.win, text="Shoot the snake with the rifle", bg='#567', fg='White', command=lambda: self.killSnake())
        self.conditionButton2_2 = tk.Button(self.win, text="Fight the snake!", bg='#567', fg='White', command=lambda: self.incorrectInput(self.conditionCase2, "You have been poisoned by the snake!", "Fight the snake!", flag = 1))
        self.condition2_label = tk.Label(self.win, text="")
        tk.Label(self.win, text = "").grid(row=8, column=2, columnspan=4)
        self.condition_image2.grid(row=9, column=2, columnspan=4)
        self.condition2.grid(row=10, column=2, columnspan=4)
        self.conditionCase2.grid(row=11, column=2, columnspan=4)
        self.conditionButton2_1.grid(row=12, column=2, columnspan=2)
        self.conditionButton2_2.grid(row=12, column=4, columnspan=2)

    def killSnake(self):
        if self.isPistol:
            self.journey = f"{self.journey}\nStab the snake with the knife"
            if 'knife' in self.bag:
                self.conditionCase2.configure(text=f"You killed the snake with the knife!")
                self.bag.remove("knife")
                self.condition2_label.configure(text=f"Walking in the jungle (for 3 seconds)")
                time.sleep(3)
                self.Hyenas()
            else:
                self.conditionCase2.configure(text=f"Mission complete! Move ahead!")
        else:
            self.journey = f"{self.journey}\nShoot the snake with the rifle"
            if "hunting rifle (with 6 bullets)" in self.bag:
                self.conditionCase2.configure(text=f"You killed the snake with the rifle! (Discarding rifle)")
                self.bag.remove("hunting rifle (with 6 bullets)")
                self.condition2_label.configure(text=f"Walking in the jungle (for 3 seconds)")
                time.sleep(3)
                self.Hyenas()
            else:
                self.conditionCase2.configure(text=f"Mission complete! Move ahead!")


    def Hyenas(self):
        self.img_hyena = ImageTk.PhotoImage(Image.open(f'GUI images/hyenas.png').resize((300, 200)))
        self.condition_image3 = tk.Label(self.win, image=self.img_hyena)
        self.condition3 = tk.Label(self.win, text=self.obstacleDesc[2])
        self.conditionCase3 = tk.Label(self.win, text='')
        self.conditionButton3_1 = tk.Button(self.win, text="Run from the hyenas!", bg='#567', fg='White',  command= lambda : self.win.destroy())
        self.conditionButton3_2 = tk.Button(self.win, text="Fight the hyenas", bg='#567', fg='White', command = lambda: self.incorrectInput(self.conditionCase3, "You have been killed by the hyenas!!","Fight the hyenas", flag= 1))
        self.condition3_label = tk.Label(self.win, text="")


        tk.Label(self.win, text="").grid(row=13, column=2, columnspan=4)
        self.condition_image3.grid(row=14, column=2, columnspan=4)
        self.condition3.grid(row=15, column=2, columnspan=4)
        self.conditionCase3.grid(row=16, column=2, columnspan=4)
        self.conditionButton3_1.grid(row=17, column=2, columnspan=2)
        self.conditionButton3_2.grid(row=17, column=4, columnspan=2)

    def getBag(self):
        return self.bag

    def returnJourney(self):
        return f"{self.journey}\nRun from the hyenas!"