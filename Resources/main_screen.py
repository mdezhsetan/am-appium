from alttester import By, NotFoundException, AltObject, AltDriver

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

    def popup_onboardingselectionmanager_btn_close(self) -> AltDriver | None:
        try:
            return self.alt_driver.wait_for_object(By.PATH,
                                                   "//*//OnboardingWelcomeController/OnboardingWelcomeView/UIGroup1/btn_Close")
        except NotFoundException:
            return None
