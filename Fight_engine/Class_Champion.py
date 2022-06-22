import xml.etree.ElementTree as ET
from Fight_engine import globals_variable


class Class_Champion:

    def __init__(self, champion_name):
        self.champion_name = champion_name
        self.champ_stats = {}
        self.attackStartAtMs = 0
        self.hex_q = 0
        self.hex_r = 0

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
            1 / 1 + (Champion.champ_stats["ARMOR"] / 100))
        Champion.champ_stats["Actual_HP"] = Champion.champ_stats["Actual_HP"] - AP_dmg * round(
            1 / 1 + (Champion.champ_stats["MR"] / 100))
        Champion.champ_stats["Actual_HP"] = Champion.champ_stats["Actual_HP"] - True_dmg
        print(f"Champion - HP left : {Champion.champ_stats['Actual_HP']}")

    def spell(self):
        self.spell_function(self.champ_stats)

    def nearest_in_range(self):
        pass
        # visited = [[["2,3"],["4,2"]#movement1],[["2,5"]["-1,3"]#movement2]
        visited = [[[self.hex_q, self.hex_r]]]
        for k in range(int(self.champ_stats["Range"])):
            for base_hex in visited[-1]:
                for dir in globals_variable.Hex_direction:
                    new_hex = [base_hex[0] + dir[0], base_hex[1] + dir[1]]
                    #print([new_hex])
                    #print(globals_variable.Board_Hex_q_r)
                    is_visited = 0
                    for movement_visited in visited:
                        if is_visited == 1:
                            continue
                        for hex_visited in movement_visited:
                            if hex_visited[0] == new_hex[0] and hex_visited[1] == new_hex[1]:
                                is_visited = 1
                                continue
                    if is_visited == 0:  # if visited check is there is a champ there
                        if globals_variable.Board_Hex_q_r[new_hex[0]][new_hex[1]] is not None and globals_variable.Board_Hex_q_r[new_hex[0]][new_hex[1]] != self:
                            print(f"{dir[0]},{dir[1]}")
                            print(f"q={new_hex[0]} - r={new_hex[1]} - champ = {globals_variable.Board_Hex_q_r[new_hex[0]][new_hex[1]].champion_name}")
                            return globals_variable.Board_Hex_q_r[new_hex[0]][new_hex[1]]

        return None

    def update(self):
        # Check for AA Timing
        if self.attackStartAtMs + 1000 / self.champ_stats["AS"] < globals_variable.time_ms:
            print(f"{globals_variable.time_ms} - {self.champion_name} AA - {self.champ_stats['AS']}")
            self.apply_dmg(globals_variable.Board_Hex[0][0], self.champ_stats["AD"], 0, 0)
            self.attackStartAtMs = globals_variable.time_ms
