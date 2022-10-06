from altunityrunner import By

from Resources.base_page import BasePage


class LoginScreen(BasePage):

    def guest_link(self):
        return self.alt_driver.wait_for_object(By.ID, "21364")

    def is_displayed(self):
        if self.guest_link:
            return True
