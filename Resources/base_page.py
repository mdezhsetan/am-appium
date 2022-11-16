class BasePage:

    def __init__(self, altdriver, appium_driver):
        self.alt_driver = altdriver
        self.appium_driver = appium_driver