from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import random
import time
import hello

class ChangeProxy:
    @staticmethod
    def change_proxy(option):
        driver = webdriver.Chrome(service=Service('./chromedriver'), options=option)
        proxy = NewProxy.proxy(driver=driver)
        print(proxy)
        option.add_argument(f'--proxy-server={proxy}')
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
        driver = webdriver.Chrome(service=Service('./chromedriver'), options=option)
        return driver

import global_variables
