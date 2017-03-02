# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Fixber_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Fixber_test(self):
        success = True
        wd = self.wd
        wd.get("http://fixber.com/")
        wd.find_element_by_css_selector("li").click()
        wd.find_element_by_xpath("//div[@class='maincol']/table/tbody/tr/td[1]/div[2]/table/tbody/tr[1]/td[2]/a/img").click()
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys("VINTEM")
        wd.find_element_by_name("passw").click()
        wd.find_element_by_name("passw").clear()
        wd.find_element_by_name("passw").send_keys("E6FFBC")
        wd.find_element_by_name("btn").click()
        wd.find_element_by_xpath("//div[@id='TB_ajaxContent']/div/input").click()
        wd.find_element_by_xpath("//div[@class='ad']/div[6]/a/img").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
