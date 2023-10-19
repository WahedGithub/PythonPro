import unittest #unittest is the framework in python inbuild in default package, to organize the testcases unittest is used
from appium import webdriver #appium library me webdriver ek class hai from selenium, webdriver = super class in selenium, in appium mobiledriver is the super class
import time

class WhatsappAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {} #it is a selenium class and appium uses the selenium class
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Samsung S8'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)# appium is server so to call the server remote is called

    def tearDown(self): #it is the part of unittest and it will close everything
        self.driver.quit()

    def test_text_friend(self):

        search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")# for finding element id we have 8 methods= xpath, accessiblity id, tag name, link text, 
        search_button.click()# .click is the class in appium

        name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
        name_search_box.send_keys("Ather")

        msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Ather")')
        msg.click()
        time.sleep(2)
        text_box1 = self.driver.find_element_by_id("com.whatsapp:id/entry")
        text_box1.send_keys("Appium se send krro message ye")
        time.sleep(3)
        send_button = self.driver.find_element_by_id("com.whatsapp:id/send")
        send_button.click()
        time.sleep(8)
	
if __name__ == '__main__': #this can be used only when single class is used as all the classes have the same name.
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)