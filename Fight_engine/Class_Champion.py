class Class_Champion:
    ultimate = None

    def __init__(self, champion_name):
        if champion_name == "Teemo":
            from Fight_engine.Ultimate_data import ultimate_teemo as ultimate_function
        elif champion_name == "Gragas":
            from Fight_engine.Ultimate_data import ultimate_gragas as ultimate_function
        self.ultimate = ultimate_function
