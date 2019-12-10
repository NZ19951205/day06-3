import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TsetEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api=ApiEmployee()
    # 新增员工
    def test01_post(self,username="zizz123",mobile="18787504243",workNumber="52996"):
    #     调用新增员工方法
        r=self.api.api_post_employee(username,mobile,workNumber)
        print("新增员工 后结果为：",r.json())
    #     提取id
        api.user_id=r.json().get("data").get("id")
        print("新增的员工id为：",api.user_id)
    #     断言
        assert_common(self,r)
    # 更新
    def test02_put(self,username="zizz132"):
        r=self.api.api_put_employee(username)
        print("更新的数据:",r.json())
        assert_common(self,r)
    # 查询
    def test03_get(self):
        r=self.api.api_get_employee()
        print("查询数据结果为:",r.json())
        assert_common(self,r)
    # 删除
    def test04_delete(self):
    #     调用删除业务方法
        r=self.api.api_delete_employee(api.user_id)
        print("删除数据结果为：",r.json())
    #     断言
        assert_common(self,r)