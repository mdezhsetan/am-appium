from Resources.accounts import Accounts
from Resources.journey import Journey
from Resources.login_screen import LoginScreen
from Resources.main_screen import *
from Tests.base_test import TestBase


class TestJ01AllAboutAm(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)
        self.main_screen = MainScreen(self.alt_driver, self.appium_driver)

    def go_to_j01(self):
        self.login_screen.login_function(username=Accounts.default_username, password=Accounts.default_password,
                                         button=self.login_screen.signin_button())
        # if self.main_screen.popup_onboardingselectionmanager_btn_close() is not None:
        #     self.main_screen.popup_onboardingselectionmanager_btn_close().tap()

        self.main_screen.journeys_card().tap()
        j01_element = self.alt_driver.find_object(By.PATH, "//*//Page{0}//Mask".format("01"))
        j15_element = self.alt_driver.find_object(By.PATH, "//*//Page{0}".format("15"))

        j01_position = j01_element.get_screen_position()
        print(j01_position)

        # self.alt_driver.swipe(start=j01_position, end=(j01_element.x - 250, j01_element.y - 100), duration=0.6,
        #                       wait=True)
        sleep(1)
        self.alt_driver.click(coordinates=j01_position)
        # self.main_screen.popup_samd_labelling_btn_ok().tap()

    def test_j01_accessibility_DEV_T173(self):
        self.go_to_j01()
        # self.take_screenshot("J01")
        sleep(5)
        assert self.main_screen.j01_screen_is_accessible()

    def test_j01_stages_availability_DEV_T174(self):
        j1 = Journey(self.main_screen,9, 1)
        assert j1.is_all_stages_available()


    def test_j01_stages_playability(self):
        self.main_screen.play_stage(self.main_screen.j01_s01)

    def test_j02_stages_availability_DEV_T174(self):
        j2 = Journey(self.main_screen, 18, 2)
        assert j2.is_all_stages_available()

