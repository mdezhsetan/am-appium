from Resources.main_screen import MainScreen


class Journey:
    def __init__(self, main_screen: MainScreen, stage_count: int, journey_number: int):
        self.main_screen = main_screen
        self.stage_count = stage_count
        self.journy_prefix = "j" + f'{journey_number:02}' + '_s'

    def is_all_stages_available(self):
        for i in range(1, self.stage_count):
            stage_name = self.journy_prefix + f'{i:03}'
            get_stage = getattr(self.main_screen, stage_name)
            if get_stage is None or get_stage() is None:
                return False
        return True
