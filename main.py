import json
from tkinter import *
from tkinter import ttk


# put functions here
def getArmourVests():
    global aVests
    aVests = []
    with open("data/armourVests.json", "r") as file:
        for line in file:
            aVests.append(json.loads(line))

    global aVestsNames
    aVestsNames = []
    for item in aVests:
        aVestsNames.append(item["name"])


def getArmourPlates():
    global aPlates
    aPlates = []
    with open("data/armourVests.json", "r") as file:
        for line in file:
            aPlates.append(json.loads(line))


getArmourVests()
getArmourPlates()


# inits main windows
root = Tk()
# sets window title
root.title("Testing")

# put display inits here
mainframe = ttk.Frame(root)
mainframe.pack()

# armoured vests drop-down menu
armouredVestsClicked = StringVar()
armouredVestsClicked.set(aVestsNames[0])

armouredVestsDrop = OptionMenu(mainframe, armouredVestsClicked, *aVestsNames)
armouredVestsDrop.pack()

# starts loop
root.mainloop()
