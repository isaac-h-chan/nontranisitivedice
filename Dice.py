import random
import tkinter as tk
from tkinter import font


# Dice class which contains two class variables 'name' and 'nums' which represent the die's name and faces respectively
class Dice:
    def __init__(self, color):
        if color == 'red':
            self.name = 'Red'
            self.nums = [3, 3, 3, 3, 6, 6]
        elif color == 'blue':
            self.name = 'Blue'
            self.nums = [2, 2, 2, 5, 5, 5]
        else:
            self.name = 'Green'
            self.nums = [1, 4, 4, 4, 4, 4]

    # getter method of name of die
    def getName(self):
        return self.name

    # getter method for list of faces
    def getNums(self):
        return self.nums

    # The method roll takes two dice and randomly selects one face from each die. The values of the faces are then
    # compared and whichever one is greater is deemed the winning die. This is repeated n times and each victory of
    # each die is recorded
    def roll(self, dice, n):
        selfWin, win = 0, 0
        for i in range(n):
            if self.getNums()[random.randint(0, 5)] > dice.getNums()[random.randint(0, 5)]:
                selfWin += 1
            else:
                win += 1
        return self, dice, selfWin, win


def main():
    red = Dice('red')
    blue = Dice('blue')
    green = Dice('green')

    def execute1():
        cache = red.roll(green, int(spin1.get()))
        updateLab(cache)

        drawPie('RED', 'GREEN', cache[2], cache[3])

    def execute2():
        cache = green.roll(blue, int(spin1.get()))
        updateLab(cache)
        drawPie('GREEN', 'BLUE', cache[2], cache[3])

    def execute3():
        cache = blue.roll(red, int(spin1.get()))
        updateLab(cache)
        drawPie('BLUE', 'RED', cache[2], cache[3])

    def updateLab(cache):
        name1 = cache[0].getName()
        name2 = cache[1].getName()
        lab1["text"] = name1 + ': ' + str(cache[2]) + '\n' + name2 + ': ' + str(cache[3]) + '\n\n'
        if cache[2] == cache[3]:
            lab1['text'] += 'Tie!'
        elif cache[2] > cache[3]:
            lab1['text'] += name1 + ' wins!'
        else:
            lab1['text'] += name2 + ' wins!'

    def drawPie(color1, color2, x, y):
        if x == 0 or y == 0:
            if x == 0:
                x = 1
                y = 359
                color1 = color2
            else:
                y = 1
                x = 359
                color2 = color1
        elif x > y:
            x = 360*x/float(x+y)
            y = 360-x
        elif y > x:
            y = 360 * y / float(x + y)
            x = 360 - y
        else:
            x, y = 180, 180
        can1.create_arc((2, 2, 148, 148), fill=color1, start=0, extent=x, outline=color1)
        can1.create_arc((2, 2, 148, 148), fill=color2, start=x, extent=y, outline=color2)

    root = tk.Tk()
    root.title('Non-transitive Dice')
    root.resizable(width=False, height=False)

    frm1 = tk.Frame(master=root)
    frm1.grid(row=0, column=0, padx=10, pady=10)
    frm2 = tk.Frame(master=root)
    frm2.grid(row=1, column=0, padx=10)
    frm3 = tk.Frame(master=frm2)
    frm3.grid(row=0, column=0, padx=10, pady=10)
    frm4 = tk.Frame(master=frm2)
    frm4.grid(row=0, column=2, padx=10, pady=10)

    button1 = tk.Button(master=frm1, text='RED vs GREEN', command=execute1, font=font.Font(size=15))
    button2 = tk.Button(master=frm1, text='GREEN vs BLUE', command=execute2, font=font.Font(size=15))
    button3 = tk.Button(master=frm1, text='BLUE vs RED', command=execute3, font=font.Font(size=15))
    button1.grid(row=0, column=1, padx=60)
    button2.grid(row=0, column=0, padx=30)
    button3.grid(row=0, column=2, padx=30)

    lab2 = tk.Label(master=frm3, text='# of Rolls', font=font.Font(size=20))
    lab2.grid(row=0, column=0)
    lab3 = tk.Label(master=frm4, text='Wins', font=font.Font(size=20))
    lab3.grid(row=0, column=0)

    spin1 = tk.Spinbox(master=frm3, width=10, from_=1, to=10000, font=font.Font(size=20))
    spin1.grid(row=1, column=0)

    lab1 = tk.Label(master=frm2, text='Choose to Simulate', width=15, height=4, font=font.Font(size=20))
    lab1.grid(row=0, column=1, padx=30)

    lab4 = tk.Label(master=root, text='Green: 1/4/4/4/4/4     Blue: 2/2/2/5/5/5     Red: 3/3/3/3/6/6')
    lab4.grid(row=2, column=0, pady=5)

    can1 = tk.Canvas(master=frm4, width=150, height=150)
    can1.grid(row=1, column=0)

    root.mainloop()


main()
