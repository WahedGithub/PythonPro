import unittest
from appium import webdriver
import time

class WhatsappAndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Galaxy S8'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")
        search_button.click()
        time.sleep(1)

        name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
        name_search_box.send_keys("Ather")

        time.sleep(1)
        msg = self.driver.find_element_by_android_uiautomator('new UIselector().textContains("Ather")')
        msg.click()

        text_box = self.driver.find_element_by_id("com.whatsapp:id/entry")
        text_box.send_keys("Aya miyan Appium se message......")

        send_button = self.driver.find_element_by_id("com.whatsapp:id/send")
        send_button.click()
        time.sleep(3)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)