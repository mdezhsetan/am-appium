from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestOpenApplication(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)

    def test_open_application_DEV_T27(self):
        print("test open application")
        assert self.login_screen.is_signed_in()
        self.alt_driver.get_png_screenshot("../Screenshots")



    def tearDown(self):
        self.alt_driver.stop()
        self.appium_driver.quit()