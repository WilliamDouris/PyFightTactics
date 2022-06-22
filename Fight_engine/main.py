from Fight_engine import globals_variable
from Fight_engine.Class_Board import Class_Board

if __name__ == '__main__':
    Board = Class_Board()
    Board.add_champion("angry_dummy", "DOWN", 0, 0)
    Board.add_champion("dummy", "UP", -2, 0)
    print(globals_variable.Board_Hex_q_r)
    globals_variable.Board_Hex[0][0].nearest_in_range()
    for time_ms_simu in range(0):
        globals_variable.time_ms = time_ms_simu
        #print(f"Time : {globals_variable.time_ms}")
        Board.update()


