"""
    Level 3: Market

    Class Market is created which is used to make the user
    buy appropriate items from the market with respect to the
    various probable obstacles during their expedition.

"""
import time
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import copy

class Market:
    def __init__(self, bag):
        """
            Constructor method used to initialise the money allotted,
            the Conditions and items for each of them and the bag which
            has been passed as a parameter.
        :param bag: bag of items from the previous levels
        """
        self.journey = ''
        self.bag = bag
        self.items = []
        self.itemsSelected = {}
        self.money = 100
        self.CondItemsPrice = {'Mountainous region with heavy rain': {"Mountain climbing boots": 10, "Windcheater": 20, "Waterproof jacket": 20, "Swim wear": 90},
                               'Presence of wild animals in the jungle': {"Knife": 10, "Pistol (with 5 bullets)": 30, "Hunting rifle (with 6 bullets)": 40, "Assault rifle (with 50 bullets)": 100},
                               'Presence of rivers and unstable rope bridges': {"Rope": 10, "Ladder": 20, "Motorboat": 150, "Jet ski": 100}}
        self.conditions = list(self.CondItemsPrice.keys())
        self.win = tk.Tk()
        self.win.title("Uncharted")
        self.win.geometry("1000x1000")
        self.win.resizable(False, False)
        self.conditionsAndGame()
        self.win.mainloop()

    def conditionsAndGame(self):
        self.location = tk.Label(self.win, text="Chapter 3 (Location : Market)",bg='black',fg='white')
        self.objective = tk.Label(self.win, text="Objective: With respect to each of the above conditions, you are required to procure items from the market.")
        self.warning = tk.Label(self.win, text = f"NOTE: ONLY {self.money}$ have been allocated for this task.", fg='red')
        self.condition1 = tk.Label(self.win, text = f"{self.conditions[0]}. (HINT: CHOOSE ONLY TWO ITEMS!)",bg='black',fg='white')
        self.condition2 = tk.Label(self.win, text= f"{self.conditions[1]}. (HINT: CHOOSE ONE TO TWO ITEMS!)",bg='black',fg='white')
        self.condition3 = tk.Label(self.win, text= f"{self.conditions[2]}. (HINT: CHOOSE ONLY TWO ITEMS!)",bg='black',fg='white')
        self.tkmoney = tk.Label(self.win, text = f"Money available : {self.money}",bg='black',fg='red')
        self.tkreset = tk.Label(self.win, text = "",fg='red')

        tk.Button(self.win, text="Quit", command=self.win.destroy, bg='#567', fg='White').grid(row=0, column=0)
        self.location.grid(row=0, column=2, columnspan=4)
        self.objective.grid(row=1, column=2, columnspan=4)
        self.warning.grid(row = 3, column = 2, columnspan = 4)
        self.condition1.grid(row = 4, column = 2, columnspan = 4)
        self.tkmoney.grid(row = 0, column = 8, columnspan = 2)
        self.tkreset.grid(row = 1, column = 8, columnspan = 2)

        self.cond_item_price = {i: [f'{item} : {price}' for item, price in self.CondItemsPrice[self.conditions[i]].items()] for i, cond in enumerate(self.conditions)}
        self.condAndItem = {i: [f'{item}' for item, price in self.CondItemsPrice[self.conditions[i]].items()] for i, cond in enumerate(self.conditions)}

        self.condition1CheckButton1 = tk.IntVar()
        self.condition1CheckButton2 = tk.IntVar()
        self.condition1CheckButton3 = tk.IntVar()
        self.condition1CheckButton4 = tk.IntVar()


        c1_button1 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[0][0]}",
                              variable=self.condition1CheckButton1,
                              onvalue=-10,
                              offvalue=0)

        c1_button2 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[0][1]}",
                              variable=self.condition1CheckButton2,
                              onvalue=-20,
                              offvalue=0)

        c1_button3 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[0][2]}",
                              variable=self.condition1CheckButton3,
                              onvalue=-20,
                              offvalue=0)

        c1_button4 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[0][3]}",
                              variable=self.condition1CheckButton4,
                              onvalue=-90,
                              offvalue=0)

        condition1Button = tk.Button(text = "Confirm items", command = lambda : self.printAmount(0),bg='#567', fg='White')

        c1_button1.grid(row = 5, column = 2, columnspan = 4)
        c1_button2.grid(row = 6, column = 2, columnspan = 4)
        c1_button3.grid(row = 7, column = 2, columnspan = 4)
        c1_button4.grid(row = 8, column = 2, columnspan = 4)

        condition1Button.grid(row = 9, column = 2, columnspan = 4)

        self.condition2.grid(row=10, column=2, columnspan=4)

        self.condition2CheckButton1 = tk.IntVar()
        self.condition2CheckButton2 = tk.IntVar()
        self.condition2CheckButton3 = tk.IntVar()
        self.condition2CheckButton4 = tk.IntVar()

        c1_button1 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[1][0]}",
                                    variable=self.condition2CheckButton1,
                                    onvalue=-10,
                                    offvalue=0)

        c1_button2 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[1][1]}",
                                    variable=self.condition2CheckButton2,
                                    onvalue=-30,
                                    offvalue=0)

        c1_button3 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[1][2]}",
                                    variable=self.condition2CheckButton3,
                                    onvalue=-40,
                                    offvalue=0)

        c1_button4 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[1][3]}",
                                    variable=self.condition2CheckButton4,
                                    onvalue=-100,
                                    offvalue=0)

        condition2Button = tk.Button(text="Confirm items", command=lambda : self.printAmount(1) ,bg='#567', fg='White')

        c1_button1.grid(row=11, column=2, columnspan=4)
        c1_button2.grid(row=12, column=2, columnspan=4)
        c1_button3.grid(row=13, column=2, columnspan=4)
        c1_button4.grid(row=14, column=2, columnspan=4)

        condition2Button.grid(row=15, column=2, columnspan=4)

        self.condition3.grid(row=16, column=2, columnspan=4)

        self.condition3CheckButton1 = tk.IntVar()
        self.condition3CheckButton2 = tk.IntVar()
        self.condition3CheckButton3 = tk.IntVar()
        self.condition3CheckButton4 = tk.IntVar()

        c1_button1 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[2][0]}",
                                    variable=self.condition3CheckButton1,
                                    onvalue=-10,
                                    offvalue=0)

        c1_button2 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[2][1]}",
                                    variable=self.condition3CheckButton2,
                                    onvalue=-20,
                                    offvalue=0)

        c1_button3 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[2][2]}",
                                    variable=self.condition3CheckButton3,
                                    onvalue=-150,
                                    offvalue=0)

        c1_button4 = tk.Checkbutton(self.win, text=f"{self.cond_item_price[2][3]}",
                                    variable=self.condition3CheckButton4,
                                    onvalue=-100,
                                    offvalue=0)

        condition3Button = tk.Button(text="Confirm items", command=lambda : self.printAmount(2), bg='#567', fg='White')

        c1_button1.grid(row=18, column=2, columnspan=4)
        c1_button2.grid(row=19, column=2, columnspan=4)
        c1_button3.grid(row=20, column=2, columnspan=4)
        c1_button4.grid(row=21, column=2, columnspan=4)

        condition3Button.grid(row=22, column=2, columnspan=4)

    def destroy_widgets(self):
        for widgets in self.win.winfo_children():
            widgets.destroy()


    def printAmount(self, case):
        self.tkreset.configure(text = "")
        self.journey = f"{self.journey}\nConfirm items"
        if case == 0:
            self.money += self.condition1CheckButton1.get() + self.condition1CheckButton2.get() + self.condition1CheckButton3.get() + self.condition1CheckButton4.get()
            if self.condition1CheckButton1.get()!= 0:
                self.journey = f"{self.journey}\n{self.condAndItem[0][0]}"
                self.bag.append(self.condAndItem[0][0])
            if self.condition1CheckButton2.get()!= 0:
                self.journey = f"{self.journey}\n{self.condAndItem[0][1]}"
                self.bag.append(self.condAndItem[0][1])
            if self.condition1CheckButton3.get()!= 0:
                self.journey = f"{self.journey}\n{self.condAndItem[0][2]}"
                self.bag.append(self.condAndItem[0][2])
            if self.condition1CheckButton4.get()!= 0:
                self.journey = f"{self.journey}\n{self.condAndItem[0][3]}"
                self.bag.append(self.condAndItem[0][3])
        elif case == 1:
            self.money += self.condition2CheckButton1.get() + self.condition2CheckButton2.get() + self.condition2CheckButton3.get() + self.condition2CheckButton4.get()
            if self.condition2CheckButton1.get()!= 0:
                self.bag.append(self.condAndItem[1][0])
                self.journey = f"{self.journey}\n{self.condAndItem[1][0]}"
            if self.condition2CheckButton2.get()!= 0:
                self.bag.append(self.condAndItem[1][1])
                self.journey = f"{self.journey}\n{self.condAndItem[1][1]}"
            if self.condition2CheckButton3.get()!= 0:
                self.bag.append(self.condAndItem[1][2])
                self.journey = f"{self.journey}\n{self.condAndItem[1][2]}"
            if self.condition2CheckButton4.get()!= 0:
                self.bag.append(self.condAndItem[1][3])
                self.journey = f"{self.journey}\n{self.condAndItem[1][3]}"
        elif case == 2:
            self.money += self.condition3CheckButton1.get() + self.condition3CheckButton2.get() + self.condition3CheckButton3.get() + self.condition3CheckButton4.get()
            if self.condition3CheckButton1.get()!= 0:
                self.bag.append(self.condAndItem[2][0])
                self.journey = f"{self.journey}\n{self.condAndItem[2][0]}"
            if self.condition3CheckButton2.get()!= 0:
                self.bag.append(self.condAndItem[2][1])
                self.journey = f"{self.journey}\n{self.condAndItem[2][1]}"
            if self.condition3CheckButton3.get()!= 0:
                self.bag.append(self.condAndItem[2][2])
                self.journey = f"{self.journey}\n{self.condAndItem[2][2]}"
            if self.condition3CheckButton4.get()!= 0:
                self.bag.append(self.condAndItem[2][3])
                self.journey = f"{self.journey}\n{self.condAndItem[2][3]}"
        self.tkmoney.configure(text=f"Money available : {self.money}")
        if self.money < 0:
            self.money = 100
            self.bag = ["Byzantine Coin", "Map"]
            self.tkreset.configure(text = "Incorrect items! Resetting!")
        elif self.money == 0:
            if (len(self.bag) == 8 or len(self.bag) == 7):
                self.win.destroy()
            else:
                self.money = 100
                self.bag = ["Byzantine Coin", "Map"]
                self.tkreset.configure(text = "Incorrect items! Resetting!")

    def returnJourney(self):
        return self.journey