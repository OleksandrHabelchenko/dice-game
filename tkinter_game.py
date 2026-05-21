from tkinter import *  # import tkinter

import random, time  # random choice and time delay

import os  # folder management

import winsound  # Windows sound

import sys  # system parameters

if getattr(sys, 'frozen', False):  # running as exe
    os.chdir(os.path.dirname(sys.executable))  # set folder to exe location
else:  # running as .py
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # set folder to script location

def bros():  # returns random dice image
    x = random.choice(['b.png','b2.png','b3.png',
                       'b4.png','b5.png','b6.png'])  # pick random image
    return x  # return file name

def image(event):  # dice roll animation
    global b1, b2  # global image variables
    winsound.PlaySound('dice_roll.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # play sound
    for i in range(20):  # 20 animation frames
        b1 = PhotoImage(file=(bros()))  # dice 1 image
        b2 = PhotoImage(file=(bros()))  # dice 2 image
        lab1['image'] = b1  # show dice 1
        lab2['image'] = b2  # show dice 2
        root.update()  # refresh window
        time.sleep(0.12)  # pause between frames

root = Tk()  # main window
root.geometry('400x200')  # window size
root.title('Dice Game 😊')  # window title
root.resizable(height=False, width=False)  # fixed size
root.iconphoto(True, PhotoImage(file='iconka.png'))  # app icon
fon = PhotoImage(file='holst.png')  # background image
Label(root, image=fon).pack()  # place background
lab1 = Label(root)  # dice 1 label
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)  # dice 1 position
lab2 = Label(root)  # dice 2 label
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)  # dice 2 position
root.bind('<1>', image)  # mouse click → animation
image('event')  # show dice on startup

root.mainloop()  # start main loop