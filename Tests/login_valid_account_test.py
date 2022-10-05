# from time import sleep
#
# from altunityrunner import By
#
#
# class TestLoginScreen:
#
#     def __init__(self, appiumdriver, altdriver):
#         self.appium_driver = appiumdriver
#         self.alt_driver = altdriver
#
#         self.registered_email_text = "testaccount-am1@pso.com"
#         self.registered_pass_text = "Welcome20!"
#         self.email_obj = self.alt_driver.wait_for_object(By.ID, "23694")
#         self.pass_obj = self.alt_driver.wait_for_object(By.ID, "25418")
#         self.btn_obj = self.alt_driver.wait_for_object(By.ID, "16510")
#
#         print("inputs found by altunity")
#
#     def test_login(self):
#         print("username added: ", self.email_obj)
#         self.email_obj.set_text(self.registered_email_text)
#         self.pass_obj.set_text(self.registered_pass_text)
#         print("password added: ", self.pass_obj)
#
#         sleep(5)
#         self.btn_obj.tap()
