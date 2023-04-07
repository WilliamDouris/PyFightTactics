from Fight_engine.Class_Champion import Class_Champion
from Fight_engine import globals_variable
from math import floor


class Class_Board:
    # Setup variable - Will be moved to a configuration file later
    BoardRow = 3
    BoardCols = 4

    def __init__(self):
        globals_variable.Board_Hex_r_q = dict()
        for r in range(-4, 4):  # -4 to +3
            globals_variable.Board_Hex_r_q.update(dict([[r, dict()]]))
            for q in range(-3, 4):  # -3 to +3
                # At -4 : from -1 to +5
                # At -3 : from -1 to +5
                # At -2 : from -2 to +4
                # At 0 : from -3 to +3
                globals_variable.Board_Hex_r_q[r].update(dict([[q - floor(r / 2), None]]))
        pass

    def add_champion(self, champion_name, team, hex_q, hex_r):
        champion = Class_Champion(champion_name, team)
        try:
            if globals_variable.Board_Hex_r_q[hex_r][hex_q] is not None:
                raise ValueError("An other champion is place here")
            else:
                champion.hex_q = hex_q
                champion.hex_r = hex_r
                globals_variable.Board_Hex_r_q[hex_r][hex_q] = champion
        except:
            raise ValueError("The coordinate is situated out of the board")

    def update(self):
        for r in range(-4, 4):  # -4 to +3
            for q in range(-3, 4):
                Hex = globals_variable.Board_Hex_r_q[r][q - floor(r / 2)]
                if Hex is not None:
                    #print("")
                    #print(f"Update : {Hex.hex_q} {Hex.hex_r}")
                    Hex.update()
