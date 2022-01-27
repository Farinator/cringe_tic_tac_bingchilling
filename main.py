# Log button presses. If the modulus is 0, then x is logged. If the modulus is 1, them o is logged
import tkinter as tk
import time
# import numpy as np
from PIL import Image, ImageTk

import tkinter.messagebox

button_sizex = 320
button_sizey = 301

global click_count
click_count = 0
import tkinter.messagebox

# Initializing Tkinter module
root = tk.Tk()
root.title("Social Credit?")
# Setting up grid
root.rowconfigure((0, 1, 2), weight=1)
root.columnconfigure((0, 1, 2), weight=1)



gboard = [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
]

btnboard = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# COnfiguring Images and Image display
images =[]
#Generating the background Null image

theWok1 = Image.open("the_wok.png")
theWok2 = Image.open("the_wok_copy.png")
images.append(ImageTk.PhotoImage(theWok1))
images.append(ImageTk.PhotoImage(theWok2))
images.append(ImageTk.PhotoImage(Image.new(mode="RGB", size=(button_sizex,button_sizey), color=(240, 240, 240))))
img_display = ImageTk.PhotoImage(theWok1)




# configuring buttons



def returnWinner():
    for row in gboard:
        if row[0] !=3 :
            for x in range(len(row)-1):
                if row[x] != row[x+1]:
                    break
            else:
                return row[0]

    for column in range(len(gboard[0])):
        if gboard[0][column] != 3:
            for i in range(len(gboard[0])-1):
                if gboard[i][column] != gboard[i+1][column]:
                    break
            else:
                return gboard[0][column]

    if gboard[0][0]!= 3:
        for x in range(len(gboard)-1):
            if gboard[x][x] != gboard [x+1][x+1]:
                break
        else:
            return gboard[0][0]

    if gboard[0][-1] != 3:
        for y in range(len(gboard)-1):
            if gboard[i][-i-1] != gboard[i+1][-i-2]:
                break
        else:
            return gboard[0][-1]


    return 3





def update_grid(x,y):
    if gboard[y][x] == 3:
        global click_count
        click_count = click_count+1

        if click_count%2 == 0:
            gboard[y][x] = 0
        elif click_count%2 == 1:
            gboard[y][x] = 1

        btnstate = gboard[y][x]

        btnboard[y][x].config(image=images[btnstate])

        winner = returnWinner()

        print(gboard)
        if winner != 3:
            print(f"The winner is player {winner}")
            if winner == 0:
                winner = " +100000 social credit to Deepfried THE WOK \n -1000 Social credit to the loser,Xi is angry!!"
            elif winner ==1:
                winner = " +100000 social credit to THE OG WOK \n -1000 Social credit to the loser,time for execution!!!!"
            tkinter.messagebox.showinfo(title= "Winner!", message=winner)



def mkbutton(x,y):
 btn = tk.Button(root, text= 'test', bd=5, image=images[2], command= lambda: update_grid(x,y))
 btn.grid(row=y, column=x)
 btnboard[y][x] = btn


for y in range(len(gboard)):
    for x in range(len(gboard)):
        mkbutton(x,y)








tk.mainloop()


