import time

from selenium import webdriver
from KDT_MODULE.services.parseXLS import Parse
from KDT_MODULE.services.keylib import KeyLib
from KDT_MODULE.services.collector import Collector

class Excuter:

    def __init__(self):
        self.driver = None
        self.collector = Collector()

    @classmethod
    def get_driver(cls, browser='chrome'):
        browser.lower()
        if browser == "chrome":
            cls.driver = webdriver.Chrome()
        elif browser == "edge":
            cls.driver = webdriver.Edge()
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        else:
            print("请选择chrmoe、edge、firefox任一种浏览器输入")
        cls.driver.maximize_window()
        return cls.driver

    def runner(self):
        p = Parse("../testdata/case1.xls")
        p.get_sheet("Sheet1")
        tcs = p.prepare_tc()
        for tc in tcs:
            rlts = []
            self.driver = self.get_driver()
            keylib = KeyLib(self.driver)
            rdict = self.collector.get_data(tc)
            for step in tc.steps:
                time.sleep(1)
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
            self.collector.get_result(rdict, rlts)
            self.driver.close()
            self.collector.print_rltlist()

if __name__ == '__main__':
    exe = Excuter()
    exe.runner()
