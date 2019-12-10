import requests

import api


class ApiLogin:
    # 初始化url
    def __init__(self):
        self.url=api.BASE_URL+"/api/sys/login"
    # 登录
    def api_login(self,mobile,password):
        data={"mobile":mobile,"password":password}
        # 请求登录
        return requests.post(url=self.url,json=data)

# if __name__ == '__main__':
