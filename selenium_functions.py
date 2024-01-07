from selenium_functions import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class Selenium():
    def __init__():
        pass
    
    def open_instagram():
        chrome_driver_path = 'C:\Users\johnny\Downloads\chromedriver_win32'
        chrome_service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service)

        url = 'https://www.instagram.com/'

        driver.get(url)

    def login(username, password):
        pass