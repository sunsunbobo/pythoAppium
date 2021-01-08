from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWV:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            # 'appPackage': 'com.xueqiu.android',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings',
            # 'appActivity': 'com.xueqiu.android.common.MainActivity',
            'noReset': True,
            'dontStopAppOnReset': True,
            'skipDeviceInitialization': True,
            'unicodeKeyBoard': True,
            'resetKeyBoard': True
            # 'chromedriverExecutable': '/Users/chromedriver'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_webview(self):
        # self.driver.find_element_by_xpath('//*[@text="交易"]')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]')
        A_locator = (MobileBy.XPATH, '//h1[@text="A股开户"]')
        print(self.driver.contexts)
        self.driver.switch_to.content(self.driver.contexts[-1])
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        phone_locator = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("13810212345")
        self.driver.find_element(By.ID, 'code').send_keys("1234")
        self.driver.find_element(By.XPATH, '//h1[@text="立即开户"]').click()

    def test_sendcall(self):
        self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        self.driver.send_sms('5551234567', "hello")
        self.driver.set_network_connection()

