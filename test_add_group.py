# # -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/addressbook/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_groups_page(driver)
        self.create_new_groupe(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_link_text("Logout").click()

    def create_new_groupe(self, driver):
        # init groupe creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("12")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("12")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("12")
        # submit group
        driver.find_element_by_name("submit").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("LoginForm").submit()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("qwe")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("qwe")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("qwe")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_link_text("Logout").click()
    
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    #
    # def tearDown(self):
    #     # To know more about the difference between verify and assert,
    #     # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
