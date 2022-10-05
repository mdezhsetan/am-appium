import unittest

from altunityrunner import AltUnityDriver
from appium import webdriver

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_capabilities = {
            "deviceName": "Mahshad A52",
            "udid": "RZ8T11EEMNJ",
            'automationName': 'UiAutomator2',
            "platformName": "Android",
            "platformVersion": "12",
            'altUnityHost': 'localhost',
            'altUnityPort': 13000,
            "app": 'C:\\Users\\Mahshad\\Desktop\\build_apk\\Am29Sep.apk',
        }
        cls.appium_driver = webdriver.Remote(command_executor='http://127.0.0.1:{0}/wd/hub'.format(4723),
                                             desired_capabilities=cls.desired_capabilities)
        cls.alt_driver = AltUnityDriver()
