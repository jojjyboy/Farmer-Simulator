from Plot import Plot
from Item import Item
from Plant import Plant

alphabet = {
    '0' : 'A', '1' : 'B',
    '2' : 'C', '3' : 'D',
    '4' : 'E', '5' : 'F',
    '6' : 'G', '7' : 'H',
    '8' : 'I', '9' : 'J',

    '10' : 'K', '11' : 'L',
    '12' : 'M', '13' : 'N',
    '14' : 'O', '15' : 'P',
    '16' : 'Q', '17' : 'R',
    '18' : 'S', '19' : 'T',
    '20' : 'U', '21' : 'V',
    '22' : 'W', '23' : 'X',
    '24' : 'Y', '25' : 'Z'
}

indices = {
    'A' : 0, 'B' : 1,
    'C' : 2, 'D' : 3,
    'E' : 4, 'F' : 5,
    'G' : 6, 'H' : 7,
    'I' : 8, 'J' : 9,

    'K' : 10, 'L' : 11,
    'M' : 12, 'N' : 13,
    'O' : 14, 'P' : 15,
    'Q' : 16, 'R' : 17,
    'S' : 18, 'T' : 19,
    'U' : 20, 'V' : 21,
    'W' : 22, 'X' : 23,
    'Y' : 24, 'Z' : 25
}

class Farm:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plots = [[] for x in range(self.height + 1)]
        self.positions = []


        for i in range(self.height):
            for j in range(self.width):
                position = alphabet.get(str(j)) + str(i)
                self.positions.append(position)

                self.plots[i].append(Plot(position, Item("~")))
                #print(self.plots[i][j].get_position())

    def get_x(self, position):
        return indices.get(position[0:1])

    def get_y(self, position):
        return int(position[1:2])

    def add(self, position, plant):
        #self.plots.set_item(plant)
        x = self.get_x(position)
        y = self.get_y(position)

        self.plots[y][x].set_item(plant)
        print("You have plotted on: " + position)

        #for i in range(len(self.plots)):
        #    for j in range(len(self.plots[i])):
        #        #print (position + " " + self.plots[i].get_position)
        #        if position == self.plots[i][j].get_position():
        #            self.plots[i][j].set_item(plant)
        #            print("You have plotted on: " + position)

    #def water(self, position):


    def add_all(self, plant):
        for i in range(0, self.width):
            self.plots[i].set_item(plant)
            #self.plots.append(plant)

    def is_valid_area(self, area):
        result = False
        for i in range(self.height):
            for j  in range(self.width):
                if area == self.plots[i][j].get_position():
                    result = True
                elif area == i:
                    result = True

        return result


    def add_row(self):
        if self.height < 10:
            self.height += 1
            self.plots.append([])
            for i in range(self.width):
                position = alphabet.get(str(i)) + str(self.height - 1)
                self.positions.append(position)
                self.plots[self.height - 1].append(Plot(position, Item("~")))

            return "Succesfully added row " + str(self.height - 1)

        else:
            return "Cannot add more rows past 9"


    def add_column(self):
        if self.width < 25:
            self.width += 1
            for i in range(self.height):
                position = alphabet.get(str(self.width - 1)) + str(i)
                self.positions.append(position)
                self.plots[i].append(Plot(position, Item("~")))

        else:
            return "Cannot add more rows past Z"

    #def box_water():
    def box_lengthcheck(self, start, end):
        if start <= end:
            return start, end
        else:
            return end, start

    #Checks within a boxed space if th
    def box_hasplant(self, start_h, end_h, start_w, end_w):
        for i in range(start_h, end_h + 1):
            for j in range(start_w, end_w + 1):
                #position = alphabet.get(str(i)) + str(j)
                if self.plots[i][j].is_occupied():
                    print("Theres is a plant over the plots you have selected, Continue? (Y/N)")
                    return True

    def box_add(self, start, end, plant):
        startx = self.get_x(start)
        starty = self.get_y(start)

        endx = self.get_x(end)
        endy = self.get_y(end)

        start_width, end_width = self.box_lengthcheck(startx, endx)
        start_height, end_height = self.box_lengthcheck(starty, endy)


        #height = end_height - start_height
        #width = end_width - start_width

        #First check if boxes have any plants in them
        if self.box_hasplant(start_height, end_height, start_width, end_width):
            my_input = input("(Y/N) >").upper()
            while my_input != 'Y' or 'N':
                print("Error: Invalid input, try Yes or No (Y/N)")
                my_input = input("(Y/N) >").upper()

            if my_input == 'Y':
                for i in range(start_height, end_height + 1):
                    for j in range(start_width, end_width + 1):
                        position = alphabet.get(str(i)) + str(j)
                        self.add(position, plant)
            else:
                print("Cancelling planting...")


    def display_farm(self):
        print ("")
        row_title = "     "
        for i in range(0, self.width):
            row_title = row_title + alphabet.get(str(i)) + "   "
            #print ("  A   B   C  ")
        print (row_title)

        print ("   " + "~" * (self.width * 4 + 1))


        for i in range(0, self.height):
            print (" " + str(i) + " |", end=" ")
            for j in range(0, self.width):
                print (self.plots[i][j].display() + " |", end=" ")

            print ("\n   " + "~" * (self.width * 4 + 1))

        print ("")

        #print ("\n" + "~" * (self.width * 4 + 1) + "\n")
