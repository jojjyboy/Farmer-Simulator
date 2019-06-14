from Item import Item

class Plant(Item):

    def __init__(self, phases, young, old):
        super().__init__(young)
        self.phases = phases
        self.young  = young
        self.old = old
        self.current_phase = young
        #self.is_ripe = false
