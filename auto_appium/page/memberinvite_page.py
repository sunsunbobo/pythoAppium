# from auto_appium.page.contactedit_page import ContactEditPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from auto_appium.page.base_page import BasePage


class MemberInvitePage(BasePage):
    addmember_manualtext = "手动输入添加"
    def addmember_manual(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find_and_click(self.addmember_manualtext)
        from auto_appium.page.contactedit_page import ContactEditPage
        return ContactEditPage(self.driver)

    def get_toast(self):
        text_toast = self.gettoast_text()
        return text_toast