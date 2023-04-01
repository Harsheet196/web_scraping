import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_rknec(self, username: str, password: str):
        self.add_input(by=By.ID, value='j_username', text=username)
        self.add_input(by=By.ID, value='password-1', text=password)
        self.click_button(by=By.CLASS_NAME,
                          value='btn.btn-primary.btn-block.customB.mt-3')

    def find_attendance(self):
        by = By.ID
        attendance = self.browser.find_element(
            by=by, value='attendencePer').text
        print(attendance)


if __name__ == '__main__':
    browser = Browser('drivers\chromedriver.exe')
    browser.open_page('https://rcoem.in/login.htm')
    time.sleep(3)
    browser.login_rknec(username='your rknec email id',
                        password='Upload your password')
    time.sleep(3)
    browser.find_attendance()
    time.sleep(5)
    browser.close_browser()
