import time

from selenium import webdriver
from KDT_Selenium_Python.services.parseXLS import Parse
from KDT_Selenium_Python.services.keylib import KeyLib
from KDT_Selenium_Python.services.collector import Collector


class Excuter:

    def __init__(self):
        self.driver = None
        self.collector = Collector()

    @classmethod
    def get_driver(cls, browser='chrome'):
        """
        功能：获取driver
        :param browser: 选择需要打开的驱动
        :return: 驱动
        """
        browser.lower()
        if browser == "chrome":
            cls.driver = webdriver.Chrome()
        elif browser == "edge":
            cls.driver = webdriver.Edge()
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        else:
            print("请选择chrmoe、edge、firefox任一种浏览器输入")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        return cls.driver

    def runner(self, browser):
        p = Parse("../testdata/case1.xls")  # 打开测试用例
        p.get_sheet("Sheet1")  # 通过名字选择xls文件的sheet页
        tcs = p.prepare_tc()  # 准备测试脚本
        for tc in tcs:
            if tc.mark == 1:
                rlts = []  # 用于存放测试结果
                self.driver = self.get_driver(browser=browser)
                keylib = KeyLib(self.driver)
                rdict = self.collector.get_data(tc)  # 将测试用例存放进收集器的字典中
                for step in tc.steps:  # 分解步骤，执行操作，保存结果
                    rlt = None
                    key = step["key"]
                    obj = step["object"]
                    if hasattr(keylib, key):
                        func = getattr(keylib, key)
                        if len(step) == 2:
                            rlt = func(obj)
                        elif len(step) == 3:
                            rlt = func(obj, step["param"])
                    rlts.append(rlt)
                    # time.sleep(1)
                if False in rlts:
                    result = "fail"
                else:
                    result = "pass"
                self.collector.get_result(rdict, rlts, result)
                self.driver.close()
        # self.collector.print_rltlist()


if __name__ == '__main__':
    exe = Excuter()
    exe.runner("chrome")