from time import sleep

from altunityrunner import AltUnityDriver

from Resources import setup_driver as setup
from Tests import open_application_test, login_valid_account_test as test

appium_driver = setup.setup_driver(port=4723)
alt_driver = AltUnityDriver()
print("object created")
test_open_obj = test_open_application.TestOpenApplication(appiumdriver=appium_driver, altdriver=alt_driver)
test_login_obj = test.TestLoginScreen(appiumdriver=appium_driver, altdriver=alt_driver)

test_open_obj.test_open_application()
test_login_obj.test_login()

sleep(10)

appium_driver.quit()
print("End")
