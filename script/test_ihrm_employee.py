# 导包
import unittest, logging
import app
from api.empoly_api import EmployeeApi
from api.lohin_api import LoginApi

# 创建测试类
class TestIHRMEmployee(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type":"application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))