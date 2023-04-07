import xml.etree.ElementTree as ET
from Fight_engine import globals_variable
from copy import deepcopy

class Class_Champion:

    def __init__(self, champion_name, team):
        self.champion_name = champion_name
        self.champ_stats = {}
        self.attackStartAtMs = 0
        self.hex_q = 0
        self.hex_r = 0
        self.team = team

        # Init champion stats
        tree = ET.parse('Champion_stats.xml')
        root = tree.getroot()

        for champion_list in root:
            # print(f"child : {child.attrib['name']}")
            if champion_list.attrib['name'] == champion_name:
                for champion in champion_list:
                    # print(f"champ_stats : {champion.tag} - {champion.text}")
                    self.champ_stats[champion.tag] = float(champion.text)

        print(f"{champion_name} stats loaded - {self.champ_stats}")

        if self.champ_stats == {}:
            raise NotImplementedError("champion not implemented in champion_stats.xml")

        # Init Champion spell - Maybe changed in futur to write here the code for each champion function
        if champion_name == "dummy":
            from Fight_engine.Spell_data import spell_dummy as spell_function
        elif champion_name == "angry_dummy":
            from Fight_engine.Spell_data import spell_angry_dummy as spell_function
        else:
            raise NotImplementedError("Class_Champion - Ultimate not implemented yet !")

        self.spell_function = spell_function

        self.champ_stats["Actual_HP"] = self.champ_stats["Total_HP"]

    def take_dmg(self, AD_dmg, AP_dmg, True_dmg):
        # MR/ARMOR reduction calcul provided by https://leagueoflegends.fandom.com/wiki/Armor
        # The reduction is confirmed with MR_armor_calculation.xlsx
        self.champ_stats["Actual_HP"] = self.champ_stats["Actual_HP"] - AD_dmg * round(
            1 / 1 + (self.champ_stats["ARMOR"] / 100))
        self.champ_stats["Actual_HP"] = self.champ_stats["Actual_HP"] - AP_dmg * round(
            1 / 1 + (self.champ_stats["MR"] / 100))
        self.champ_stats["Actual_HP"] = self.champ_stats["Actual_HP"] - True_dmg
        print(f"Dummy - HP left : {self.champ_stats['Actual_HP']}")

    def apply_dmg(self, Champion, AD_dmg, AP_dmg, True_dmg):
        # MR/ARMOR reduction calcul provided by https://leagueoflegends.fandom.com/wiki/Armor
        # The reduction is confirmed with MR_armor_calculation.xlsx
        # NEED TO CONFIRM : Is % resistance rounded or dmg ?
        Champion.champ_stats["Actual_HP"] = Champion.champ_stats["Actual_HP"] - AD_dmg * round(
            1 / (1 + (Champion.champ_stats["ARMOR"] / 100)))
        Champion.champ_stats["Actual_HP"] = Champion.champ_stats["Actual_HP"] - AP_dmg * round(
            1 / (1 + (Champion.champ_stats["MR"] / 100)))
        Champion.champ_stats["Actual_HP"] = Champion.champ_stats["Actual_HP"] - True_dmg
        print(f"Champion - HP left : {Champion.champ_stats['Actual_HP']}")

    def spell(self):
        self.spell_function(self.champ_stats)

    def nearest_in_range(self, team):

        # Define local variable
        board_local = deepcopy(globals_variable.Board_Hex_r_q) # Will store our tree of path
        board_local[self.hex_r][self.hex_q] = "v"
        hex_visited = [globals_variable.Hex(self.hex_q, self.hex_r)] # Store the Hex coordinate explored in the current iteration
        hex_last_visited = []  # Store the Hex coordinate explored in last iteration

        for k in range(int(self.champ_stats["Range"])):
            #print(f"---- range : {k} ----")

            hex_last_visited = hex_visited
            hex_visited = []

            # Explore Hex discoverer in last iteration
            for hex_base in hex_last_visited:
                #print(f"--- base_hex : {hex_base.r} {hex_base.q}")

                # Explore all direction around the Hex
                for dir in globals_variable.Hex_direction:
                    hex_explore = hex_base + dir
                    #print(f"--- new_hex : {hex_explore.r} {hex_explore.q}")

                    try:
                        Hex = board_local[hex_explore.r][hex_explore.q]
                        if Hex is not None: # Visited or Champion
                            if Hex == "v": # If visited
                                continue
                            elif Hex.team == team: # If the champion is from the wanted team
                                #print(f"Champion find in {Hex.hex_q} {Hex.hex_r}")
                                return Hex
                            else: # If the champion is not from the wanted team
                                #print(f"If the champion is not from the wanted team")
                                hex_visited.append(globals_variable.Hex(hex_explore.q,hex_explore.r))
                                Hex = "v"
                        else: # The hex is empty
                            hex_visited.append(globals_variable.Hex(hex_explore.q, hex_explore.r))
                            Hex = "v"
                    except:
                        pass

        return None


    def update(self):
        # Check for AA Timing
        champ = self.nearest_in_range(1 - self.team)
        if champ is None: # Champ not in range - Try to move
            # print("hi")
            pass # TODO: Implement move
        elif champ is not None:
            if self.attackStartAtMs + 1000 / self.champ_stats["AS"] < globals_variable.time_ms:
                print(f"{globals_variable.time_ms} - {self.champion_name} AA - {self.champ_stats['AS']}")
                self.apply_dmg(champ, self.champ_stats["AD"], 0, 0)
                self.attackStartAtMs = globals_variable.time_ms
