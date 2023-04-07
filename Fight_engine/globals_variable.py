time_ms = None

Board_Hex = []


class Hex:
    def __init__(self, q, r, is_visited=0, parent_hex=None):
        self.q = q
        self.r = r
        self.parent_hex = parent_hex
        self.champion = None

    def __add__(self, other):
        r = self.r + other.r
        q = self.q + other.q
        return Hex(q, r)

    def __eq__(self, other):
        if self.r == other.r and self.q == other.q:
            return 1
        else:
            return 0


Board_Hex_r_q = None
Hex_direction = [Hex(1, 0), Hex(1, -1), Hex(0, -1), Hex(-1, 0), Hex(-1, 1), Hex(0, 1)]
