#Fuck my ass daddy
from Plot   import Plot
from Plant  import Plant
from Farm   import Farm
from Item   import Item


import cmd
import sys
import os

farm_width = 9
farm_height = 4

class User:
    def __init__(self):
        self.inventory = []
        self.energy = 100

farmer = User()

plants = {
    'BLUEBERRY'   :  Plant(3, 'b', 'B'),
    'STRAWBERRY'  :  Plant(6, 's', 'S')
}

'''
commands = {
    ''

}
'''
def make_title():
    print(" _ _ _       _                           _        ")
    print("| | | | ___ | | ___  ___ ._ _ _  ___   _| |_ ___  ")
    print("| | | |/ ._>| |/ | '/ . \| ' ' |/ ._>   | | / . \ ")
    print("|__/_/ \___.|_|\_|_.\___/|_|_|_|\___.   |_| \___/ ")
    print(" ______      _____  __  __ ______ _____       _____ _                 _       _             ")
    print("|  ____/\   |  __ \|  \/  |  ____|  __ \     / ____(_)               | |     | |            ")
    print("| |__ /  \  | |__) | \  / | |__  | |__) |   | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ ")
    print("|  __/ /\ \ |  _  /| |\/| |  __| |  _  /     \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|")
    print("| | / ____ \| | \ \| |  | | |____| | \ \     ____) | | | | | | | |_| | | (_| | || (_) | |   ")
    print("|_|/_/    \_\_|  \_\_|  |_|______|_|  \_\   |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   \n")

    print("To get started type out \'COMMANDS\' and then \'DISPLAY\' to see your farm!\n")

def make_farm():
    global farm
    farm = Farm(farm_width, farm_height)


def get_input():
    return input(">").upper()


def update():
    print("   __ __              _               ___                 ")
    print("  |  \  \ ___  ___  _| | ___  _ _ _  | __>___  _ _ ._ _ _ ")
    print("  |     |/ ._><_> |/ . |/ . \| | | | | _><_> || '_>| ' ' |")
    print("  |_|_|_|\___.<___|\___|\___/|__/_/  |_| <___||_|  |_|_|_|")
    #print("")
    farm.display_farm()
    print("    __|_ _ ._ _ o._  _ ")
    print("   _\ | (_|| | ||| |(_|")
    print("   _____________________________")
    print("  |#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| 100%")
    print("   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    #farm.display_farm()
    print("\nWhat would you like to do?")

    while (True):
        current_command = get_input()

        if current_command == "DISPLAY":
            farm.display_farm()

        elif current_command == "PLANT":
            command_plant()

        elif current_command == "ADDROW":
            print(farm.add_row())

        elif current_command == "ADDCOLUMN":
            farm.add_column()

        elif current_command == "Q":
            sys.exit()

        elif current_command == "PLANTFROM":
            command_plantfrom()

        else:
            print("Error: Invalid Command")



def command_plant():
    print("What plant would you like to plant?")
    plant = get_input()

    if plant in plants.keys():
        print("Where would you like to plant?")
        position = get_input()
        if farm.is_valid_area(position):
            farm.add(position, plants.get(plant, "Not Valid"))
        else:
            print("ERROR: Invalid Position")
    else:
        print("ERROR: Invalid Plant")


def command_plantfrom():
    print("What is your starting position?")
    start = get_input()
    print(start)
    if farm.is_valid_area(start):
        print("What is your ending position?")
        end = get_input()
        if farm.is_valid_area(end):
            print("What would you like to plant?")
            #show_inventory()
            plant = get_input()
            if plant in plants.keys():
                farm.box_add(start, end, plants.get(plant))
            else:
                print("Error: Invalid Plant")
        else:
            print("Error: Invalid Position")
    else:
        print("Error: Invalid Position")


make_title()
make_farm()
update()


############### Farm ###############

#     A   B   C   D   E   F   G   H
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1 | ~ | ~ | p | p | p | c | c | c |
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2 | b | b | B | B | B | w | w | w |
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3 | s | s | s | s | s | s | w | w |
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Examples: s = strawberry, b = blueberry, w = wheat, c == corn
