class ClassAngryDummy:

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

    def __init__(self):
        pass

    def take_dmg(self, AD_dmg):
        self.Actual_HP = self.Actual_HP - AD_dmg
        print(f"Angry_dummy - HP left : {self.Actual_HP}")

    def update(self, Board_Hex):
        if self.AA_Cycle == 0:
            Board_Hex[0][0].take_dmg(self.AD)  # Dmg the Dummy
            self.AA_Cycle = self.AS_Cycle
        else:
            self.AA_Cycle = self.AA_Cycle - 1




