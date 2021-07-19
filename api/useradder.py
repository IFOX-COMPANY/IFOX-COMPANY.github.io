from tkinter import *
import time

window = Tk()
userlbl = Label(window, text="Player Name")
userentry = Entry(window)
capelbl = Label(window, text="Cape URL")
capeentry = Entry(window)

userlbl.pack()
userentry.pack()
capelbl.pack()
capeentry.pack()

def addcape():
    f = open('capes.json', 'r+')
    contents = f.read().replace("{\n", "")
    contents = contents.replace("\n}", "")
    contents = contents.replace("", "")
    contents = contents + "," + "\n"
    print(contents)
    f.write(f.read().replace("\n}", ""))
    f.close
    quotefile = open('quote.txt')
    quote = quotefile.read()
    quotefile.close()
    f = open('capes.json', 'r+')
    f.write("{\n" + contents + "    " + quote + userentry.get() + quote + ": " + quote + capeentry.get() + quote + "\n}")
    f.close()

        
    
button = Button(window, text="Add Player Cape", command=addcape)
button.pack()
input('Press any key to finish')