from Fight_engine.Class_Angry_Dummy import ClassAngryDummy
from Fight_engine.Class_Dummy import ClassDummy


class ClassBoard:
    # Setup variable - Will be moved to a configuration file later
    BoardRow = 3
    BoardCols = 4

    # UID - Unique number to identify each champion
    # - Negative for Team Up and Positive for Team Down
    # - Increase each time you add a champion.
    UID = 1

    # BoardHex - Contain a dictionary [UID, ClassChampion, Hex_q, Hex_r]]
    Board_Hex = []

    def __init__(self):
        pass

    def add_angry_dummy(self, team, hex_q, hex_r):
        self.Board_Hex.append([self.UID if team == "UP" else -self.UID, ClassAngryDummy(), hex_q, hex_r])
        self.UID = self.UID + 1

    def add_dummy(self, team, hex_q, hex_r):
        self.Board_Hex.append([self.UID if team == "UP" else -self.UID, ClassDummy(), hex_q, hex_r])
        self.UID = self.UID + 1
