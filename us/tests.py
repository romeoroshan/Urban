from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'
    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login/"]')
        login.click()
        print('redirection to login')
        time.sleep(2)
        email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][name="email"]')
        email.send_keys("futurefc@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"][name="password"]#id_password')
        password.send_keys("Romeo!0481")
        print('Typed email and password')
        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.text-light.p-2.w-50.mt-3')
        submit.click()
        print('logged in')
        time.sleep(2)

        feeds = driver.find_element(By.CSS_SELECTOR, 'a[href="/tournaments"]')
        feeds.click()
        time.sleep(2)
        print('Showing tournaments')
        host = driver.find_element(By.CSS_SELECTOR, 'a[href="/hosted_tour"]')
        host.click()
        time.sleep(2)
        print('Showing hosted tournaments')
        part = driver.find_element(By.CSS_SELECTOR, 'a[href="/tour_participants/22"]')
        part.click()
        time.sleep(2)
        print('Viewing participants')
        logout = driver.find_element(By.CSS_SELECTOR, 'a[href="/logout/"]')
        logout.click()
        print('logged out')
        time.sleep(2)
        

if __name__ == '__main__':
    import unittest
    unittest.main()