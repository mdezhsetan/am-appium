from time import sleep

from alttester.altdriver import AltObject, AltDriver

from Resources.screen import Screen


class MainScreen(Screen):
    def j01_screen_is_accessible(self):
        return (self.j01_screen)() is not None

    def __init__(self, altdriver: AltDriver, appium_driver):
        elements = {
            'j01_screen': "/Canvas/JourneyScreen01",
            'journeys_card': "//*//JourneysCard",
            'popup_onboardingselectionmanager_btn_close': "//*//OnboardingWelcomeController/OnboardingWelcomeView/UIGroup1/btn_Close",
            'popup_samd_labelling_btn_ok': "//*//Window/ContentArea/ButtonArea/OKButton",
            'popup_samd_labelling_btn_cancel': "//*//Window/ContentArea/ButtonArea/CancelButton",
        }
        super(MainScreen, self).__init__(altdriver, appium_driver, elements)



# /Canvas/LessonStage/MeditationScreen/Titlebar/MeditationEndMessageBox/text_Message
