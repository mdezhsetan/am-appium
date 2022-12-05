from alttester import AltDriver, AltObject, By, WaitTimeOutException

class Screen:
    def __init__(self, altdriver: AltDriver, appium_driver, elements):
        self.alt_driver = altdriver
        self.appium_driver = appium_driver

        for key in elements:
            setattr(self, key, lambda : self.try_get_object(elements[key]))


    def touch_and_hold(self, desired_object, duration):
        card_position = desired_object.get_screen_position()
        self.alt_driver.hold_button(duration=duration, coordinates=card_position)

    def try_get_object(self, path: str) -> AltObject | None:
        try:
            obj = self.alt_driver.wait_for_object(By.PATH, path, timeout=5)
            return obj
        except WaitTimeOutException:
            return None
