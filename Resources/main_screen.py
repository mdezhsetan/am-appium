from alttester import By, NotFoundException, AltObject, WaitTimeOutException

from Resources.base_page import BasePage


class MainScreen(BasePage):

    def journeys_card(self) -> AltObject | None:
        """

        :rtype: object
        """
        try:
            return self.alt_driver.wait_for_object(By.PATH, "//*//JourneysCard")
        except NotFoundException:
            return None

    def popup_onboardingselectionmanager_btn_close(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH,
                                                   "//*//OnboardingWelcomeController/OnboardingWelcomeView/UIGroup1/btn_Close")
        except NotFoundException:
            return None

    def popup_samd_labelling_btn_ok(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH,
                                                   "//*//Window/ContentArea/ButtonArea/OKButton")
        except NotFoundException:
            return None

    def popup_samd_labelling_btn_cancel(self) -> AltObject | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH,
                                                   "//*//Window/ContentArea/ButtonArea/CancelButton")
        except NotFoundException:
            return None

    def j01_screen(self) -> AltObject | None:
        try:
            j01_screen_element = self.alt_driver.wait_for_object(By.PATH,
                                                   "/Canvas/JourneyScreen01",timeout=5)
            return j01_screen_element
        except WaitTimeOutException:
            print("j01 screen not found!")
            return None

    def j01_screen_is_accessible(self):
        if self.j01_screen() is not None:
            return True
        return False