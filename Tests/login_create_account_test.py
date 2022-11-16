from Resources.accounts import Accounts
from Resources.login_screen import LoginScreen
from Tests.base_test import TestBase


class TestLoginCreateAccount(TestBase):

    def setUp(self):
        self.login_screen = LoginScreen(self.alt_driver, self.appium_driver)
        self.accounts = Accounts()

    def test_login_createaccount_DEV_T29(self):
        print("\ntest login by creating new account")
        # print(self.login_screen.OnboardingSelectionManager_is_Displayed())

        self.username = self.accounts.new_account_username()
        self.login_screen.signuptoggle_link().tap()
        self.login_screen.login_function(username=self.username,password=Accounts.password,button=self.login_screen.signup_button())
        self.take_screenshot("CreateAcc")
        assert self.login_screen.OnboardingSelectionManager_is_Displayed()

    #
    # def tearDown(self):
    #     self.alt_driver.stop()
    #     self.appium_driver.quit()
