from Resources.base_page import BasePage
from altunityrunner import By


class LoginScreen(BasePage):

    def guest_link(self):
        return self.alt_driver.wait_for_object(By.ID, "21364")
