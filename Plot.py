class Plot:

    def __init__(self, position, item):
        self.position = position
        self.item = item
        self.occupied = False
        #self.is_watered = false

    def display(self):
        return self.item.get_output()

    def set_item(self, item):
        self.item = item
        self.occupied = True

    def is_occupied(self):
        return self.occupied

    def get_item(self):
        return self.item

    def get_position(self):
        return self.position

    #def return_self(self, position):
