from altunityrunner import By, NotFoundException, WaitTimeOutException

from Resources.base_page import BasePage


class LoginScreen(BasePage):

    def guest_link(self):
        try:
            return self.alt_driver.wait_for_object(By.ID, "21364")
        except NotFoundException:
            return None

    def username_input(self):
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//UsernameInputField")
        except NotFoundException:
            return None

    def password_input(self):
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//PasswordInputField")
        except NotFoundException:
            return None

    def signin_button(self):
        try:
            return self.alt_driver.wait_for_object(By.NAME, "SignInButton")
        except NotFoundException:
            return None

    def popup_after_signin(self):
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay")
        except NotFoundException:
            return None

    def popup_yes_button(self):
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay//*//YesButton")
        except NotFoundException:
            return None

    def account_selection_screen(self):
        try:
            account_selection_obj = self.alt_driver.wait_for_object(By.PATH, "/Canvas/HomeScreenNew/AccountSelection",
                                                                    timeout=5)
            return account_selection_obj
        except WaitTimeOutException:
            print("account selection screen not found!")
            return None

    def is_signed_in(self):
        try:
            if self.account_selection_screen() is None:
                return True
            print("Is not signed In!")
            return False
        except Exception as ex:
            print(repr(ex))
            return False

    def is_displayed(self):
        if self.account_selection_screen() is not None:
            return True
        return False
