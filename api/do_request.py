import requests


class DoRequests:
    def __init__(self):
        self.req = requests.session()
        self.resp = None

    def do_login(self):
        param = {"username": "admin", "password": "Milor123", "verifycode": "0000"}
        res = self.req.request("post", "http://localhost:8080/woniusales/user/login", param)
        return res.text

    def do_request(self, method, url, param):
        try:
            if param is None:
                self.resp = self.req.request(method, url)
            else:
                self.resp = self.req.request(method, url, param)
            return self.resp
        except Exception as e:
            print(e)

    def get_resp(self, method, url, param, accept_type):
        self.do_request(method, url, param)
        if self.resp is None:
            print("请求未发送成功")
        try:
            if accept_type == "text":
                return self.resp.text
            if accept_type == "json":
                return self.resp.json()[0]
        except Exception as e:
            print(e)

    def get_act(self, precondition, method, url, param, accept_type):
        if precondition == "已登录":
            self.do_login()
            act = self.get_resp(method, url, param, accept_type)
        else:
            act = self.get_resp(method, url, param, accept_type)
        return act


if __name__ == '__main__':
    d = DoRequests()
    # act = d.get_act("无", "post", "http://localhost:8080/woniusales/user/login", {'username': 'admin12', 'password': 'milor123', 'verifycode': '0000'}, "json")
    act = d.get_act( '已登录', 'get', 'http://localhost:8080/woniusales/sell/summary', {'customerphone': '15983123450', 'paymethod': '微信', 'totalprice': '50', 'creditratio': '2.0', 'creditsum': '101', 'tickettype': '无', 'ticketsum': '11', 'oldcredit': '0'}, 'text')
    print(act)