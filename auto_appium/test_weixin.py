from time import sleep
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, equal_to
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeChat:
    def setup(self):
        desired_cap = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            # 'appPackage': 'com.xueqiu.android',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            # 'appActivity': 'com.xueqiu.android.common.MainActivity',
            'noReset': True,
            'dontStopAppOnReset': True,
            'skipDeviceInitialization': True,
            'unicodeKeyBoard': True,
            'resetKeyBoard': True,
            'settings[waitForIdleTimeout]': 0
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_appium(self):
        sendtext = 'hello1'
        self.driver.find_element(MobileBy.ID, 'ie_').click()
        self.driver.find_element(MobileBy.ID, 'gwt').send_keys('孙博')
        self.driver.find_element(MobileBy.ID, 'eae').click()
        self.driver.find_element(MobileBy.ID, 'etm').send_keys(sendtext)
        self.driver.find_element(MobileBy.ID, 'eti').click()

        ele1 = self.driver.find_element(MobileBy.ID, 'et8')
        # print(ele[-1].text)
        # assert sendtext == ele1[-1].text

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        sleep(5)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hzp').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/awm').click()
        message = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/pt').text
        assert message == '外出打卡成功'
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="打卡"]').click()

    @pytest.mark.parametrize("name, gender,phonenum", yaml.safe_load(open('./data/addcontact.yml',encoding = 'utf-8')))
    def test_addcontact(self,name,gender,phonenum):
        # name = "test001"
        # gender = "女"
        # tel = "13712345678"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@text="手机号"]').send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        toastlocator = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toastlocator))
        text_toast = self.driver.find_element(*toastlocator).text
        assert text_toast == "添加成功"



