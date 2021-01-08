from appium.webdriver.common.mobileby import MobileBy

from auto_appium.page.base_page import BasePage
from auto_appium.page.memberinvite_page import MemberInvitePage


class AddressListPage(BasePage):
    addmember_text = "添加成员"
    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_scroll_click(self.addmember_text)
        return MemberInvitePage(self.driver)