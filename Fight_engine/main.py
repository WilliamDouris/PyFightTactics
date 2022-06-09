from Fight_engine.Class_Board import ClassBoard

from Fight_engine.Class_Champion import Class_Champion

if __name__ == '__main__':

    Teemo = Class_Champion("Teemo")
    Gragas = Class_Champion("Gragas")
    Teemo.ultimate()
    Gragas.ultimate()

    """Board = ClassBoard()
    Board.add_dummy("UP", 0, 1)
    Board.add_angry_dummy("DOWN", 0, 1)

    for i in range(10):
        print(f"update {i}")
        Board.update()"""


