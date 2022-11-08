from Resources.accounts import Accounts
from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestLoginCreateAccount(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)
        self.accounts = Accounts(self.alt_driver, self.appium_driver)

    def test_login_createaccount_DEV_T29(self):
        # self.username = self.accounts.new_account_username()



        print("test login by creating new account")
        print( self.login_screen.signuptoggle_link())
        # self.login_screen.username_input().set_text(self.username)
        # self.login_screen.password_input().set_text(self.password)
        # self.login_screen.signup_button().tap()
        # self.login_screen.popup_yes_button().tap()
        # self.alt_driver.get_png_screenshot("./Screenshots/login.png") #I have to add date and time in the name!

        # assert self.login_screen.is_signed_in()
    #
    # def tearDown(self):
    #     self.alt_driver.stop()
    #     self.appium_driver.quit()
