from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestOpenApplication(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)

    def test_open_application(self):
        print("objects are found by altunity")
        self.guest_obj = self.login_screen.guest_link()
        self.guest_obj.tap()
