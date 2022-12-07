from time import sleep

from alttester import AltDriver, AltObject

from Resources.screen import Screen


class Journeys(Screen):
    def __init__(self, altdriver: AltDriver, appium_driver, stage_count: int,
                 journey_number: int):
        self.stage_count = stage_count
        self.journy_prefix = "j" + f'{journey_number:02}' + '_s'

        elements = {
            'j01_element': "//*//Page01/Mask",
            'j01_s01': "//*/jsb_J01S01",
            'j01_s02': "//*/jsb_J01S02",
            'j01_s03': "//*//jsb_J01S03",
            'j01_s04': "//*//jsb_J01S04",
            'j01_s05': "//*//jsb_J01S05",
            'j01_s06': "//*//jsb_J01S06",
            'j01_s07': "//*//jsb_J01S07",
            'j01_s08': "//*//jsb_J01S08",
            'j01_s09': "//*//jsb_J01S09",
            'play_button': "//*//PlayButton/Button",
            'pause_button': "//*//PauseButton/Button",
            'done_button': "//*//DoneButton",
            'download_animation_1': "//*//DownloadAnimation/1",
            'download_animation_2': "//*//DownloadAnimation/2",
            'download_animation_3': "//*//DownloadAnimation/3"
        }
        super(Journeys, self).__init__(altdriver=altdriver, appium_driver=appium_driver, elements=elements)

    def is_all_stages_available(self):
        for i in range(1, self.stage_count):
            get_stage = self.get_stage(i)
            if get_stage is None or get_stage() is None:
                return False
        return True

    def get_stage(self, stage_number: int):
        stage_name = self.journy_prefix + f'{stage_number:02}'
        return getattr(self, stage_name)

    def play_stage(self, stage: AltObject):
        # stage_position = stage.get_screen_position()

        # print("\n\n1 :  ",element_1.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))

        stage.click()
        sleep(5)
        stage.click()
        sleep(7)
        pause_button = self.pause_button()

        self.touch_and_hold(pause_button, 9)
        self.done_button().click()
