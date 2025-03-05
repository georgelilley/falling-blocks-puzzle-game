class Random_Shape:

    def __init__(self):
        self.orange_ricky = 'Orange_Ricky' #Orange_Ricky()
        self.hero = 'hero' # Hero()

        self.possible_pieces = []
        self.possible_pieces.append(self.orange_ricky)
        self.possible_pieces.append(self.hero)

    def print_list(self):
        print(self.possible_pieces)
