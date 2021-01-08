# from auto_appium.page.memberinvite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy

from auto_appium.page.base_page import BasePage


class ContactEditPage(BasePage):
    contact_input_name = (MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]')
    contact_input_gender_male = (MobileBy.XPATH, '//*[@text="男"]')
    contact_input_gender_female = (MobileBy.XPATH, '//*[@text="女"]')
    contact_input_tel = (MobileBy.XPATH,
                                 '//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@text="手机号"]')
    contact_save_button = (MobileBy.XPATH, '//*[@text="保存"]')
    def edit_name(self,name):
        self.find_and_sendkeys(self.contact_input_name)
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        return self

    def edit_gender(self,gender):
        self.find_and_click(self.contact_input_gender_male)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        if gender == "女":
            self.find_and_click(self.contact_input_gender_female)
        else:
            self.find_and_click(self.contact_input_gender_male)
        return self

    def edit_phonenum(self,phonenum):
        self.find_and_sendkeys(self.contact_input_tel,phonenum)
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@text="手机号"]').send_keys(phonenum)
        return self

    def click_save(self):
        self.find_and_click(self.contact_save_button)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        from auto_appium.page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)