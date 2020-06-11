import unittest

import logging

from api.lohin_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass
    def test01_login_success(self):
        response =self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                       {"Content-Type": "application/json"})
        logging.info("登陆成功的结果为:{}".format(response.json()))
        # 断言
        assert_common(self,200,True,10000,"操作成功",response)
    # 手机号码为空
    def test02_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("登陆成功的结果为:{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    # 密码错误
    def test03_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "error"},
                                        {"Content-Type": "application/json"})
        logging.info("登陆成功的结果为:{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)




