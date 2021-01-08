import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True,
            'dontStopAppOnReset': True,
            'skipDeviceInitialization': True,
            'unicodeKeyBoard': True,
            'resetKeyBoard': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

    @pytest.mark.parametrize('searchkey, type, price',[('alibaba','BABA',230),('xiaomi','01810',33)],ids=['ali', 'xiaomi'])
    def test_search(self, searchkey, type, price):
        print("test search")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # locator = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text = "searchkey"]')
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        #  and @text = "阿里巴巴"]
        current_price = float(self.driver.find_element_by_xpath(f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert_that(current_price, close_to(price, price*0.1))


    def test_case(self):
        ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        assert ele.is_displayed() == True
        print(ele.get_attribute('name'))
        print(ele.location)
        print(ele.size)
        ele.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        ele1 = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text = "阿里巴巴"]')
        if ele1.is_displayed() == True:
            print("搜索成功")
        else:
            print("搜索失败")

    def test_touch_action(self):
        action = TouchAction(self.driver)
        width = self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        # action.press(x=int(width/2), y=int(height*80%)).wait(200).move_to(x=int(width/2), y=int(height*20%)).release().perform()

    def test_ui_auto(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("1234")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        assert_that(10, equal_to(10), '这是一个提示')
        assert_that(8, close_to(10,2))
        assert_that('contains some string', contains_string('string'))


# if __name__=='__main__':
#     pytest.main()
