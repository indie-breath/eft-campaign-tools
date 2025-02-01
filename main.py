import json
from tkinter import *
from tkinter import _setit, ttk

# globals

A_VESTS = []
A_VESTS_NAMES = []
A_PLATES = []
A_PLATES_FRONT_NAMES = [""]
A_PLATES_BACK_NAMES = [""]
A_PLATES_SIDES_NAMES = [""]


# put functions here
def getArmourVests():
    with open("data/armourVests.json", "r") as file:
        for line in file:
            A_VESTS.append(json.loads(line))

    for item in A_VESTS:
        A_VESTS_NAMES.append(item["name"])


def getArmourPlates():
    with open("data/armourPlates.json", "r") as file:
        for line in file:
            A_PLATES.append(json.loads(line))


getArmourVests()
getArmourPlates()


def updateArmourVests():
    currentAVest = armouredVestsClicked.get()
    vestJSON = {}

    # TODO: make better
    for x in A_VESTS:
        if x["name"] == currentAVest:
            vestJSON = x
            break

    A_PLATES_FRONT_NAMES = []
    for frontPlate in A_PLATES:
        tmp = False
        for x in vestJSON["fits"][0]["fits"]:
            tmp = x in frontPlate["fits"]
            if tmp:
                break

        if tmp:
            A_PLATES_FRONT_NAMES.append(frontPlate["name"])

    A_PLATES_BACK_NAMES = []
    for backPlate in A_PLATES:
        tmp = False
        for x in vestJSON["fits"][1]["fits"]:
            tmp = x in backPlate["fits"]
            if tmp:
                break

        if tmp:
            A_PLATES_BACK_NAMES.append(backPlate["name"])

    A_PLATES_SIDES_NAMES = []
    for sidePlate in A_PLATES:
        tmp = False
        for x in vestJSON["fits"][2]["fits"]:
            tmp = x in sidePlate["fits"]
            if tmp:
                break

        if tmp:
            A_PLATES_SIDES_NAMES.append(sidePlate["name"])

    if not A_PLATES_FRONT_NAMES:
        A_PLATES_FRONT_NAMES = [""]
    if not A_PLATES_BACK_NAMES:
        A_PLATES_BACK_NAMES = [""]
    if not A_PLATES_SIDES_NAMES:
        A_PLATES_SIDES_NAMES = [""]

    armouredPlatesFrontClicked.set(A_PLATES_FRONT_NAMES[0])
    armouredPlatesBackClicked.set(A_PLATES_BACK_NAMES[0])
    armouredPlatesSidesClicked.set(A_PLATES_SIDES_NAMES[0])

    armouredPlatesFrontDrop["menu"].delete(0, "end")
    for x in A_PLATES_FRONT_NAMES:
        armouredPlatesFrontDrop["menu"].add_command(
            label=x, command=_setit(armouredPlatesFrontClicked, x)
        )
    armouredPlatesBackDrop["menu"].delete(0, "end")
    for x in A_PLATES_BACK_NAMES:
        armouredPlatesBackDrop["menu"].add_command(
            label=x, command=_setit(armouredPlatesBackClicked, x)
        )
    armouredPlatesSidesDrop["menu"].delete(0, "end")
    for x in A_PLATES_SIDES_NAMES:
        armouredPlatesSidesDrop["menu"].add_command(
            label=x, command=_setit(armouredPlatesSidesClicked, x)
        )

    root.update()


# inits main windows
root = Tk()
# sets window title
root.title("Testing")

# put display inits here
mainframe = ttk.Frame(root)
mainframe.pack()

# armoured vests drop-down menu
armouredVestsClicked = StringVar()
armouredVestsClicked.set(A_VESTS_NAMES[0])

armouredVestsDrop = OptionMenu(mainframe, armouredVestsClicked, *A_VESTS_NAMES)
armouredVestsDrop.pack()

armouredVestsUpdate = Button(
    mainframe, text="Update Armoured Vests", command=updateArmourVests
)
armouredVestsUpdate.pack()

# armoured plates drop-down menus
armouredPlatesFrontClicked = StringVar()
armouredPlatesFrontClicked.set(A_PLATES_FRONT_NAMES[0])

armouredPlatesBackClicked = StringVar()
armouredPlatesBackClicked.set(A_PLATES_BACK_NAMES[0])

armouredPlatesSidesClicked = StringVar()
armouredPlatesSidesClicked.set(A_PLATES_SIDES_NAMES[0])

armouredPlatesFrontDrop = OptionMenu(
    mainframe, armouredPlatesFrontClicked, *A_PLATES_FRONT_NAMES
)
armouredPlatesFrontDrop.pack()

armouredPlatesBackDrop = OptionMenu(
    mainframe, armouredPlatesBackClicked, *A_PLATES_BACK_NAMES
)
armouredPlatesBackDrop.pack()

armouredPlatesSidesDrop = OptionMenu(
    mainframe, armouredPlatesSidesClicked, *A_PLATES_SIDES_NAMES
)
armouredPlatesSidesDrop.pack()

# starts loop
root.mainloop()
