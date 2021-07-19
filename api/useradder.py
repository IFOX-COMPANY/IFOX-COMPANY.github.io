from tkinter import *
from json import *

f = open('textfile.txt', 'r+')
window = Tk()
userlbl = Label(window, text="Player Name")
userentry = Entry(window)
capelbl = Label(window, text="Cape URL")
capeentry = Entry(window)
#add = Button(window, text ="Add Player Cape", command=addcape)

userlbl.pack()
userentry.pack()
capelbl.pack()
capeentry.pack()

def addcape():
    print(f.read())
    f.write(f.read() - 1 + userentry.get() + ": " + capeentry.get())
    f.close()