from Fight_engine.Class_Angry_Dummy import ClassAngryDummy
from Fight_engine.Class_Dummy import ClassDummy


class ClassBoard:
    # Setup variable - Will be moved to a configuration file later
    BoardRow = 3
    BoardCols = 4

    # BoardHex - Contain a dictionary [ClassChampion, Team, Hex_q, Hex_r]]
    Board_Hex = []

    def __init__(self):
        pass

    def add_angry_dummy(self, team, hex_q, hex_r):
        self.Board_Hex.append([ClassAngryDummy(), team, hex_q, hex_r])

    def add_dummy(self, team, hex_q, hex_r):
        self.Board_Hex.append([ClassDummy(), team, hex_q, hex_r])

    def update(self):
        for champ in self.Board_Hex:
            champ[1].update(self.Board_Hex)

