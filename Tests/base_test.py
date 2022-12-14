import unittest

from alttester import AltDriver
from appium import webdriver

from Resources.accounts import Accounts


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_capabilities = {
            "deviceName": "Mahshad A52",
            "udid": "RZ8T11EEMNJ",
            'automationName': 'UiAutomator2',
            "platformName": "Android",
            "platformVersion": "13",
            'altUnityHost': 'localhost',
            'altUnityPort': 13000,
            "app": 'C:\\Users\\Mahshad\\Desktop\\build_apk\\Am8Nov2.apk',
        }
        cls.appium_driver = webdriver.Remote(command_executor='http://127.0.0.1:{0}/wd/hub'.format(4723),
                                             desired_capabilities=cls.desired_capabilities)
        cls.alt_driver = AltDriver()

    def take_screenshot(self, subject):
        self.alt_driver.get_png_screenshot("./Screenshots/" + subject + Accounts.current_time_string() + ".png")

    def touch_and_hold(self, desired_object, duration):
        card_position = desired_object.get_screen_position()
        self.alt_driver.hold_button(duration=duration, coordinates=card_position)

# @classmethod
# def tearDownClass(cls):
#     print("Ending")
#     cls.alt_driver.stop()
#     cls.appium_driver.quit()
