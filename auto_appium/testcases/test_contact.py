from auto_appium.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = "test001"
        gender = "女"
        tel = "13712345678"
        mypage = self.main.goto_addresslist().add_member().addmember_manual().edit_name(name).edit_gender(gender).edit_phonenum(tel).click_save()
        mytoast = mypage.get_toast()
        assert "添加成功" == mytoast