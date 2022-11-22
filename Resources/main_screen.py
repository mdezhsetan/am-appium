from alttester import By, NotFoundException, AltObject, WaitTimeOutException

from Resources.base_page import BasePage


def j01_stage_is_available(stage):
    if stage is not None:
        return True
    return False


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
                                                                 "/Canvas/JourneyScreen01", timeout=5)
            return j01_screen_element
        except WaitTimeOutException:
            print("j01 screen not found!")
            return None

    def j01_screen_is_accessible(self):
        if self.j01_screen() is not None:
            return True
        return False

    @property
    def j01_s01(self):
        try:
            j01s01 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S01", timeout=5)
            return j01s01
        except WaitTimeOutException:
            print("j01-s01 not found!")
            return None

    @property
    def j01_s02(self):
        try:
            j01s02 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S02", timeout=5)
            return j01s02
        except WaitTimeOutException:
            print("j01-s02 not found!")
            return None

    @property
    def j01_s03(self):
        try:
            j01s03 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S03", timeout=5)
            return j01s03
        except WaitTimeOutException:
            print("j01-s03 not found!")
            return None

    @property
    def j01_s04(self):
        try:
            j01s04 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S04", timeout=5)
            return j01s04
        except WaitTimeOutException:
            print("j01-s04 not found!")
            return None

    @property
    def j01_s05(self):
        try:
            j01s05 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S05", timeout=5)
            return j01s05
        except WaitTimeOutException:
            print("j01-s05 not found!")
            return None


    @property
    def j01_s06(self):
        try:
            j01s06 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S06", timeout=5)
            return j01s06
        except WaitTimeOutException:
            print("j01-s06 not found!")
            return None


    @property
    def j01_s07(self):
        try:
            j01s07 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S07", timeout=5)
            return j01s07
        except WaitTimeOutException:
            print("j01-s07 not found!")
            return None


    @property
    def j01_s08(self):
        try:
            j01s08 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S08", timeout=5)
            return j01s08
        except WaitTimeOutException:
            print("j01-s08 not found!")
            return None

    @property
    def j01_s09(self):
        try:
            j01s09 = self.alt_driver.wait_for_object(By.PATH,
                                                      "//*//jsb_J01S09", timeout=5)
            return j01s09
        except WaitTimeOutException:
            print("j01-s09 not found!")
            return None
