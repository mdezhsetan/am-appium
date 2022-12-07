from alttester.altdriver import *

from Resources.screen import Screen


class LoginScreen(Screen):

    def __init__(self, altdriver: AltDriver, appium_driver):

        elements = {
            "guest_link": "//*//GuestRow//Card",
            "username_input": "//*//UsernameInputField",
            "password_input": "//*//PasswordInputField",
            "signuptoggle_link": "//*//SignupToggle//Create",
            "signup_button": "//*//SignUpButton",
            "toggle_ReceiveScheduledNotifications_check": "//*///toggle_ReceiveScheduledNotifications",
            "signin_button": "//*//SignInButton",
            "popup_after_signin": "//Canvas//PopupOverlay",
            "popup_yes_button": "//Canvas//PopupOverlay//*//YesButton",
            "account_selection_screen": "/Canvas/HomeScreenNew/AccountSelection",
            "OnboardingSelectionManager": "//*//OnboardingSelectionManager",
        }
        super(LoginScreen, self).__init__(altdriver=altdriver, appium_driver=appium_driver, elements=elements)

    def OnboardingSelectionManager_is_Displayed(self):
        try:
            self.OnboardingSelectionManager()
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
        return self.account_selection_screen() is not None
