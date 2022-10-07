from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestLoginRegisteredAccount(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)

    def test_login_registeredaccount_DEV_T14(self):
        print("test login with registered account")
        self.login_screen.username_input().set_text(self.registered_email_text)
        self.login_screen.password_input().set_text(self.registered_pass_text)
        self.login_screen.signin_button().tap()
        self.login_screen.popup_yes_button().tap()
        self.alt_driver.get_png_screenshot("./Screenshots/login.png") #I have to add date and time in the name!
        assert self.login_screen.is_signed_in()

    def tearDown(self):
        self.alt_driver.stop()
        self.appium_driver.quit()
