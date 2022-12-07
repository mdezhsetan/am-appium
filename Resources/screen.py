from alttester import AltDriver, AltObject, By, WaitTimeOutException


def try_get_object(s, path: str) -> AltObject | None:
    try:
        obj = s.alt_driver.wait_for_object(By.PATH, path, timeout=5)
        return obj
    except WaitTimeOutException:
        return None


class Screen:
    def __init__(self, altdriver: AltDriver, appium_driver, elements={}):
        self.alt_driver = altdriver
        self.appium_driver = appium_driver

        for key in elements:
            setattr(self, key, lambda k=key: try_get_object(self, elements[k]))

    def touch_and_hold(self, desired_object: AltObject, duration):
        object_position = desired_object.get_screen_position()
        self.alt_driver.hold_button(duration=duration, coordinates=object_position)

    def try_get_object(self, path: str) -> AltObject | None:
        try:
            obj = self.alt_driver.wait_for_object(By.PATH, path, timeout=5)
            return obj
        except WaitTimeOutException:
            return None
