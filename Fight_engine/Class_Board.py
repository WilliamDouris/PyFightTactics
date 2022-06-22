from Fight_engine.Class_Champion import Class_Champion
from Fight_engine import globals_variable

class Class_Board:
    # Setup variable - Will be moved to a configuration file later
    BoardRow = 3
    BoardCols = 4

    def __init__(self):
        pass

    def add_champion(self, champion_name, team, hex_q, hex_r):
        champ = Class_Champion(champion_name)
        champ.q = hex_q
        champ.r = hex_r
        globals_variable.Board_Hex.append([champ, team, hex_q, hex_r])
        globals_variable.Board_Hex_q_r[hex_q][hex_r] = champ
        # Board_Hex_q_r[q][r] = [Champion] # None if no champ
        # Board_Hex_champion = [Champion]
        # Board_Hex_team[team] = [Champion]


    def update(self):
        for champ in globals_variable.Board_Hex:
            champ[0].update()
