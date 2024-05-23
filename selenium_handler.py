from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Selenium_Handler:
    def __init__(self, logger, username, password):
        self.username = username
        self.password = password
        self.logger = logger
        self.chrome_driver_path = (
            r"C:\Users\johnny\Desktop\repos\chromedriver-win64\chromedriver.exe"
        )
        self.chrome_binary_path = r"C:\Users\johnny\Downloads\chrome-win64\chrome-win64\chrome.exe"  # Update this path if necessary

        # Initialize ChromeOptions and set binary location
        self.options = Options()
        self.options.binary_location = self.chrome_binary_path
        self.options.add_argument("--start-maximized")
        try:
            self.chrome_service = Service(self.chrome_driver_path)
            self.driver = webdriver.Chrome(
                service=self.chrome_service, options=self.options
            )
            print("WebDriver initialized successfully.")
        except Exception as e:
            self.logger(f"An error occurred while initializing the WebDriver: {e}")
            self.driver = None

    def open_instagram(self):
        url = "https://www.instagram.com/"
        self.driver.get(url)
        decline_xpath = "//button[contains(text(), 'Decline optional cookies')]"
        # decline_xpath = (
        #     "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        # )
        if self.is_element(decline_xpath):
            self.click_element(decline_xpath)
        home_nav_xpath = "//span[contains(text(), 'Home')]"
        # self.login()
        # if not self.is_element(home_nav_xpath):
        self.click_element(home_nav_xpath)

    def create_post(self, image_path):
        for _ in range(5):
            try:
                create_nav_xpath = "//span[contains(text(), 'Create')]"
                post_nav_xpath = "//span[contains(text(), 'Post')]"
                self.click_element(create_nav_xpath)
                self.click_element(post_nav_xpath)
                file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
                file_input.send_keys(image_path)
                breakpoint()
                break
            except Exception as e:
                self.logger.error("Failed to create post, retrying..")

    def close_element(self, xpath, timeout=15):
        count = 0
        while self.is_element(xpath):
            count + 1
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].click();", element)
                continue
            except Exception as e:
                self.logger.info(
                    f"js click xpath failed, trying python next: {xpath}" + str(e)
                )
                try:
                    self.logger.info(f"clicking cpath:{xpath}")
                    print(f"clicking cpath:{xpath}")
                    WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    ).click
                    continue
                except:
                    self.logger.error(f"couldn't click xpath: {xpath}" + str(e))
            if count > 4:
                break

    def click_element(self, xpath, timeout=15):
        for _ in range(5):
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                self.driver.execute_script("arguments[0].click();", element)
                break
            except Exception as e:
                self.logger.info(
                    f"js click xpath failed, trying python next: {xpath}" + str(e)
                )
                try:
                    self.logger.info(f"clicking cpath:{xpath}")
                    print(f"clicking cpath:{xpath}")
                    WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    ).click
                    break
                except:
                    self.logger.error(f"couldn't click xpath: {xpath}" + str(e))

    def is_element(self, xpath, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except Exception as e:
            self.logger.error(f"error. {e}")
            return False

    def send_keys(self, xpath, input, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.send_keys(input)
            return True
        except Exception as e:
            self.logger.error(f"failed input. {e}")
            return False

    def login(self, username=None, password=None):
        username_input = "//input[@name='username']"
        password_input = "//input[@name='password']"
        login_btn = "//div[contains(text(), 'Log in')]"
        continue_as_xpath = "//span[contains(text(), 'Continue as ')]/parent::button"
        notifications_no_btn = "//button[contains(text(), 'Not Now')]"
        # if self.is_element(continue_as_xpath):
        #     self.click_element(continue_as_xpath)
        #     return
        self.send_keys(username_input, self.username)
        self.send_keys(password_input, self.password)
        self.click_element(login_btn)
        self.click_element(notifications_no_btn)
