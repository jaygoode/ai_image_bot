from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Selenium_Handler:
    def __init__(self):
        self.chrome_driver_path = (
            r"C:\Users\johnny\Desktop\repos\chrome-win64\chrome.exe"
        )
        # self.chrome_service = Service(ChromeDriverManager().install())
        self.chrome_service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.chrome_service)

    def open_instagram(self):
        url = "https://www.instagram.com/"
        self.driver.get(url)
        home_nav_xpath = "//span[contains(text(), 'Home')]"
        home_button = self.driver.find_elements(By.XPATH, home_nav_xpath)
        breakpoint()
        if not home_button:
            self._login()
        home_button.click()

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
        breakpoint()
