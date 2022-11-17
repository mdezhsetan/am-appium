from Resources.accounts import Accounts
from Resources.login_screen import LoginScreen
from Resources.main_screen import MainScreen
from Tests.base_test import TestBase


class TestJ01AllAboutAm(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)
        self.main_screen = MainScreen(self.alt_driver, self.appium_driver)

    def go_to_j01(self):
        self.login_screen.login_function(username=Accounts.default_username, password=Accounts.default_password,
                                         button=self.login_screen.signin_button())
        self.main_screen.popup_onboardingselectionmanager_btn_close().tap()
        self.main_screen.journeys_card().tap()
        # self.touch_and_hold(JOURNEYS_CARD, 3)

    def test_j01_accessibility_DEV_T173(self):
        print("test j01")

        self.go_to_j01()

        self.take_screenshot("J01")

        # assert

    # def tearDown(self):
    #     self.alt_driver.stop()
    #     self.appium_driver.quit()
