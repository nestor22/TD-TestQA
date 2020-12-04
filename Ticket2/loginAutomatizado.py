import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
import os


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://opencart.abstracta.us/index.php?route=account/login')


    def test_new_user(self):
        USUARIO = os.envirion.get('USUARIO_QA_TEST')
        PASSWORD = os.envirion.get('PASSWORD_QA_TEST')

        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/button[3]').click()
        driver.find_element_by_xpath('/html/body/div/div[3]/p[2]/a').click()


        email_address = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input')
        pass_input = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input')
        
        submit_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/form/input')
        self.assertTrue(email_address.is_enabled() 
        and pass_input.is_enabled())

        email_address.send_keys(USUARIO)
        pass_input.send_keys(PASSWORD)
        submit_button.click()
        my_accout_title = driver.find_element_by_xpath('/html/body/div[2]/div/div/h2[1]')
        self.assertTrue(my_accout_title)





    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'login-report'))

