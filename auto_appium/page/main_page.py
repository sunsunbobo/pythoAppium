"""
主页
"""
from appium.webdriver.common.mobileby import MobileBy

from auto_appium.page.addresslist_page import AddressListPage
from auto_appium.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_addresslist(self):
        self.find_and_click(self.addresslist_element)
        self.driver.find_element().click()
        return AddressListPage(self.driver)


    def goto_workbench(self):
        pass