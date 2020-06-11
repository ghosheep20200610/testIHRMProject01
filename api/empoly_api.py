# 导包
import requests


# 创建要封装的员工类
class EmployeeApi:

    def __init__(self):
        # 定义员工模块的URL
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    def add_emp(self, username, mobile, headers):
        # 根据外部传入的username和mobile拼接成要发送的请求体数据
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        query_url = self.emp_url + "/" + emp_id
        return requests.get(url=query_url, headers=headers)

    def modify_emp(self, emp_id, jsonData, headers):
        modify_url = self.emp_url + "/" + emp_id
        return requests.get(url=modify_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        delete_url = self.emp_url + "/" + emp_id
        return requests.get(url=delete_url, headers=headers)
