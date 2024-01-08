from selenium_functions import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class Selenium():
    def __init__():
        chrome_driver_path = 'C:\Users\johnny\Downloads\chromedriver_win32'
        chrome_service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service)
    
    def open_instagram(self):
        url = 'https://www.instagram.com/'
        self.driver.get(url)
        home_nav_xpath = "//span[contains(text(), 'Home')]"
        home_button = self.driver.find_elements(By.XPATH, home_nav_xpath)
        home_button.click()
        if not home_button:
            self._login()

    def create_post(self, image_path):
        create_nav_xpath = "//span[contains(text(), 'Create')]"
        post_nav_xpath = "//span[contains(text(), 'Post')]"
        create_button = self.driver.find_elements(By.XPATH, create_nav_xpath)
        post_button = self.driver.find_elements(By.XPATH, post_nav_xpath)
        create_button.click()
        post_button.click()
        select_xpath = "//span[contains(text(), 'Select from computer')]"
        select_button = self.driver.find_elements(By.XPATH, select_xpath)
        select_button.click()
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(image_path)

    def _login(self, username=None, password=None):
        continue_as_xpath = "//span[contains(text(), 'Continue as ')]/parent::button"
        login_button = self.driver.find_element(By.XPATH, continue_as_xpath)
        login_button.click()