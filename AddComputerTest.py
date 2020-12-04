import csv, unittest
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from ComputerDatabasePage import ComputerDatabasePage as CP


def get_data(file_name):
    rows = []
    data_file= open(file_name, 'r')
    reader= csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows

    

@ddt
class AddComputerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')


    @data(*get_data('textdata.csv'))
    @unpack
    def test_add_computer(self, name, introduced, discontinued, company):
        computer = CP(self.driver)
        computer.open()
        computer.type_name(str(name))
        computer.type_introduced(str(introduced))
        computer.type_discontinued(str(discontinued))
        computer.select_company(str(company))
        computer.click_submit()
        messaje = self.driver.find_element_by_css_selector('#main > div.alert-message.warning > strong')
        self.assertTrue(messaje)
        print(messaje)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'hello-world-report'))