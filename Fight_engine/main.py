from Fight_engine import globals_variable
from Fight_engine.Class_Board import Class_Board

if __name__ == '__main__':
    Board = Class_Board()
    Board.add_champion("angry_dummy", 0, 0, 0)
    Board.add_champion("dummy", 1, 1, 0)
    #globals_variable.Board_Hex_r_q[0][0].nearest_in_range(1)
    for time_ms_simu in range(10000):
        globals_variable.time_ms = time_ms_simu
        #print(f"Time : {globals_variable.time_ms}")
        Board.update()


