from appium.webdriver import webdriver
from appium import webdriver

def setup_driver(port):
    desired_capabilities = {
        "deviceName": "Mahshad A52",
        "udid": "RZ8T11EEMNJ",
        'automationName': 'UiAutomator2',
        "platformName": "Android",
        "platformVersion": "12",
        'altUnityHost': 'localhost',
        'altUnityPort': 13000,
        "app": 'C:\\Users\\Mahshad\\Desktop\\build_apk\\Am29Sep.apk',

    }
    return webdriver.Remote(command_executor='http://127.0.0.1:{0}/wd/hub'.format(port),
                            desired_capabilities=desired_capabilities)
