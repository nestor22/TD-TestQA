import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
from time import sleep





class DeleteComputer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        self.driver.get('http://computer-database.gatling.io/computers')



    def test_delete_computer(self):
        driver = self.driver

        first_element = driver.find_element_by_xpath('/html/body/section/table/tbody/tr[1]/td[1]/a')
        self.assertTrue(first_element.is_enabled())
        first_element.click()

        sleep(3)
        delete_button = driver.find_elements_by_xpath('/html/body/section/form[2]/input')
        delete_button.click()

        messaje = driver.find_elements_by_xpath('/html/body/section/div[1]/text()')
        self.assertTrue(messaje)


  
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'Delete-report'))



