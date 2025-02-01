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
    file.close()

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
mainframe["borderwidth"] = 2
mainframe["relief"] = "sunken"
mainframe.pack()

armouredVestsClicked = StringVar()
armouredVestsClicked.set(aVestsNames[0])

armouredVestsDrop = OptionMenu(mainframe, armouredVestsClicked, *aVestsNames)
armouredVestsDrop.pack()

root.update()

# starts loop
root.mainloop()
