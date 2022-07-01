time_ms = None

Board_Hex = []


class Hex:
    def __init__(self, q, r, is_visited=0, parent_hex=None):
        self.q = q
        self.r = r
        self.parent_hex = parent_hex

    def __add__(self, other):
        r = self.r + other.r
        q = self.q + other.q
        return Hex(q, r)

    def __eq__(self, other):
        if self.r == other.r and self.q == other.q:
            return 1
        else:
            return 0

Board_size_q = 7  # horizontal
Board_size_r = 8  # vertical
Board_Hex_q_r = [[None for x in range(Board_size_r)] for y in range(Board_size_q)]
Hex_direction = [Hex(1, 0), Hex(1, -1), Hex(0, -1), Hex(-1, 0), Hex(-1, 1), Hex(0, 1)]
