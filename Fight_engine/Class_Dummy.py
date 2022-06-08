
class ClassDummy:

    # Parameter to import from file
    Champ_name = "Angry_dummy"
    AD = 75
    Total_HP = 400
    Range = 1

    # Parameter to calculate
    AS_Cycle = 3
    AA_Cycle = 3

    # Change in-game
    Actual_HP = 400

    def take_dmg(self, AD_dmg):
        self.Actual_HP = self.Actual_HP - AD_dmg
        print(f"Dummy - HP left : {self.Actual_HP}")

    def update(self, Board_Hex):
        pass

    def __init__(self):
        pass
