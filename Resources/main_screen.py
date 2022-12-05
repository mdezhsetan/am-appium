from time import sleep

from alttester import By, NotFoundException, WaitTimeOutException
from alttester.altdriver import AltObject, AltDriver

from Resources.screen import Screen



class MainScreen(Screen):
    def j01_screen_is_accessible(self):
        return self.j01_screen is not None

    def __init__(self, altdriver: AltDriver, appium_driver):
        elements = {
            'journeys_card': "//*//JourneysCard",
            'popup_onboardingselectionmanager_btn_close': "//*//OnboardingWelcomeController/OnboardingWelcomeView/UIGroup1/btn_Close",
            'popup_samd_labelling_btn_ok': "//*//Window/ContentArea/ButtonArea/OKButton",
            'popup_samd_labelling_btn_cancel': "//*//Window/ContentArea/ButtonArea/CancelButton",
            'j01_screen': "/Canvas/JourneyScreen01",
            'j01_s01': "//*//jsb_J01S01",
            'j01_s02': "//*//jsb_J01S02",
            'j01_s03': "//*//jsb_J01S03",
            'j01_s04': "//*//jsb_J01S04",
            'j01_s05': "//*//jsb_J01S05",
            'j01_s06': "//*//jsb_J01S06",
            'j01_s07': "//*//jsb_J01S07",
            'j01_s08': "//*//jsb_J01S08",
            'j01_s09': "//*//jsb_J01S09",
            'play_button': "//*//PlayButton//Button",
            'pause_button': "//*//PauseButton//Button",
            'done_button': "//*//DoneButton",
        }
        super(MainScreen, self).__init__(altdriver, appium_driver, elements)
        

    # def journeys_card(self) -> AltObject | None:
    #     return self.try_get_object( "//*//JourneysCard")
    #
    # def popup_onboardingselectionmanager_btn_close(self) -> AltObject | None:
    #     return self.try_get_object("//*//OnboardingWelcomeController/OnboardingWelcomeView/UIGroup1/btn_Close")
    #
    # def popup_samd_labelling_btn_ok(self) -> AltObject | None:
    #     return self.try_get_object("//*//Window/ContentArea/ButtonArea/OKButton")
    #
    # def popup_samd_labelling_btn_cancel(self) -> AltObject | None:
    #     return self.try_get_object("//*//Window/ContentArea/ButtonArea/CancelButton")
    #
    # @property
    # def j01_screen(self) -> AltObject | None:
    #     return self.try_get_object("/Canvas/JourneyScreen01")
    #
    # @property
    # def j01_s01(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S01")
    #
    # @property
    # def j01_s02(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S02")
    #
    # @property
    # def j01_s03(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S03")
    #
    # @property
    # def j01_s04(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S04")
    #
    # @property
    # def j01_s05(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S05")
    #
    # @property
    # def j01_s06(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S06")
    #
    # @property
    # def j01_s07(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S07")
    #
    # @property
    # def j01_s08(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S08")
    #
    # @property
    # def j01_s09(self) -> AltObject | None:
    #     return self.try_get_object("//*//jsb_J01S09")
    #
    # @property
    # def play_button(self) -> AltObject | None:
    #     return self.try_get_object("//*//PlayButton//Button")
    #
    # @property
    # def pause_button(self) -> AltObject | None:
    #     return self.try_get_object("//*//PauseButton//Button")
    #
    # @property
    # def done_button(self) -> AltObject | None:
    #     return self.try_get_object("//*//DoneButton")

    def play_stage(self, stage: AltObject):
        # stage_position = stage.get_screen_position()
        element_1 = self.alt_driver.find_object(By.PATH,"/Canvas/JourneyScreen01/Content/ScrollView/Viewport/Content/jsb_J01S01/DownloadAnimation/1")
        element_2 = self.alt_driver.find_object(By.PATH,"/Canvas/JourneyScreen01/Content/ScrollView/Viewport/Content/jsb_J01S01/DownloadAnimation/2")
        element_3 = self.alt_driver.find_object(By.PATH,"/Canvas/JourneyScreen01/Content/ScrollView/Viewport/Content/jsb_J01S01/DownloadAnimation/3")
        print("\n\n1 :  ",element_1.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n2 :  ",element_2.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n3 :  ",element_3.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))

        stage.click()
        # self.alt_driver.click(coordinates=stage_position,count=2,interval=5)
        print("\n\n1 :  ",element_1.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n2 :  ",element_2.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n3 :  ",element_3.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        sleep(30)
        print("\n\n1 :  ",element_1.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n2 :  ",element_2.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n3 :  ",element_3.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        stage.click()
        sleep(5)
        print("\n\n1 :  ",element_1.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n2 :  ",element_2.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        print("\n\n3 :  ",element_3.call_component_method(component_name="UnityEngine.UI.Image",assembly="UnityEngine.UI",method_name="IsActive"))
        pause_button = self.pause_button.get_screen_position()
        # self.alt_driver.press_key(key_code=AltKeyCode.Mouse0, duration=8, coordinates=pause_button)
        finger_id = self.alt_driver.begin_touch(coordinates=pause_button)
        sleep(8)
        self.alt_driver.end_touch(finger_id=finger_id)

# /Canvas/LessonStage/MeditationScreen/Titlebar/MeditationEndMessageBox/text_Message


