"""
存放App端特有的操作，启动应用，关闭应用，重启应用，进入到首页
"""
from appium import webdriver
from auto_appium.page.base_page import BasePage
from auto_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        # 复用app的判断
        if self.driver == None:
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
        else:
            # self.driver.start_activity()
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        return MainPage(self.driver)

