from Fight_engine.Class_Board import ClassBoard

if __name__ == '__main__':
    Board = ClassBoard()
    Board.add_dummy("UP", 0, 1)
    Board.add_angry_dummy("DOWN", 0, 1)

    print(Board.Board_Hex)
