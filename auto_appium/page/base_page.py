from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)


    def find_and_click(self,locator):
        self.find(locator).click()

    def find_and_sendkeys(self,locator,value):
        self.find(locator).send_keys(value)

    def find_scroll_click(self,text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));')
        self.find_and_click(ele)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def gettoast_text(self):
        toastlocator = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toastlocator))
        return self.find_and_get_text(toastlocator)