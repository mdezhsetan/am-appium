from Resources.accounts import Accounts
from Resources.journeys import Journeys
from Resources.login_screen import LoginScreen
from Resources.main_screen import *
from Tests.base_test import TestBase


class TestJ01AllAboutAm(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)
        self.main_screen = MainScreen(self.alt_driver, self.appium_driver)
        self.j1 = Journeys(self.alt_driver, self.appium_driver, stage_count=9,
                           journey_number=1)

    def go_to_j01(self):
        self.login_screen.login_function(username=Accounts.default_username, password=Accounts.default_password,
                                         button=self.login_screen.signin_button())
        # if self.main_screen.popup_onboardingselectionmanager_btn_close() is not None:
        #     self.main_screen.popup_onboardingselectionmanager_btn_close().tap()
        sleep(3)
        journeys_card = getattr(self.main_screen, "journeys_card")()

        journeys_card.tap()
        j01_element = getattr(self.j1, "j01_element")()
        j01_position = j01_element.get_screen_position()
        # self.alt_driver.swipe(start=j01_position, end=(j01_element.x - 250, j01_element.y - 100), duration=0.6,wait=True)

        self.alt_driver.click(coordinates=j01_position)
        # self.main_screen.popup_samd_labelling_btn_ok().tap()

    def test_j01_accessibility_DEV_T173(self):
        self.go_to_j01()
        sleep(5)
        assert self.main_screen.j01_screen_is_accessible()

    def test_j01_stages_availability_DEV_T174(self):
        assert self.j1.is_all_stages_available()

    def test_j01_stages_playability(self):
        current_stage = self.j1.get_stage(1)
        self.j1.play_stage(current_stage())
