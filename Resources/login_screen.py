from alttester import NotFoundException, WaitTimeOutException
from alttester.altdriver import *

from Resources.base_page import BasePage


class LoginScreen(BasePage):

    def guest_link(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH ,"//*//GuestRow//Card")
        except NotFoundException:
            return None

    def username_input(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//UsernameInputField")
        except NotFoundException:
            return None

    def password_input(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//PasswordInputField")
        except NotFoundException:
            return None

    def signuptoggle_link(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//SignupToggle//Create")
        except NotFoundException:
            return None

    def signup_button(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//SignUpButton")
        except NotFoundException:
            return None

    def toggle_ReceiveScheduledNotifications_check(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*///toggle_ReceiveScheduledNotifications")
        except NotFoundException:
            return None

    def signin_button(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.NAME, "SignInButton")
        except NotFoundException:
            return None

    def popup_after_signin(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay")
        except NotFoundException:
            return None

    def popup_yes_button(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay//*//YesButton")
        except NotFoundException:
            return None

    def account_selection_screen(self) -> AltObject | None:
        try:
            account_selection_obj = self.alt_driver.wait_for_object(By.PATH, "/Canvas/HomeScreenNew/AccountSelection",
                                                                    timeout=5)
            return account_selection_obj
        except WaitTimeOutException:
            print("account selection screen not found!")
            return None

    def OnboardingSelectionManager_is_Displayed(self):
        try:
            self.alt_driver.wait_for_object(By.PATH, "//*//OnboardingSelectionManager")
            return True
        except Exception as ex:
            print(repr(ex))
            return False

        # get_isActiveAndEnabled() Boolean

    def login_function(self, username, password, button):
        self.username_input().set_text(username)
        self.password_input().set_text(password)
        button.tap()
        self.popup_yes_button().tap()

    def is_signed_in(self):
        try:
            self.alt_driver.wait_for_object_to_not_be_present(By.PATH, "/Canvas/HomeScreenNew/AccountSelection")
            return True
        except Exception as ex:
            print(repr(ex))
            return False

    def is_displayed(self):
        if self.account_selection_screen() is not None:
            return True
        return False
