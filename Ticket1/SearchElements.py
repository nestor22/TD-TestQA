import csv
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner



def get_data(file_name):
    rows = []
    data_file= open(file_name, 'r')
    reader= csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows

    

@ddt
class SearchElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        self.driver.get('http://computer-database.gatling.io/computers')



    @data(*get_data('searchdata.csv'))
    @unpack
    def test_search_computer(self, search_value):
        driver = self.driver

        search_field = driver.find_element_by_xpath('/html/body/section/div[1]/form/input[1]')
        self.assertTrue(search_field.is_enabled())


        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('/html/body/section/table/tbody/tr/td/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertNotEqual((len(products)), 0)

        
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'Search-report'))


