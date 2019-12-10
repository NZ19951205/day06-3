def assert_common(self,response,status_code=200,msg="操作成功！"):
    # 状态码
    self.assertEqual(status_code,response.status_code)
    # 断言cuccess
    self.assertTrue(response.json().get("success"))
    # 断言code
    self.assertEqual(10000,response.json().get("code"))
    # 断言mgs
    self.assertEqual(msg,response.json().get("message"))