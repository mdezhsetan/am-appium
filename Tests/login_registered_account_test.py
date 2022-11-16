from Resources.accounts import Accounts
from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestLoginRegisteredAccount(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)

    def test_login_registeredaccount_DEV_T14(self):
        print("test login with registered account")

        self.login_screen.login_function(username=Accounts.default_username, password=Accounts.default_password,
                                         button=self.login_screen.signin_button())

        self.take_screenshot("Login")
        assert self.login_screen.is_signed_in()

    def tearDown(self):
        self.alt_driver.stop()
        self.appium_driver.quit()
