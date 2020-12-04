
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class ComputerDatabasePage(object):
    def __init__(self, driver):
        self._driver = driver 
        self._url = 'http://computer-database.gatling.io/computers/new'
    
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(Ec.presence_of_element_located((By.CSS_SELECTOR, '#main > h1')))
        return True
    
    def open(self):
        self._driver.get(self._url)

    
    def type_name(self, computer_name):
        input_name = self._driver.find_element_by_id('name')
        input_name.clear()
        input_name.send_keys(computer_name) 


    def type_introduced(self, introduced):
        input_introduced = self._driver.find_element_by_id('introduced')        
        input_introduced.clear()
        input_introduced.send_keys(introduced) 


    def type_discontinued(self, discontinued):
        input_discontinued = self._driver.find_element_by_id('discontinued')
        input_discontinued.clear()
        input_discontinued.send_keys(discontinued) 

    
    def select_company(self, company):
        select_company = Select(self._driver.find_element_by_id('company'))
        select_company.select_by_value(company) 
    

    def click_submit(self):
        create_computer_button = self._driver.find_element_by_css_selector('#main > form > div > input')
        create_computer_button.click()
    

    
