import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class KeyLib:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def deal_args(self, args):
        """
        功能：处理参数，分解出环境的how，what
        :param args:
        :return:
        """
        ele_list = args[0].split("=", 1)
        how, what = ele_list[0], ele_list[1]
        how = how.replace("_", " ")
        return how, what

    def open(self, *args):
        """
        功能：打开指定url页面，如果url不能到达，返回None
        :param url:
        :return:
        """
        try:
            self.driver.get(args[0])
            return True
        except Exception as e:
            print(e)
        return False

    def input(self, *args):
        """
        通过how与what定位元素，将param填入元素中去
        :param how:
        :param what:
        :param param:
        :return:
        """
        how, what = self.deal_args(args)
        try:
            self.driver.find_element(how, what).send_keys(args[1])
            return True
        except Exception as e:
            print(e)
        return False

    def click(self, *args):
        """
        功能：根据how与what定位后，点击元素
        :param how:
        :param what:
        :return:
        """
        how, what = self.deal_args(args)
        try:
            self.driver.find_element(how, what).click()
            return True
        except Exception as e:
            print(e)
        return False

    def clear(self, *args):
        """
        清除输入框的内容
        :param args:
        :return:
        """
        how, what = self.deal_args(args)
        try:
            self.driver.find_element(how, what).clear()
            return True
        except Exception as e:
            print(e)
        return False


    def select(self, *args):
        """
        功能：通过不同选项选择下拉框
        :param args:
        :return:
        """
        how, what = self.deal_args(args)
        method = args[1].split(">", 1)[0]
        content = args[1].split(">", 1)[1]
        slt = Select(self.driver.find_element(how, what))
        try:
            if method == "index":
                slt.select_by_index(int(content))
            elif method == "value":
                slt.select_by_value(content)
            elif method == "text":
                slt.select_by_visible_text(content)
            else:
                print("请输入正确的查找参数")
            return True
        except Exception as e:
            print(e)
        return False

    def choose_alter(self, *args):
        """
        功能：进行弹窗操做
        :param args:
        :return:
        """
        try:
            if args[0] == "确定":
                self.driver.switch_to.alert.accept()
            elif args[0] == "取消":
                self.driver.switch_to.alert.dismiss()
            elif args[0] == "写入":
                dr = self.driver.switch_to.alert
                dr.send_keys(args[1])
                dr.accept()
            else:
                print("填入数据错误")
            return True
        except Exception as e:
            print(e)
        return False


    def should_contain(self, *args):
        """
        功能：在page_source中查找是否存在expected字符串，有则返回True
        :param expected:
        :return: boolean
        """
        if args[0] in self.driver.page_source:
            return True
        return False

    def should_exists(self, *args):
        """
        功能：查找元素是否存在，存在则返回True
        :param how:
        :param what:
        :return: boolean
        """
        how, what = self.deal_args(args)
        try:
            self.driver.find_element(how, what)
            return True
        except Exception as e:
            print(e)
        return False

    def should_eq(self, *args):
        """
        功能：查找指定元素的text属性，然后与expected进行对比，相同则返回True
        :param how:
        :param what:
        :param expected:
        :return: boolean
        """
        how, what = self.deal_args(args)
        try:
            actual = self.driver.find_element(how, what).text
            if actual == args[1]:
                return True
        except:
            pass
        return False

    def should_alter_text(self, *args):
        try:
            if args[0] == "contain":
                if args[1] in self.driver.switch_to.alert.text:
                    return True
            elif args[0] == "eq":
                if args[1] == self.driver.switch_to.alert.text:
                    return True
        except:
            pass
        return False

    def sleep_time(self, *args):
        """
        功能：等待时间
        :param args: 等待的秒数
        :return:
        """
        try:
            time.sleep(float(args[0]))
            return True
        except:
            pass
        return False


if __name__ == '__main__':
    dr = webdriver.Chrome()
    kl = KeyLib(dr)
    kl.open("http://localhost:8080/woniusales")
    kl.input("id=username", "admin")
    kl.input("id=password", "Milor123")
    kl.input("id=verifycode", "0000")
    kl.click("xpath=/html/body/div[4]/div/form/div[6]/button")
    # t = dr.page_source
    print(kl.should_contain("注销"))
    # dr.get("http://localhost:8080/woniusales")