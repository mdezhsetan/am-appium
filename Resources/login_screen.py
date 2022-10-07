from altunityrunner import By

from Resources.base_page import BasePage


class LoginScreen(BasePage):

    def guest_link(self):
        return self.alt_driver.wait_for_object(By.ID, "21364")

    def username_input(self):
        return self.alt_driver.wait_for_object(By.PATH, "//*//UsernameInputField")

    def password_input(self):
        return self.alt_driver.wait_for_object(By.PATH, "//*//PasswordInputField")

    def signin_button(self):
        return self.alt_driver.wait_for_object(By.NAME, "SignInButton")

    def popup_after_signin(self):
        return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay")

    def popup_yes_button(self):
        return self.alt_driver.wait_for_object(By.PATH, "//Canvas//PopupOverlay//*//YesButton")

    def is_signed_in(self):
        self.homescreen_element = self.alt_driver.wait_for_object(By.PATH, "//*//JourneyButton")
        if self.homescreen_element:
            return True
        return False

    def is_displayed(self):
        if self.guest_link and self.username_input and self.password_input:
            print("username", self.username_input)
            print("pass", self.password_input)
            print("guest", self.guest_link)
            return True
        return False
