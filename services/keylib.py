import time

from selenium import webdriver

class KeyLib:
    def __init__(self, driver):
        self.driver = driver

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
        ele_list = args[0].split("=", 1)
        how, what = ele_list[0], ele_list[1]
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
        ele_list = args[0].split("=", 1)
        how, what = ele_list[0], ele_list[1]
        try:
            self.driver.find_element(how, what).click()
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
        ele_list = args[0].split("=", 1)
        how, what = ele_list[0], ele_list[1]
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
        ele_list = args[0].split("=", 1)
        how, what = ele_list[0], ele_list[1]
        try:
            actual = self.driver.find_element(how, what).text
            if actual == args[1]:
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
        time.sleep(args[0])
        return True



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
