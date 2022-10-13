from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestOpenApplication(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)

    def test_login_guestaccount_DEV_T27(self):
        print("test login guest account")

        self.login_screen.guest_link().tap()

        assert self.login_screen.is_signed_in()

    def tearDown(self):
        self.alt_driver.stop()
        self.appium_driver.quit()
